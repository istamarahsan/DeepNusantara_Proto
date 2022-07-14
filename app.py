from flask import Flask, render_template
from fetch import get_catalogue, get_featured

app = Flask(__name__)

@app.route('/home')
def home():  # put application's code here
    return render_template('home.html', catalogue = get_catalogue(), featured = get_featured())

@app.route('/nav')
def nav():
    return render_template('nav.html')

if __name__ == '__main__':
    app.run()
