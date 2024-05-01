
# Discord Bot

This Discord bot uses the Google AI Generative Language API to generate responses based on user queries. It also provides search functionality using Google search.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Luciferair/Discord-bot.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:

   Create a `.env` file in the root directory with the following contents:

   ```plaintext
   TOKEN=YOUR_DISCORD_BOT_TOKEN
   BOT_ID=YOUR_BOT_ID
   MY_ID=YOUR_DISCORD_ID
   API_KEY=YOUR_GEMINI_API_KEY
   ```

   Replace `YOUR_DISCORD_BOT_TOKEN`, `YOUR_BOT_ID`, `YOUR_DISCORD_ID`, and `YOUR_GEMINI_API_KEY` with your actual Discord bot token, bot ID, Discord ID, and Gemini API key, respectively.

## Usage

- Run the bot:

   ```bash
   python main.py
   ```

- Use the bot in your Discord server by mentioning it and typing your query.
- The bot will respond with generated content from the Google AI Generative Language API and relevant search links from Google.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## Credits

- Discord.py: https://github.com/Rapptz/discord.py
- Google AI Generative Language API: https://googleapis.dev/python/ai-generativelanguage/latest/index.html
- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `YOUR_DISCORD_BOT_TOKEN`, `YOUR_BOT_ID`, `YOUR_DISCORD_ID`, and `YOUR_GEMINI_API_KEY` with your actual credentials. You can also customize the README further to include more specific details about your project.
