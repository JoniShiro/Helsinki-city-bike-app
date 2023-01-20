from flask import Blueprint, render_template
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/')
def home():
    data = pd.read_csv('https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv')
    return render_template("home.html", text = data['Return station name'][1])