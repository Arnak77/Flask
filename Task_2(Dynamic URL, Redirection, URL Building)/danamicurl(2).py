from flask import Flask

app= Flask (__name__)

@app.route("/")
def home():
    return "<h1>Welcome buddy......</h1"

@app.route("/Welcome/<name>")
def Welcome(name):
    return f"<h1>Welcome {name}, buddy......</h1"



if __name__ == "__main__":
    app.run(debug=True)



