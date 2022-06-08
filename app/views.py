from app import app
from flask import Flask, redirect, url_for, render_template, request, jsonify 
import requests
# import json

@app.route('/')
def home():
   return "hello world! aditia"

@app.route('/mhs-data/all', methods = ['POST', 'GET'])
def dataMshAll():

    endpoint_token = "https://developer.ump.ac.id/token/index.php"
    endpoint_mhs = "https://developer.ump.ac.id/PD/tlm/mahasiswa.php"

    data_token = { "username" : "datatlm", "password" : "tlm@access", "url" : "https://developer.ump.ac.id/PD/tlm/mahasiswa.php"}
    r = requests.post(url = endpoint_token, json = data_token)



    pastebin_url = r.json()
    # parse_token = json.loads(pastebin_url)
    print(pastebin_url)
    key = request.form['key']
    context = {
        'status' : 'sukses',
        'key' : key,
        'address' : pastebin_url 
    }
    return jsonify(context)
