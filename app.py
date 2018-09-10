from flask import Flask, request, render_template, redirect

from form import CoefficientsForm
from utils import calculate_roots

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'


@app.route('/', methods=['GET', 'POST'])
def calculate():
    form = CoefficientsForm()
    if form.validate_on_submit():
        return redirect('/result?a={}&b={}&c={}'.format(form.a.data, form.b.data, form.c.data))
    return render_template('calculation.html', form=form)


@app.route('/result')
def result():
    return calculate_roots(a=request.args['a'], b=request.args['b'], c=request.args['c'])


if __name__ == '__main__':
    app.run(debug=True)
