#from crypt import methods
from flask import Flask, render_template, request
import sa1

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    if request.method == "POST":
        my_text = request.form["my-text"]
        my_sentiment=sa1.sa1_predict(my_text)
        print(my_sentiment[1])
        return render_template("index.html",the_text=my_sentiment[0],the_result=my_sentiment[1])
    return render_template("index.html")
    
"""
@app.route("/sub",methods=['POST'])
def submit():
    if request.method == "POST":
        my_text = request.form["my-text"]
    return render_template("sub.html",text=my_text)
"""

if __name__=="__main__":
    app.run(debug=True)