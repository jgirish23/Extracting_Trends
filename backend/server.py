from flask import Flask, jsonify
import pathlib
import json
from Tweet_extractor import start_extracting_tweets
from Tweet_extractor import scrape_data
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

Electronics_json_PATH = pathlib.Path("./scrapped_data/Electronics.json")
Phone_json_PATH = pathlib.Path("./scrapped_data/Phones.json")
Shoes_json_PATH = pathlib.Path("./scrapped_data/Shoes.json")
Fashion_json_PATH = pathlib.Path("./scrapped_data/Fashion.json")
Electronics_content = json.load(open(Electronics_json_PATH, "r"))
Phones_content = json.load(open(Phone_json_PATH, "r"))
Shoes_content = json.load(open(Shoes_json_PATH, "r"))
Fashion_content = json.load(open(Fashion_json_PATH, "r"))
Home_content = []


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


def return_by_category(jsonC, cat):
    temp = []
    for i in jsonC:
        # if i["Category"] == cat:
        temp.append(i)
    return temp


@app.route("/phones")
def phones():
    # print(type(Phones_content))
    return jsonify(return_by_category(Phones_content, "Phones"))


@app.route("/electronics")
def electronics():
    # print(return_by_category(Electronics_content, "Electronics"))
    return jsonify(return_by_category(Electronics_content, "Electronics"))


@app.route("/fashion")
def fashion():
    dat = return_by_category(Fashion_content, "Fashion")
    dat.extend(return_by_category(Shoes_content, "Shoes"))
    return jsonify(dat)


@app.route("/home")
def home():
    Home_content.clear()
    dat = return_by_category(Fashion_content, "Home")
    for i in range(0, len(dat)):
        if i > 2:
            break
        Home_content.append(dat[i])
    dat = return_by_category(Electronics_content, "Home")
    for i in range(0, len(dat)):
        if i > 2:
            break
        Home_content.append(dat[i])
    dat = return_by_category(Phones_content, "Home")
    for i in range(0, len(dat)):
        if i > 2:
            break
        Home_content.append(dat[i])
    return jsonify(scrape_data.sort_list((Home_content), "Trend_score"))


def start():
    print_date_time()
    print("Backend has Started!")
    # start_extracting_tweets.starting_file()


if __name__ == "__main__":
    # Restarts the extracting process for new tweets in 10 days interval
    scheduler = BackgroundScheduler()
    start()
    scheduler.add_job(func=start, trigger="interval", seconds=10 * 12 * 360)
    app.run(debug=True)
