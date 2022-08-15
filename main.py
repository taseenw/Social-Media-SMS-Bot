# Author: Taseen Waseq
# Date Created: 2022-08-15
# This program will use Selenium to scrape the users social media data, and text it back to them using Twilio API

from twilio.rest import Client
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Function sending the text message using twilio library function, and twilio credentials
def text(msg):
    account_sid = "ENTER YOUR ACCOUNT SID HERE"
    auth_token = "ENTER YOUR AUTH TOKEN HERE"
    client = Client(account_sid, auth_token)

    client.messages \
                        .create(
                            body = msg,
                            from_ = '+YOUR TWILIO PHONE NUMBER',
                            to = '+YOUR VERIFIED PHONE NUMBER',
                        )

#Function constructing the message
def constructMessage():
    youtubeSection = ""
    instagramSection = ""
    twitterSection = ""

    #Copy paste your path to chromedriver.exe, and desired youtube, instagram and twitter information
    path = "C:\\Users\\tasee\\Desktop\\chromedriver.exe"
    youtubeURL = "https://www.youtube.com/channel/UC4Oalqat4VhD-zmGAA5uvfA"
    instagramURL = "https://instablogs.net/live-instagram-followers-count/"
    instagramHandle = "taseenw"
    twitterURL = "https://twitter.com/taseenaw"
    twitterHandle = "taseenaw"

    driver = webdriver.Chrome(executable_path=path)

    #YouTube
    driver.get(youtubeURL)
    subCount = driver.find_element(By.ID, "subscriber-count").text
    subCount = subCount.split()[0]
    videoTitles = driver.find_elements(By.ID, "video-title")
    videoViews = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

    #Three most recent uploads
    for x in range (3):
        titleSplit = videoTitles[x].text.split()
        titleToSend = titleSplit[0] + " " + titleSplit[1] + "..."
        youtubeSection = youtubeSection + titleToSend + " / " + videoViews[x].text + "\n"

    youtubeSection = "\nYouTube Subscriber Count: " + subCount + "\n" + youtubeSection

    #Instagram follower count site; inputting username and submitting
    driver.get(instagramURL)
    usernameEntry = driver.find_element(By.ID, 'search-username')
    usernameEntry.send_keys(instagramHandle)
    usernameEntry.send_keys(Keys.RETURN)
    time.sleep(5)
    instagramFollowers = driver.find_element(By.ID, 'follower-count')
    instagramSection = "Instagram Followers: " + instagramFollowers.text

    #Twitter
    driver.get(twitterURL)
    time.sleep(5)
    twitterFollowers = driver.find_element(By.CSS_SELECTOR, 'a[href="/'+ twitterHandle +'/followers"] > span > span')
    twitterSection = "Twitter Followers: " + twitterFollowers.text

    #Return
    message = "------------\n" + str(date.today()) + "\n" + youtubeSection + "\n" + instagramSection + "\n\n" + twitterSection
    return message

def main():
    message = constructMessage()
    print(message)
    text(message)

if __name__ == "__main__":
    main()
