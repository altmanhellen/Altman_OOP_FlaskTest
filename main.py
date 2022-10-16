from flask import Flask, render_template
import random
from operator import add, mul, pow, sub, truediv
from string import ascii_letters
import string
import csv


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


@app.route('/cities')
def printCities():
    file = open(
        '/Users/helene/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Python/Домашнее задание/Russian_cities.csv',
        'r')
    data = file.read()
    words = data.split('\n')
    length = len(words)
    for i in range(len(words)):
        print(words[i])
    return render_template('cities.html', words=words, length=length)


if __name__ == '__main__':
    app.run()