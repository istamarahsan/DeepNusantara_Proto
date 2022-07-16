from flask import Flask, render_template
from fetch import get_catalogue, get_featured, get_entry

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'home.html',
        catalogue=get_catalogue(),
        featured=get_featured()
    )


@app.route('/pages/the-origin-of-lake-toba')
def lake_toba():
    return render_template(
        'pages/the-origin-of-lake-toba.html',
        catalogue=get_catalogue(),
        page_data=get_entry("page_data/laketoba.json")
    )


if __name__ == '__main__':
    app.run()
