import os
from flask import Flask, jsonify, render_template, request
from unificontrol import UnifiClient

app = Flask(__name__, static_url_path='/static', static_folder='static')
wifi_client = UnifiClient(host = os.environ.get('UNIFI_HOST'), password = os.environ.get('UNIFI_PW'))
managed_networks = [name.strip() for name in os.environ.get('MANAGED_NETWORK_IDS').split(',')]

@app.route("/")
def wifi_toggle():
    return render_template('index.html', wlans=_wlan_status())

@app.route("/status", methods=['GET'])
@app.route("/status/<wifi_name>", methods=['GET'])
def wifi_status(wifi_name = None):
    return _wlan_status(wifi_name)

@app.route("/enable/<wifi_name>", methods=['GET'])
def wifi_enable(wifi_name):
    wlan_id = _network_id(wifi_name)
    if wlan_id:
      # ToDo: take out this debug line
      print(f"Debug: Would call enable_wlan on ID: {wlan_id}")
      #wifi_client.enable_wlan(wlan_id, True)
    else:
      return f"Error: wifi_name ({wifi_name}) not found\n", 404
    return '', 204

@app.route("/disable/<wifi_name>", methods=['GET'])
def wifi_disable(wifi_name):
    wlan_id = _network_id(wifi_name)
    if wlan_id:
      # ToDo: take out this debug line
      print(f"Debug: Would call enable_wlan(False) on ID: {wlan_id}")
      #wifi_client.enable_wlan(wlan_id, False)
    else:
      return f"Error: wifi_name ({wifi_name}) not found\n", 404
    return '', 204

def _wlan_status(wifi_name = None):
    wlans = [{'id': net['_id'], 'enabled': net['enabled'], 'name': net['name']} for net in wifi_client.list_wlanconf() if net['name'] in managed_networks]
    return [row for row in wlans if row['name'] == wifi_name] if wifi_name else wlans

def _network_id(wifi_name):
    status = _wlan_status(wifi_name)
    return status[0]['id'] if status else None

def _wifi_enabled(wifi_name):
    status = _wlan_status(wifi_name)
    return status[0]['enabled'] if status else None
