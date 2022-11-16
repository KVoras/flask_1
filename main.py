"""
-API (Application Program Interface)
-parsing dictionaries in jinja
-simple app
    -bootstrap
    -home page
    -clients page
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/clients')
def show_clients():
    clients = [
        {'id': 1, 'name': 'Company Name1'},
        {'id': 2, 'name': 'Company Name2'},
        {'id': 3, 'name': 'Company Name3'},
        {'id': 4, 'name': 'Company Name4'},
        {'id': 5, 'name': 'Company Name5'},
    ]
    return render_template('clients.html', data=clients)

if __name__ == '__main__':
    app.run(debug=True)

app.run()