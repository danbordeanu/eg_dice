fpp.run(host='0.0.0.0', port=5000)rom flask import Flask, request, abort, Response
from flask import render_template
import random
from functools import wraps

app = Flask(__name__)


def require_appkey(view_function):

    """
    simple appkey validation
    it will check presence of the header secretkey with value 123
    :param view_function:
    :return:
    """

    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('secretkey') and request.headers.get('secretkey') == '1234':
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function

@app.route('/api/dice', methods=['GET'])
#@require_appkey
def randomfactor():
    """
    this will return a random value from 1 to 6
    :return:
    """
    dice = random.randint(1, 6)
    return render_template('dice.html', what=dice)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
