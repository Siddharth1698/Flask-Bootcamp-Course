from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello</h1>'

@app.route('/information')
def info():
    return '<h1>hello this is an info page</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1> this is {} profile page</h1>".format(name.upper())

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        name = name[:-1]
        name = name + "iful"
        return "<h1> this is {} profile page</h1>".format(name.upper())

        # removing y from lasy character and appending it with iful.

    else:
        name = name + 'y'
        return "<h1> this is {} profile page</h1>".format(name.upper())

        # adding y to end character.



if __name__ == '__main__':
    app.run(debug=True)
