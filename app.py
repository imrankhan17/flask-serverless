from flask import Flask, request

app = Flask(__name__)


def calculate_roots(a, b, c):
    a, b, c = map(float, (a, b, c))

    if a == 0:
        return str(-c / b)

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return 'No real roots'

    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    if x1 == x2:
        return str(x1)

    return '{},{}'.format(x1, x2)


@app.route('/')
def quadratic():
    return calculate_roots(a=request.args['a'], b=request.args['b'], c=request.args['c'])


if __name__ == '__main__':
    app.run(debug=True)
