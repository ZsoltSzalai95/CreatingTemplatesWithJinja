from flask import Flask, render_template
import datetime
app = Flask(__name__)
import requests


@app.route("/username/<name>")
def home(name):
    gender_url=f"https://api.genderize.io/?name={name}"
    gender= requests.get(gender_url)
    gender_json=gender.json()
    gender_data=gender_json["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    age = requests.get(age_url)
    age_json = age.json()
    age_data = age_json["age"]

    return render_template("index.html", name=name, age=age_data, gender=gender_data)


if __name__== "__main__":
    app.run(debug=True)