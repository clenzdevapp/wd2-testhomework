import hashlib
import uuid

from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all()  # create new tables in database


@app.route("/")  # CONTROLLER
def index():
    session_token = request.cookies.get("session_token")

    if session_token:
        # get user from the database based on email address
        user = db.query(User).filter_by(session_token=session_token).first()
        

    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/index", methods=["GET", "POST"])
def form_signin():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        user_name = request.form.get("email")

        user_password = request.form.get("password")

    session_token="1234"
    user = User(user_name=user_name, user_password=user_password, session_token=session_token)
    # save user into database
    db.add(user)
    db.commit()

   

    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True)
    
    
