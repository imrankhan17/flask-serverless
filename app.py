from flask import Flask, request, render_template, redirect, url_for

from form import CoefficientsForm
from utils import calculate_roots, save_to_db

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'


@app.route('/', methods=['GET', 'POST'])
def calculate():
    form = CoefficientsForm()
    if form.validate_on_submit():
        return redirect(url_for('result', a=form.data['a'], b=form.data['b'], c=form.data['c']))
    return render_template('form.html', form=form)


@app.route('/result')
def result():
    save_to_db(request=request)
    return calculate_roots(a=request.args['a'], b=request.args['b'], c=request.args['c'])


if __name__ == '__main__':
    app.run()
