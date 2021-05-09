from flask import Flask, render_template, request, url_for, flash, redirect
import os
from os import path
import sys
import sqlite3
from werkzeug.exceptions import abort
from flask import send_file
from werkzeug.utils import secure_filename
from google.cloud.storage import Blob
import python_scripts.BLAST_new_alignments_parser as parser
import python_scripts.reset as reset


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['UPLOAD_FOLDER'] = "uploads"

def cout(String):
    print(String, file=sys.stderr)

def return_single_parse(filename, contents):
    path = f"/tmp/{filename}.xlsx"
    parser.parse(filename, contents, True, path)
    return send_file_function(path)

def return_batch_parse(filenames, contents):
    path = "/tmp/Batch Parse Results.xlsx"
    parser.parse_batch(filenames, contents, path)
    return send_file_function(path)


def send_file_function(path, as_attachment=True):
    file = send_file(path, as_attachment=as_attachment)
    os.remove(path)
    return file


@app.route('/', methods=("GET", "POST"))
def index():
    reset.reset()

    user = "guest"
    if request.method == 'POST':

        if "file" in request.files:
            file = request.files['file']

            filename = secure_filename(file.filename)
            
            if not filename.endswith(".txt"):
                return "Wrong Format (only .txts)"
            filename = filename[:-4]

            contents = []
            for line in file:
                contents.append(line.decode("utf-8"))

            return return_single_parse(filename, contents)

        else:
            files = request.files.getlist("file[]")
            # file = request.files['file']

            filenames = list(map(lambda x: secure_filename(x.filename), files))
            
            for filename in filenames:
                if not filename.endswith(".txt"):
                    return "Wrong Format (only .txts)"
                filename = filename[:-4]

            contents = []
            for file in files:
                file_contents = []
                for line in file:
                    file_contents.append(line.decode("utf-8"))
                contents.append(file_contents)

            return return_batch_parse(filenames, contents)

    return render_template('basic_new.html', user=user)
