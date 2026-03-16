from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None
    number = ''
    if request.method == 'POST':
        number = request.form.get('number')
        if number:
            try:
                number_int = int(number)
                result = number_int * number_int
            except ValueError:
                error = "Invalid input. Please enter a number."
        else:
            error = "Invalid input. Please enter a number."

    return render_template('index.html', result=result, number=number, error=error)

if __name__ == '__main__':
    app.run(debug=True)