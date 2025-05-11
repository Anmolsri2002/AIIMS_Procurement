from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

def start_flask():
    print("Starting Flask server...")
    app.run(debug=False)
