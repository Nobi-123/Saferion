from pyrogram import Client
import config
from ..logging import LOGGER

# -----------------------------
# Hardcoded Log Group ID
# -----------------------------
LOGGER_ID = -1003133341793  # Replace with your log group's ID
UPDATE_CHANNEL = "TechNodeCoders"  # The support/update channel

# Track assistants globally
assistants = []
assistant_ids = []

class Userbot(Client):
    def __init__(self):
        """
        Initializes up to 5 assistant clients using session strings from config.
        """
        self.clients = []
        # Gather session strings from config (STRING1 to STRING5)
        strings = [getattr(config, f"STRING{i}") for i in range(1, 6)]
        
        for i, string in enumerate(strings, start=1):
            if string:
                client = Client(
                    name=f"VILLAINAss{i}",
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(string),
                    no_updates=True
                )
                self.clients.append(client)
            else:
                self.clients.append(None)

    async def start(self):
        """
        Starts all assistants, logs their info, joins the update channel, and sends a startup message.
        """
        LOGGER(__name__).info("Starting Assistants...")
        for i, client in enumerate(self.clients, start=1):
            if client:
                await client.start()
                assistants.append(i)
                
                # Track IDs and usernames
                client.id = client.me.id
                client.name = client.me.mention
                client.username = client.me.username
                assistant_ids.append(client.id)

                # Join the update/support channel safely
                try:
                    await client.join_chat(UPDATE_CHANNEL)
                except Exception:
                    LOGGER(__name__).warning(
                        f"Assistant {i} could not join the update channel '{UPDATE_CHANNEL}'. "
                        "Maybe already joined or missing permission."
                    )

                # Send startup message to hardcoded log group
                try:
                    await client.send_message(LOGGER_ID, f"Assistant {i} Started")
                except Exception:
                    LOGGER(__name__).error(
                        f"Assistant Account {i} failed to access the log group! "
                        "Make sure it is added and promoted as admin."
                    )
                    exit()

                LOGGER(__name__).info(f"Assistant {i} started as {client.name}")

    async def stop(self):
        """
        Stops all assistants safely.
        """
        LOGGER(__name__).info("Stopping Assistants...")
        for client in self.clients:
            if client:
                try:
                    await client.stop()
                except Exception:
                    pass