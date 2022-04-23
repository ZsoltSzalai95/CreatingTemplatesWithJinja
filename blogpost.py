from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_json = response.json()
    return render_template("blog.html", blog=blog_json)


if __name__== "__main__":
    app.run(debug=True)