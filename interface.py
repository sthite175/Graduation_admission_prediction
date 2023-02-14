from flask import Flask,render_template,request,jsonify
from utilities import predict_admission
import pickle
import config

app=Flask(__name__)
@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction", methods=["post"])
def get_admission():
    data=request.form
    admission=predict_admission(data)

    #return jsonify({"Result":admission})
    return render_template("index.html", Result=admission)

if __name__=="__main__":
    app.run(debug=True,port=config.PORT,host=config.HOST)

    