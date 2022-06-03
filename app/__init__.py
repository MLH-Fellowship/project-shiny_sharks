import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/home')
def home():
    return render_template('home.html', title="Home Page", url=os.getenv("URL"))
 















# I added the extra lines to prevent merge conflicts :)
map_link = ""
map_link = "https://www.google.com/maps/d/u/0/embed?mid=1XH7YSZNH1D0C2EyBt-MWoSai8VBj-zg&ehbc=2E312F"
@app.route('/map_page')
def map():
    return render_template('map_page.html', title="Map", map_url = map_link, url=os.getenv("URL"))