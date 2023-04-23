from flask import Blueprint, render_template, request,flash,jsonify,redirect
from flask_login import login_required, current_user
from .models import Note
from . import db 
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category ='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():

    note = json.loads(request.data)
    noteId = note['noteId']
    print(noteId)
    note = Note.query.get(noteId)
    print(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note was deleted.', category='success')
    return jsonify({})

@views.route('/<int:id>/update', methods=['GET','POST'])
@login_required
def update(id):
    
    if request.form.get('home') == 'fromHome':
        return render_template("update.html", user=current_user, id=id)   
    else:
        
        if request.method == 'POST':
            updated_note = request.form.get('note')
            noteId = request.form.get('home')
            print(updated_note)
            print(noteId)

            if len(updated_note) < 1:
                flash('Note is too short!', category='error')
            else:
                note = Note.query.filter_by(id=noteId).first()
                print(note.data)
                note.data = updated_note
                current_time = datetime.datetime.now()
                note.updated_date = current_time.replace(microsecond=0)
                note.have_update = True
                db.session.commit()
                flash('Note updated!', category ='success')
            return redirect('/')
    return render_template("home.html", user=current_user)    
