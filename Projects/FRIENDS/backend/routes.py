from models import Friend, db
from flask import Blueprint, request, jsonify

friend_blueprint = Blueprint('friends', __name__)

# Get all the friends
@friend_blueprint.route('/api/friends/', methods = ['GET'])
def get_friends():
    friends = Friend.query.all()
    # Converting to a list of dictionaries
    friends = [friend.to_json() for friend in friends]
    #return the json object along with the status code
    return jsonify(friends), 200

# Create a new friend
@friend_blueprint.route('/api/friends/', methods = ['POST'])
def create_friend():
    data = request.get_json()
    
    missing_fields = []
    required_fields = ['name', 'role', 'description', 'gender']

    for field in required_fields:
        if field not in data:
            missing_fields.append(field)

    if len(missing_fields) > 0:
        return jsonify({"missing_fields" : missing_fields}), 404
    
    if data['gender'] == 'male':
        img_url = f'https://avatar.iran.liara.run/public/boy?username={data['name']}'
    else:
        img_url = f'https://avatar.iran.liara.run/public/girl?username={data['name']}'
    
    try:
        friend = Friend(name = data['name'], role = data['role'], description = data['description'], gender = data['gender'], img_url = img_url )
        
        db.session.add(friend)
        db.session.commit()

        return jsonify({"message" : "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}), 500

# Delete a friend
@friend_blueprint.route('/api/friends/<int:id>', methods = ['DELETE'])
def delete_friend(id):
    friend = Friend.query.get(id)

    if friend is None:
        return jsonify({"error" : "Friend doesn't exist"}), 404
    
    try:
        db.session.delete(friend)
        db.session.commit()

        return jsonify({"message" : "Friend deleted succesfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}), 500
    
#Update a friend
@friend_blueprint.route('/api/friends/<int:id>', methods = ['PUT'])
def update_friend(id):
    friend = Friend.query.get(id)
    if friend is None:
        return jsonify({"error" : "Friend doesn't exist"}), 404
    data = request.get_json()
    if 'name' in data:
        friend.name = data['name']
    if 'role' in data:
        friend.role = data['role']
    if 'description' in data:
        friend.description = data['description']
    if 'gender' in data:
        friend.gender = data['gender']
    try:
        db.session.commit()
        return jsonify({"message" : "Friend updated succesfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}), 500


    