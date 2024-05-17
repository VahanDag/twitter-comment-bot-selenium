# Twitter Comment Bot

This is a simple Twitter bot that automatically comments on the latest tweet under a specific hashtag with a random selection of words(to bypass the Twitter bot security) or specific comments that you selected. The bot uses Python and Selenium to interact with the Twitter web interface.

## Features
- Logs into Twitter using provided credentials.
- Navigates to the latest tweets under a specified hashtag.
- Comments on the latest tweet with a random selection of words and a base comment.
- Avoids commenting on the same tweet multiple times.

## Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome browser version)

### Install Dependencies
1. Clone this repository to your local machine.
    ```sh
    git clone https://github.com/yourusername/twitter-comment-bot.git
    cd twitter-comment-bot
    ```

2. Create a virtual environment and activate it (optional but recommended).
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages.
    ```sh
    pip install -r requirements.txt
    ```

### Environment Variables
Create a `.env` file in the root directory of the project and add your Twitter credentials.
USERNAME=your_twitter_username
PASSWORD=your_twitter_password


### Running the Bot
1. Ensure you have Google Chrome installed and the corresponding ChromeDriver in your PATH.
2. Run the bot.
    ```sh
    python bot.py
    ```

## Code Overview
- **bot.py:** The main script that contains the bot logic.
- **requirements.txt:** List of required Python packages.
- **.env:** Environment variables file to store Twitter credentials (not included in the repository for security reasons).

### bot.py
- **random_words:** List of random words.
- **generate_random_comment(base_comment, num_words=5):** Generates a comment with a random selection of words to bypass the Twitter bot security.
- **twitter_login(driver, username, password):** Logs into Twitter with provided credentials.
- **comment_on_latest_tweet(driver, hashtag, comment):** Comments on the latest tweet under the specified hashtag.

## Notes
- Make sure your ChromeDriver version matches your Chrome browser version.
- The bot might need adjustments if Twitter updates its web interface.
- Use this bot responsibly and adhere to Twitter's rules and policies.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
Unlicensed

## Disclaimer
This bot is for educational purposes only. The creator is not responsible for any misuse of this bot.
