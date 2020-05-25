from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    pokemon = "blastatoise"
    letters = list(pokemon)
    dict = {'water':'bulba', 'fire':'charmandar'}
    return render_template('basics.html',name=pokemon,letters=letters,dict=dict)

if __name__ == '__main__':
    app.run(debug=True)
