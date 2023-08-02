from flask import Flask,render_template


application = Flask(__name__)


@application.route("/",methods = ['GET'])
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__" :
    application.run(debug = True)