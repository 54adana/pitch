from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from .forms import PitchForm

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

@main.route('/new_pitch', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
      pitch = Pitch(title = form.title.data, category =form.category.data, content = form.content.data, author = form.author.data,upvote = 0,downvote = 0,user_id=current_user.id)
      pitch.save_pitch()
    return render_template('new_pitch.html',form=form)

@main.route('/comments/<int:pitch_id>/comment',methods=['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentsForm()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    user = current_user.username
    if form.validate_on_submit():
        comment = Comment(content = form.comment.data,user_id = current_user.id,pitch_id = pitch.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.comment',pitch_id=pitch_id))
    return render_template('comments.html', form = form,pitch=pitch,pitch_id=pitch_id,user=user)


@main.route('/view', methods = ['GET','POST'])
def view():
    return render_template('view.html')