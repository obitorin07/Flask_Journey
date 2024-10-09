from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        input_data = request.form['data_input']
        message = f"You entered: {input_data}. Great data input for analysis!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
