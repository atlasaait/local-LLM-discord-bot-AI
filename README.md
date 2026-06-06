# 1.Discord bot with built-in AI
The first version (v0.5) of a Discord bot (using discord.py) that runs locally, with a few slash commands (/command).

The whole thing is designed to connect to an API I created myself, with the aim of this API connecting to an AI model via Ollama (llama3.2:1b) running locally (on a computer, but with better performance on a server, even a very small one, so as not to overburden the CPU)

Future versions? Absolutely possible, to improve the performance of the bot’s main code, as well as the API’s capabilities, and to refine the sending and receiving of requests.

Translated with DeepL.com (free version)

# 2.Key Tools
A standard approach, where the architecture simply involves using discord.py (with discord.txt), which will allow the client to connect (all admin and moderation settings are configured in the Discord Dev Portal)

Next, a connection is established to the API (using the FastAPI framework, the Uvicorn server, and finally HTTPX for request handling)

The API then queries the Ollama model (downloadable online and used via the documentation at https://ollama.readthedocs.io/)

The CPU must be powerful enough to support the real-time processing of the selected model, as well as the response time and potential hosting requirements

Translated with DeepL.com (free version)
