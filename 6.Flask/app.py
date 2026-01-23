from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have a 'index.html' file in the 'templates' folder

@app.route("/about")
def about():
    return render_template("about.html")  # Ensure you have an 'about.html' file in the 'templates' folder
if __name__ == "__main__":
    app.run(debug=True)