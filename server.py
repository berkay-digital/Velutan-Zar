from flask import Flask, request, jsonify

app = Flask(__name__)

roll_number = None

@app.route('/set_roll', methods=['POST'])
def set_roll():
    global roll_number
    roll_number = request.json.get('roll')
    return jsonify({'status': 'success'}), 200

@app.route('/get_roll', methods=['GET'])
def get_roll():
    global roll_number
    if roll_number is None:
        return jsonify({'error': 'No roll number set'}), 404
    else:
        return jsonify({'roll': roll_number}), 200

if __name__ == '__main__':
    app.run(debug=True)