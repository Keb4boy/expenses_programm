from financialprogramm.db import insert_all, insert_categories, insert_names, select_finance
from flask import Flask 
from flask import request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def values():
    if request.method == 'POST':
        f = request.form.to_dict()
        data = (f[date], f[categories], f[name], f[amount])
    return template('home.html')


@app.route('/categories', methods=['POST', 'GET'])
def categories():
    return template('categories.html')


@app.route('/amount', methods=['POST', 'GET'])
def amount():
    return template('amount.html')


if __name__ == '__main__':
    app()