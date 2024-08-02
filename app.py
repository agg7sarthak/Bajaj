from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.get_json()
        
        if not data or 'data' not in data:
            return jsonify({'is_success': False, 'user_id': 'john_doe_17091999', 'email': 'john@xyz.com', 'roll_number': 'ABCD123', 'numbers': [], 'alphabets': [], 'highest_alphabet': []}), 400

        user_id = 'john_doe_17091999'
        email = 'john@xyz.com'
        roll_number = 'ABCD123'

        numbers = [item for item in data['data'] if item.isdigit()]
        alphabets = [item for item in data['data'] if item.isalpha()]
        highest_alphabet = [max(alphabets)] if alphabets else []

        response = {
            'is_success': True,
            'user_id': user_id,
            'email': email,
            'roll_number': roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_alphabet': highest_alphabet
        }
        return jsonify(response)
    
    elif request.method == 'GET':
        return jsonify({'operation_code': 1})

if __name__ == '__main__':
    app.run(debug=True)
