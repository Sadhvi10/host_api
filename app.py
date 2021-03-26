import flask

app = flask.Flask(_name_)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/slots', methods=['GET'])
def locations():
    return "(1,2)(4,3)(7,1)(2,6)"

# Notice how socketio.run takes care of app instantiation as well.
if __name__ == '__main__':
    app.run()

