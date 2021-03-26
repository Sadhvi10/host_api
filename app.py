import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/slots', methods=['GET'])
def locations():
    return "(1,2)(4,3)(7,1)(2,6)"

app.run()

