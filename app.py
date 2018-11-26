# Script to load whatsapp web and load the page using selenium and Flask
import os, time
from flask import Flask, send_file
from selenium import webdriver
app = Flask(__name__)

 
@app.route("/")
def hello():
    # Load chrome driver
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)
    # Save the screenshot and load the image
    screenshot_name = os.path.abspath(os.path.join(os.path.dirname(__file__),'screenshot.gif'))
    driver.save_screenshot(screenshot_name)
    return send_file('screenshot.gif', mimetype='image/gif')
 
if __name__ == "__main__":
    app.run()
