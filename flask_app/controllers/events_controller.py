from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.events import Event

#to upload images
from werkzeug.utils import secure_filename
import os

#NEW EVENT
@app.route("/new/event")
def events():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    return render_template('new_event.html', user=user)

#SUCCESS PAGE
@app.route("/success")
def success():
    if 'user_id' not in session:
        return redirect('/new_event')

    data = {
        "id": session['user_id']
    }
         
    user = User.get_by_id(data)
    #Recent Created Event
    event = Event.get_user_created_event(data)
    return render_template("success.html", user=user, event=event)


#CREATE EVENT FUNCTION
@app.route("/create/event", methods=["POST"])
def create_event():
    if 'user_id' not in session:
        return redirect('/')
    if not Event.validate_event(request.form):
        return redirect("/new/event")
    if 'image' not in request.files:
        flash('Not image selected', 'event')
        return redirect('new/event')
    
    image = request.files['image']
    print("paso")
    if image.filename == '':
        flash('empty name for image', 'event')
        return redirect("new/event")
    
    name_image = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], name_image))
    
    data={
        "title" :request.form["title"],
        "description" : request.form["description"],
        "host" : request.form["host"],
        "location": request.form["location"],
        "cost" : request.form["cost"],
        "date" : request.form["date"],
        "time" : request.form["time"],
        "registration": request.form["registration"],
        "image" : name_image,
        "user_id" : request.form["user_id"],
        "tags" : request.form["tags"]
    }
    print(data)
    Event.save(data)
    return redirect("/success")