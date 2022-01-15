from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'answer' in session:
        print('there is an answer')
        return render_template('index.html')
    else:
        session['answer'] = random.randint(1, 100)
        print('made answer', session['answer'], type(session['answer']))
        return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print("guess made", type(session['guess']))
    return redirect('/')

@app.route('/play_again')
def play_again():
    print('guess and answer deleted')
    session.pop('answer')
    session.pop('guess')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug = True)