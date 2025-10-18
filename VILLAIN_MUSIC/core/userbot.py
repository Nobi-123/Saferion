from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        # Initialize up to 5 assistants if strings exist
        self.clients = []
        strings = [
            ("VillanAss1", config.STRING1),
            ("VillanAss2", config.STRING2),
            ("VillanAss3", config.STRING3),
            ("VillanAss4", config.STRING4),
            ("VillanAss5", config.STRING5),
        ]
        for name, string in strings:
            if string:
                client = Client(
                    name=name,
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(string),
                    no_updates=True,
                )
                self.clients.append(client)

    async def start(self):
        LOGGER(__name__).info(f"Starting {len(self.clients)} Assistant(s)...")
        for idx, client in enumerate(self.clients, start=1):
            try:
                await client.start()
                assistants.append(idx)
                # Optional: auto join support groups
                try:
                    await client.join_chat("TechNodeCoders")
                    await client.join_chat("TNCmeetup")
                except Exception:
                    pass

                # Send startup message to log group
                await client.send_message(config.LOGGER_ID, f"Assistant {idx} Started ✅")
                client.id = client.me.id
                client.name = client.me.mention
                client.username = client.me.username
                assistantids.append(client.id)
                LOGGER(__name__).info(f"Assistant {idx} Started as {client.name}")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account {idx} failed to start or access log group: {e}"
                )

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        for client in self.clients:
            try:
                await client.stop()
            except Exception:
                pass