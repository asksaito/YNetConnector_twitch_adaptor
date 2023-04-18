import os
import twitchio
from yukarinet_connector_client import call_yukarinet_connector

# Load environment variables
channel_name = os.environ["TWITCH_CHANNEL_NAME"]
oauth_token = os.environ["TWITCH_OAUTH_TOKEN"]

class Bot(twitchio.Client):
    async def event_message(self, message):
        print(message.content)
        call_yukarinet_connector(message.content)

# Execute Bot
if __name__ == "__main__":
    print("twitch_chat_client is running...")

    bot = Bot(
        token=oauth_token,
        initial_channels=[channel_name],
    )
    bot.run()

    print("twitch_chat_client is stopped.")
