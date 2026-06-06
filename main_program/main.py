import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import httpx

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    async def on_ready(self):
        print(f'Connecté en tant que {self.user}!')
        print('Connection réussie !')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if self.user in message.mentions:
            question = message.content.replace(f'<@{self.user.id}>', '').strip()
            
            if not question:
                await message.reply("Tu m'as mentionné mais tu n'as rien dit")
                return
            
            async with message.channel.typing():
                async with httpx.AsyncClient(timeout=150.0) as http_client:
                    response = await http_client.post(
                        "http://localhost:8000/chat",
                        json={"message": question}
                    )
                    data = response.json()
            
            await message.reply(data["response"])

        reponse = data["response"]

# si la réponse dépasse 2000 caractères, on la coupe en morceaux
        if len(reponse) <= 2000:
            await message.reply(reponse)
        else:
    # envoyer le premier morceau en reply, le reste en messages suivants
            morceaux = [reponse[i:i+1900] for i in range(0, len(reponse), 1900)]
            await message.reply(morceaux[0])
            for morceau in morceaux[1:]:
                await message.channel.send(morceau)

    async def setup_hook(self):
        guild = discord.Object(id=1452041121977864268)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

client = MyClient()

@client.tree.command(name="hello", description="Saluer l'utilisateur")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Salut {interaction.user.display_name} !")

@client.tree.command(name="avatar", description="Afficher l'avatar de l'utilisateur")
async def avatar(interaction: discord.Interaction):
    await interaction.response.send_message(f"Voici l'avatar de {interaction.user.display_avatar}")

@client.tree.command(name="ask", description="Discuter et demander à MIPO !")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    
    async with httpx.AsyncClient(timeout=150.0) as http_client:
        response = await http_client.post(
            "http://localhost:8000/chat",
            json={"message": question}
        )
        data = response.json()
    
    await interaction.followup.send(data["response"])

client.run(TOKEN)