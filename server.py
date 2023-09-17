from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'Life is lighter than a feather, death heavier than a mountain.'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processing():
    session['name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result', methods=['GET', 'POST'])
def results():
    print(request.form)
    return render_template('results.html')
    




if __name__ == "__main__":
    app.run(debug=True, port=5001)