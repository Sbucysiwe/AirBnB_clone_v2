#!/usr/bin/python3
""" script that starts Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes: 1- /: display “Hello HBNB!”
            2- /hbnb: display “HBNB”
            3- /c/<text>: display “C ” followed by value of text
                variable (replace underscore _ symbols with a space )
            4- /python/(<text>): display “Python ”, followed by value of...
                the text variable (replace underscore _ symbols with space )
                The default value of text is “is cool”
            5- /number/<n>: display “n is number” only if n is integer
            6- /number_template/<n>: display a HTML page only if n is an...
                ...integer: H1 tag: “Number: n” inside tag BODY
    You must use option strict_slashes=False in your route definition """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ only_hbnb method: """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def only_c(text):
    """ only_c method: route to return C followed by text variable, replaces _
        with spaces """
    text = text.replace('_', ' ')
    return ('C' + ' ' + text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def only_python(text=None):
    """ only_python method: route to return text follow by "is cool"
        (can be overwritten), replaces _ with spaces """
    if text is None:
        text = 'is cool'
    else:
        text = text.replace('_', ' ')
    return ('Python' + ' ' + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    """  number_int method: display “n is number” only if n is an integer """
    return ('{:d} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ num_template method: display HTML page only if n is integer
        route /number_templates with the integer n """
    return (render_template('5-number.html', n=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
