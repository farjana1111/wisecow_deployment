from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Function to get a random fortune and display it with cowsay
def get_cowsay_fortune():
    # Get a random fortune
    fortune = subprocess.check_output("fortune", shell=True).decode('utf-8')
    # Run cowsay with the fortune
    cowsay = subprocess.check_output(f"cowsay {fortune}", shell=True).decode('utf-8')
    return cowsay

# Route for the home page
@app.route('/')
def index():
    wisdom = get_cowsay_fortune()  # Get the fortune and cowsay it
    return render_template('index.html', wisdom=wisdom)  # Render the HTML template with the fortune

# Route for a user page
@app.route('/user')
def user():
    return "This is the user page."

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4499)  # Run the Flask app on port 4499
