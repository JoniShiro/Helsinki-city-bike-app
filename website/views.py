from flask import Blueprint, render_template
import pandas as pd
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    # data = pd.read_csv(
    #     'https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv')
    # text = data['Return station name'][1]
    return render_template("home.html", user=current_user)
