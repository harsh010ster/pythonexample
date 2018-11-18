from flask import Flask

app=Flask(__name__)

@app.route("/")
def main():
    return "welcome to my flask page!!"

@app.route("/about")
def about():
    return "welcome to my about route!!"

#to run app on port 80, else it runs on port 5000
if __name__== "__main__" or __name__=="__about__":
    app.run(debug=True, host="0.0.0.0", port=80)

# to run open terminal , move to the folder that contains the file and run python app.py