from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
import logging
import os
import csv

logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
# Fuctions

def url_check(url):
    """To check if url is ending with Page="""
    end = '&page='
    if url[-7:-1] != end:
        return url+ end
    url = url[:-1]
    return url 



application = Flask(__name__)


@application.route("/",methods = ['GET'])
def welcome():
    return render_template("welcome.html")


@application.route("/review",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            # To get the query
            url = request.form['content'].replace(" ","")
            url = url_check(url)
            product = url[25:url.find('-')]
            save_directory = "Reveiw/"
            # create the directory if it doesn't exist
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            # To prevent getting blocked
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

            #List of data with header for csv file
            data = [["Name","rating","title","review"]]

            i = 1
            page_available = True

            while page_available:
                print(f"Page {i} processing")
                print(url+str(i))
                responce = requests.get(url+str(i))
                print(responce)
                soup = BeautifulSoup(responce.content)
                # print(soup)
                name_list = soup.find_all(class_ = '_2sc7ZR _2V5EHH')
                rating_list = soup.find_all(class_ = '_3LWZlK _1BLPMq')
                title_list = soup.find_all(class_ = '_2-N8zT')
                review_list = soup.find_all(class_="t-ZTKy") 

                # Check if the page exist or not return data will be empty if page doesn't exists
                if not (len(name_list) or len(rating_list) or len(title_list) or len(review_list)) :
                    print("Page Not Available")
                    page_available = False  
                print("Going to load data")
                # Loading results in the List
                for name,rating,title,review in zip(name_list,rating_list,title_list,review_list):
                    data.append([name.text,rating.text,title.text,review.text])
                i += 1
            # print(data)
            # Loading result into Csv file
            print("Going to write csv")
            with open(f'Reveiw/{product}_review.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(data)
            print("CSV written")
        
            return "Review Loaded"
            
        except Exception as e:
                logging.info(e)
                return 'something is wrong'


    else:
        return render_template('welcome.html')

if __name__ == "__main__" :
    application.run(debug = True)