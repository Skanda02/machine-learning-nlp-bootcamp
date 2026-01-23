from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have a 'index.html' file in the 'templates' folder

@app.route("/about")
def about():
    return render_template("about.html")  # Ensure you have an 'about.html' file in the 'templates' folder

'''@app.route('/form')
def show_form():
    return render_template('forms.html')

@app.route('/submit', methods=['POST'])
def handle_data():
    # 'user_input' matches the 'name' attribute in the HTML input tag
    data = request.form.get('user_input')
    print(f"User sent: {data}") # This shows up in your terminal
    return f"<h1>Success!</h1><p>Flask received: {data}</p><a href='/form'>Try again</a>'''




'''jinja2 taplate engin is used to render html pages dynamically'''
@app.route('/form')
def show_form():
    return render_template('forms.html')

@app.route('/results', methods=['POST'])
def calculate_result():
    # 1. Get the score from the form
    score_str = request.form.get('score')
    
    # 2. Convert string to integer so we can compare it
    try:
        score_int = int(score_str)
    except ValueError:
        return "Please enter a valid number!"

    # 3. Send that integer to the results page
    return render_template('results.html', score=score_int)


if __name__ == "__main__":
    app.run(debug=True)