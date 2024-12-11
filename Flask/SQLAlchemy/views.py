from models import db
from flask import Blueprint, request, render_template, jsonify
from models import User

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def get_and_create_users():
    if request.method == 'GET':
        users = User.query.all()
        return render_template('home.html', users = users)
    
    elif request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        user = User(name = name, age = int(age))

        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        return render_template('home.html', users = users)
        

@views.route('/delete/<pid>', methods = ['DELETE'])
def delete(pid):
    user = User.query.get(pid)
    if not user:
        return jsonify({
            "error" : "User not found"
        })
    db.session.delete(user)
    db.session.commit()
    users = User.query.all()
    return render_template('home.html', users = users)


@views.route('/details/<pid>', methods = ['GET'])
def details(pid):
    user = User.query.get(pid)
    if not user:
        return jsonify({
            "error" : "User not found"
        })
    return render_template('details.html', user = user)

@views.route('/update/<int:pid>', methods = ['GET', 'PUT'])
def update(pid):
    if request.method == 'PUT':
        user = User.query.get(pid)
        if not user:
            return jsonify({
                "error" : "User not found"
            })
        data = request.get_json()
        name = data.get('name', user.name)
        age = data.get('age', user.age)

        if name is not '':
            user.name = name

        if age is not '':
            user.age = age

        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    elif request.method == 'GET':
        user = User.query.get(pid)
        return render_template('update.html', user = user)




