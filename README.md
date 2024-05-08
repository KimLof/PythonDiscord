# Discord Bot Project

This is a simple Discord bot that provides basic functionalities such as tracking the time users spend in voice channels and giving random responses to users' questions.

## Setup

The following instructions will help you get the bot running on your Discord server.

### Prerequisites

- Python 3.6 or higher
- discord.py library
- Python `dotenv` library for handling environment variables (optional)

### Installation

1. Clone the repository to your machine.
    ```bash
    git clone https://github.com/KimLof/PythonDiscord.git
    ```

2. Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.py` file in the root of the project and add your Discord bot token to it. More information on this in step 2 below.
    ```plaintext
    TOKEN = YourBotTokenHere
    ```

4. Run the bot.
    ```bash
    python bot.py
    ```

### Adding the Bot to a Discord Server

1. Go to the Discord Developer portal and create a new application.
2. Create a bot user for your application and copy the bot token.
3. Create an OAuth2 URL using the "OAuth2 URL Generator" tool. Choose "bot" as the scope and define the necessary permissions.
4. Open the generated URL in your browser and add the bot to your desired Discord server.

## Commands

The bot supports the following commands:

- `!hello`: Bot responds with a greeting.
- `!ask`: Bot gives a random response from a predefined file.
- `!time`: Shows how long you have been in the current voice channel.
- `!totaltime`: Shows the total time you have spent in voice channels.

The `!ask` command requires a `ask.txt` file in the root. You can add responses there, each separated by a new line. The bot will randomly choose one of them when `!ask` is called.
