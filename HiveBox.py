from flask import Flask

app = Flask(__name__)

app_version = "v0.0.2"

@app.route("/version")
def version():
    return {"version": app_version}

@app.route("/temperature")
def temperature():
    return {"temperature": 27.5}  #i dont  placeholder

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
