from app import app

@app.route("/", methods=["GET"])
@app.route("/index")
def index():
    return "My First API using Python3 and Flask"

@app.route("/contact", methods=["GET"])
def contact():
    return "My contact details here"
