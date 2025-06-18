from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 

@app.route('/api/message', methods=['POST'])
def api_message():
    data = request.get_json()
    # 在这里处理 data
    return jsonify({
        'status': 'success',
        'data': data
    })
