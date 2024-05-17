import os
import random
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# developed by: Vahan DAG
# 18.05.2024 

# Load environment variables from .env file
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

wait_duration = 5 # wait duration for each comment

# The reason for adding these words is to create an additional security layer that 
# reduces the risk of Twitter blocking you. If you wish, you can change these words as you like or,
# if you don't want to add random words, you can keep this list empty [ ].
random_words = [
    "blockchain", "crypto", "web3", "NFT", "decentralized", "ledger", "token", 
    "smart contract", "wallet", "Ethereum", "Bitcoin", "DeFi", "staking", 
    "mining", "hashing", "dApp", "DAO", "Solidity", "consensus", "altcoin", 
    "HODL", "ICO", "metaverse", "airdrops", "gas fees", "public key", "private key", 
    "block", "node", "hash rate", "scalability", "sharding", "cross-chain", "oracle", 
    "governance", "yield farming", "liquidity", "proof of work", "proof of stake", 
    "cryptography", "immutable", "satoshi", "whitepaper", "mainnet", "testnet", 
    "FOMO", "FUD", "whale", "pump", "dump", "rug pull", "DEX", "CEX"
]

# Function to generate a random comment with 3-5 random words from the list
def generate_random_comment(base_comment, num_words=5):
    random_selection = " ".join(random.sample(random_words, num_words))
    if random.random() > 0.5:
        return f"{random_selection} {base_comment}"
    else:
        return f"{base_comment} {random_selection}"

# Function to log in to Twitter
def twitter_login(driver, username, password):
    driver.get("https://twitter.com/login")
    time.sleep(5)
    
    # Locate and fill the username field
    username_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    username_input.send_keys(username)
    
    # Click the 'Next' button
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
    time.sleep(3)
    
    # Locate and fill the password field
    password_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)

# Function to comment on the latest tweet under a specific hashtag
def comment_on_latest_tweet(driver, hashtag, comment):
    driver.get(f"https://x.com/search?q=%23{hashtag}&src=typed_query&f=live")
    time.sleep(5)
    
    last_tweet = None
    
    while True:
        tweets = driver.find_elements(By.XPATH, "//article[@role='article']")
        
        if not tweets:
            time.sleep(5)
            continue
        
        latest_tweet = tweets[0]
        
        if last_tweet is not None and latest_tweet == last_tweet:
            time.sleep(5)
            driver.refresh()
            continue
        
        last_tweet = latest_tweet
        
        # Find the reply button and click it
        reply_button = WebDriverWait(latest_tweet, 10).until(EC.element_to_be_clickable((By.XPATH, ".//button[@data-testid='reply']")))
        reply_button.click()
        time.sleep(2)
        
        # Locate the comment input box and enter the generated comment
        comment_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
        comment_input.send_keys(generate_random_comment(comment))
        
        time.sleep(2)
        
        # Click the tweet button to post the comment
        tweet_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']")))
        tweet_button.click()
        time.sleep(wait_duration)
        
        driver.refresh()
        time.sleep(wait_duration)

if __name__ == "__main__":
    hashtag = "Bitcoin"
    comment = "Running ₿ Bitcoin!"
    
    driver = webdriver.Chrome()
    
    try:
        twitter_login(driver, username, password)
        comment_on_latest_tweet(driver, hashtag, comment)
    finally:
        driver.quit()
