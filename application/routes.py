from application import app

@app.route("/")

def index():
    return "<h1> Hello Developers </h1>"