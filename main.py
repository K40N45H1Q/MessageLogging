from os import getenv
from dotenv import load_dotenv, set_key
from pyrogram import Client
from pyrogram.filters import Message, incoming, private, outgoing

load_dotenv()

client = Client(
    name="logger",
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH")
)

@client.on_message(incoming | outgoing & private)
async def message_logging(client: Client, message: Message):
    if not getenv("FORWARD_CHAT_ID"):
        channel = client.create_channel("Message logging 💬")
        set_key(
            dotenv_path=".env",
            key_to_set="FORWARD_CHAT_ID",
            value_to_set=str(channel.id)
        )
    if message.chat.id in [contact.id for contact in await client.get_contacts()]:
        await message.forward(getenv("FORWARD_CHAT_ID"))

print("Message logging started successfully!")

if __name__ == "__main__":
    client.run()