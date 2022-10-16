from flask import Flask, render_template
import random
from operator import add, mul, pow, sub, truediv
from string import ascii_letters
import string


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()