from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import *

from .. import db,photos
from flask_login import login_required,current_user

#display categories on the landing page
@main.route('/')
def index():
    """ View root page function that returns index page """
    

    title = 'Home- Welcome'
    return render_template('index.html', title = title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))