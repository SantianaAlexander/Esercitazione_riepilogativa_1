import requests
from flask import Flask, render_template, redirect, url_for, request
def api_request():
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()
    return data.get("people", [])
