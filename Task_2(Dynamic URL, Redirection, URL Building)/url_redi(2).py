from flask import Flask,redirect,url_for

app= Flask (__name__)

@app.route("/")
def home():
    return "<h1>Welcome buddy......</h1"

@app.route("/Score/<name>/<int:num>")
def Score(name,num):
    if num > 35:
        return redirect(url_for("Passed"))
    else:
        return redirect(url_for("Failed"))


@app.route("/Passed")
def Passed():
    return "<h1>Con..Your Are Pass...</h1"

@app.route("/Failed")
def Failed():
    return "<h1>Sry..Your Are Fail...</h1"



if __name__ == "__main__":
    app.run(debug=True)


