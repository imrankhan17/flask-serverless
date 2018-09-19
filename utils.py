import os
import pymysql.cursors


def calculate_roots(a, b, c):
    """
    Calculates roots of quadratic equation of form `ax^2 +bx + c = 0`
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant
    :return: roots if they exist
    """
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


def save_to_db(request):
    db = pymysql.connect(host=os.environ['DB_NAME'], user=os.environ['DB_USER'],
                         passwd=os.environ['DB_PASS'], port=3306)
    cur = db.cursor()
    cur.execute('INSERT INTO logs.quadratic (cookie, referrer, user_agent, a, b, c) VALUES (%s, %s, %s, %s, %s, %s);',
                (request.cookies['session'], request.referrer, request.user_agent.string, request.args['a'],
                 request.args['b'], request.args['c']))
    db.commit()
    db.close()
