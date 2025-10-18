from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        # Initialize each assistant if string exists
        self.one = self.two = self.three = self.four = self.five = None

        if config.STRING1:
            self.one = Client(
                name="VillanAss1",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING1),
                no_updates=True,
            )
        if config.STRING2:
            self.two = Client(
                name="VillanAss2",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING2),
                no_updates=True,
            )
        if config.STRING3:
            self.three = Client(
                name="VillanAss3",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING3),
                no_updates=True,
            )
        if config.STRING4:
            self.four = Client(
                name="VillanAss4",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING4),
                no_updates=True,
            )
        if config.STRING5:
            self.five = Client(
                name="VillanAss5",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING5),
                no_updates=True,
            )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")

        assistants_map = [
            ("one", self.one),
            ("two", self.two),
            ("three", self.three),
            ("four", self.four),
            ("five", self.five),
        ]

        for idx, (attr_name, client) in enumerate(assistants_map, start=1):
            if client:
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
        for client in [self.one, self.two, self.three, self.four, self.five]:
            if client:
                try:
                    await client.stop()
                except Exception:
                    pass