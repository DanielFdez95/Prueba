""""import json
import ssl
from flask import Flask, redirect, render_template, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)
app.secret_key = "supersekrit"  # Replace this with your own secret!
blueprint = make_facebook_blueprint(
    client_id="",
    client_secret="",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me")
    print(resp.json())
    return "El servidor responde con {}".format(resp.json())

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
"""""