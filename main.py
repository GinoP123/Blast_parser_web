from flask import Flask, render_template, request, url_for, flash, redirect
import os
from os import path
import sys
import sqlite3
from werkzeug.exceptions import abort
from flask import send_file
from werkzeug.utils import secure_filename
from google.cloud.storage import Blob
from python_scripts.BLAST_alignments_parser import *
import python_scripts.reset as reset


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['UPLOAD_FOLDER'] = "uploads"

def cout(String):
    print(String, file=sys.stderr)

def download_return(filename, contents):
    parse(contents, filename)
    return send_file_function(f"/tmp/{filename}.xlsx")


def send_file_function(path, as_attachment=True):
    file = send_file(path, as_attachment=as_attachment)
    os.remove(path)
    return file


@app.route('/', methods=("GET", "POST"))
def index():
    reset.reset()

    user = "guest"
    if request.method == 'POST':

        file = request.files['file']

        filename = secure_filename(file.filename)
        
        if not filename.endswith(".txt"):
            return "Wrong Format (only .txts)"
        filename = filename[:-4]

        contents = []
        for line in file:
            contents.append(line.decode("utf-8"))

        return download_return(filename=filename, contents=contents)

    return render_template('basic_new.html', user=user)
