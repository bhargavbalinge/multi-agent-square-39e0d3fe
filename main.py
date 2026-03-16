from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number = data.get('number')

    if number is None:
        return jsonify({'error': 'No number provided'}), 400

    try:
        number = float(number)
        result = number ** 2
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Please enter a number.'}), 400

if __name__ == '__main__':
    app.run(debug=True)