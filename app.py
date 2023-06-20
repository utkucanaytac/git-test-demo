import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
    app.run(debug=True)
    app.run(debug=True, host='')

##3bu commiti eklemek istiyorum sadece