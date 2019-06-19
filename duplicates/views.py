# coding: utf-8
from flask import Flask, render_template, url_for, abort, send_from_directory, request, redirect

import os
import pandas as pd
import json
from duplicates import app

with open("duplicates/master.json", 'r') as f:
    master = json.load(f)

with open("duplicates/paths.json", 'r') as f:
    paths = json.load(f)

with open("duplicates/processed.json", 'r') as f:
    seen = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:ref>/', methods=["GET", "POST"])
def start(ref):
    i = int(ref)

    if request.method == "POST":
        for guid in list(request.form.keys()):
            seen.append(guid)
        with open("duplicates/processed.json", 'w') as f:
            json.dump(seen, f)

        return redirect(url_for("start", ref = ref+1))

    master_keys = list(master.keys())
    guid = master_keys[i]
    others = master[guid]

    return render_template('label.html', ref=ref, guid=guid, others=others, 
        max_len=len(master_keys)-1, seen=seen)


@app.route('/get_file/<guid>')
def download_file(guid):
    base_path = os.path.dirname(paths[guid])
    filename = os.path.basename(paths[guid])

    return send_from_directory(base_path, filename, as_attachment=False)