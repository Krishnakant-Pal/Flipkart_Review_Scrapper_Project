from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
import os
import csv

application = Flask(__name__)


@application.route("/",methods = ['GET'])
def welcome():
    return render_template("welcome.html")


@application.route("/review",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            # To get the query
            query = request.form['content'].replace(" ","")
            
            save_directory = "Reveiw/"
            # create the directory if it doesn't exist
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)


            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}








            return "Review Loaded"
        except Exception as e:
                logging.info(e)
                return 'something is wrong'


    else:
        return render_template('index.html')

if __name__ == "__main__" :
    application.run(debug = True)