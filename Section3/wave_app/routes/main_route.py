from flask import Blueprint, render_template, request
from wave_app.utils import alert_funcs
from wave_app import db
from wave_app.model import Search

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/signin')
def user_index():
    user_id = request.args.get('user_id')
    msg_code = request.args.get('msg_code', None)
    history = [lists._asdict() for lists in db.session.query(Search.date, Search.time, Search.avg, Search.hg, Search.sec).filter(Search.user_id == user_id).all()]

    alert_msg = alert_funcs.msg_processor(msg_code) if msg_code is not None else None

    return render_template('signin.html', alert_msg=alert_msg, history=history, user_id = user_id)

@bp.route('/signin')
def fail_index():
    msg_code = request.args.get('msg_code', None)

    alert_msg = alert_funcs.msg_processor(msg_code) if msg_code is not None else None

    return render_template('signin.html', alert_msg=alert_msg)

@bp.route('/signup')
def signup_index():
    msg_code = request.args.get('msg_code', None)

    alert_msg = alert_funcs.msg_processor(msg_code) if msg_code is not None else None

    return render_template('signup.html', alert_msg=alert_msg)

@bp.route('/predict/')
def predict_index():
    user_id = request.args.get('user_id', None)
    name = request.args.get('name', None)
    level = request.args.get('level', None)
    end_date = request.args.get('end_date', None)
    msg = request.args.get('msg', None)
    prediction_list = []
    if request.args.getlist('prediction'):
        for pred in request.args.getlist('prediction'):
            prediction_list.append(eval(pred))
    
    return render_template('prediction.html', user_id=user_id, name=name, level=level, end_date=end_date, msg=msg, prediction=prediction_list)