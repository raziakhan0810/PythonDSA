
from flask import Flask, request, jsonify
app = Flask(__name__)

"""
Q1) 
lst = [{id:1, name: ”Alex”, message: “hello world”},
{id:2, name: ”Amin”, message: “Great weather”}]
Write function that returns the array of objects that contains messages that user follows:
[{id:1, name:”Alex”, story: [{id:2, name: ”Amin”, messages: [“Great weather” ]}]

"""
def get_followed_stories(user_id, users, follow_relations):
    following_ids = [relation['followId'] for relation in follow_relations if relation['id'] == user_id]

    result = []

    for user in users:
        if user['id'] == user_id:
            user_story = {
                "id": user['id'],
                "name": user['name'],
                "story": []
            }
            for follow_id in following_ids:
                for followed_user in users:
                    if followed_user['id'] == follow_id:
                        user_story['story'].append({
                            "id": followed_user['id'],
                            "name": followed_user['name'],
                            "messages": [followed_user['message']]
                        })
            result.append(user_story)
            break
    return result

users = [
    {"id": 1, "name": "Alex", "message": "hello world"},
    {"id": 2, "name": "Amin", "message": "Great weather"}
]

follow_relations = [
    {"id": 1, "followId": 2}
]

output = get_followed_stories(1, users, follow_relations)
print(output)


"""
Q2)
Design application API that supports the endpoints:  
a Post, Delete, Edit Post
b View timeline (other posts of people that I follow)
c Search (key word)
"""

users = [
    {"id": 1, "name": "Alex", "message": "hello world"},
    {"id": 2, "name": "Amin", "message": "Great weather"}
]

follow_relations = [
    {"id": 1, "followId": 2}
]

posts = []

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = {
        "id": len(posts) + 1,
        "name": data["name"],
        "message": data["message"]
    }
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post["id"] != post_id]
    return jsonify({"message": "Post deleted successfully"}), 200

@app.route('/posts/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    data = request.get_json()
    for post in posts:
        if post["id"] == post_id:
            post["message"] = data["message"]
            return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/timeline/<int:user_id>', methods=['GET'])
def get_timeline(user_id):
    following_ids = [relation['followId'] for relation in follow_relations if relation['id'] == user_id]
    timeline = []
    for user in users:
        if user['id'] in following_ids:
            user_story = {
                "id": user['id'],
                "name": user['name'],
                "story": []
            }
            for follow_id in following_ids:
                if user['id'] == follow_id:
                    user_story['story'].append({
                        "id": follow_id,
                        "name": users[follow_id - 1]['name'],
                        "messages": [users[follow_id - 1]['message']]
                    })
            timeline.append(user_story)
    return jsonify(timeline), 200

@app.route('/search', methods=['GET'])
def search_posts():
    query = request.args.get('query')
    result = [post for post in posts if query.lower() in post["message"].lower()]
    return jsonify(result), 200


