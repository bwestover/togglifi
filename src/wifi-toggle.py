import os
import requests
from flask import Flask, jsonify, render_template, request
from unificontrol import UnifiClient

app = Flask(__name__, static_url_path='/static', static_folder='static')
wifi_client = UnifiClient(host = os.environ.get('UNIFI_HOST'), password = os.environ.get('UNIFI_PW'))
wlan_id = os.environ.get('UNIFI_WLAN_ID')

@app.route("/")
def wifi_toggle():
    base_url = request.base_url

    res = requests.get(base_url + 'status')

    status = res.json()["wifi_enabled"]

    return render_template('index.html', wifi_enabled=status)


@app.route("/status", methods=['GET'])
def wifi_status():
    status = wifi_client.list_wlanconf(wlan_id)[0]["enabled"]
    return {"wifi_enabled": status}


@app.route("/enable", methods=['GET'])
def wifi_enable():
    wifi_client.enable_wlan(wlan_id, True)
    return '', 204

@app.route("/disable", methods=['GET'])
def wifi_disable():
    wifi_client.enable_wlan(wlan_id, False)
    return '', 204
