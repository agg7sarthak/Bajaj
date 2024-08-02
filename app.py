from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        data = request.get_json()
        
        # Ensure data contains required fields
        if not data or 'user_id' not in data or 'college_email' not in data or 'college_roll' not in data:
            return jsonify({'Status': 'Error', 'Message': 'Invalid input'}), 400

        response = {
            'Status': 'Success',
            'User ID': data.get('user_id'),
            'College Email ID': data.get('college_email'),
            'College Roll Number': data.get('college_roll'),
            'Array for numbers': [random.randint(1, 100) for _ in range(10)],
            'Array for alphabets': [random.choice(string.ascii_letters) for _ in range(10)]
        }
        return jsonify(response)
    
    elif request.method == 'GET':
        operation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return jsonify({'operation_code': operation_code})

if __name__ == '__main__':
    app.run(debug=True)
