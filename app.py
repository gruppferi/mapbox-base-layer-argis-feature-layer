import sys
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))

@app.route('/')
def index():
    if len(sys.argv) < 3:
        print("Usage: python app.py <API_TOKEN> <URL>")
        sys.exit(1)

    token = sys.argv[1]
    url = sys.argv[2]
    return render_template('index.html', token=token, url=url)

if __name__ == '__main__':
    app.run(debug=True)
