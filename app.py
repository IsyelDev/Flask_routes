from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the main page!"

@app.route("/home")
def home():
    return "Hello, this is the main page."

@app.route("/about")
def about():
    return "Hello, this is the about page."

if __name__ == "__main__":
    app.run(debug=True)
