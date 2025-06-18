from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


groups = []
students = []

@app.route('/api/groups', methods=['GET'])
def get_groups():
    """
    Route to get all groups
    return: Array of group objects
    """

    return jsonify(groups)


@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Route to get all students
    return: Array of student objects
    """
    # TODO: (sample response below)
    return jsonify(students)

@app.route('/api/groups', methods=['POST'])
def create_group():
    """
    Route to add a new group
    param groupName: The name of the group (from request body)
    param members: Array of member names (from request body)
    return: The created group object
    """
    
    # Getting the request body (DO NOT MODIFY)
    group_data = request.json
    group_name = group_data.get("groupName")
    group_members = group_data.get("members")
    
    # TODO: implement storage of a new group and return their info (sample response below)
    if not group_name or not isinstance(group_members, list):
        abort(400, "Invalid group data")
    
    if len(set(group_members)) != len(group_members):
        abort(400, "Duplicate members are not allowed")

    new_members = []
    for member in group_members:

        existing_student = next((s for s in students if s['name'] == member), None)
        if existing_student is None:
            new_student = {"id" : len(students) + 1, "name": member}
            students.append(new_student)
            new_members.append(new_student)
        else:
            new_members.append(existing_student)

    new_group = {
        "id" : len(groups) + 1,
        "groupName": group_name,
        "members": new_members
    }

    groups.append(new_group)

    return jsonify(new_group), 201

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """
    Route to delete a group by ID
    param group_id: The ID of the group to delete
    return: Empty response with status code 204
    """
    global groups

    group_exists = any(g['id'] == group_id for g in groups)

    if not group_exists:
        abort(404, "Group not found")

    groups = [group for group in groups if group["id"] != group_id]

    return '', 204  # Return 204 (do not modify this line)

@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    """
    Route to get a group by ID (for fetching group members)
    param group_id: The ID of the group to retrieve
    return: The group object with member details
    """
    # 查找指定 ID 的组
    group = next((g for g in groups if g['id'] == group_id), None)
    if not group:
        abort(404, "Group not found")

# 根据组中存的成员 ID 列表，构造成员详情
    group_members = [
        {"id": s["id"], "name": s["name"]}
        for s in students
        if s["id"] in group["members"]
    ]

# 返回带成员详情的组对象
    return jsonify({
        "id": group["id"],
        "groupName": group["groupName"],
        "members": group_members
    })



if __name__ == '__main__':
    app.run(port=3902, debug=True)
