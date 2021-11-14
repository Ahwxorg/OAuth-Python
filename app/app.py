from flask import Flask, request, redirect
from oauth import OAuth

app = Flask(__name__)

@app.route("/", methods = ["get"])
def index():
    return redirect(OAuth.discord_login_url)

@app.route("/login", methods = ["get"])
def login():
    return OAuth.get_user(request.args.get("code")).get("id")

if __name__ == "__main__":
    app.run(debug=True)
