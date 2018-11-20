from flask import Flask
from selenium import webdriver
app = Flask(__name__)

 
@app.route("/")
def hello():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    title_text = driver.title
    return title_text
 
if __name__ == "__main__":
    app.run()
