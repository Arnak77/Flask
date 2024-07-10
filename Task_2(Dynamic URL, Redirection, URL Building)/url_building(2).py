from flask import Flask,redirect,url_for

app= Flask (__name__)

@app.route("/")
def home():
    return "<h1>Welcome buddy......</h1"

@app.route("/Score/<name>/<int:num>")
def Score(name,num):
    if num > 35:
        return redirect(url_for("Passed", sname=name, marks=num))
    else:
        return redirect(url_for("Failed" ,sname=name, marks=num))


@app.route("/Passed/<sname>/<int:marks>")
def Passed(sname,marks):
    return f"<h1>Con..{sname}Your Are Pass...with{marks}</h1"

@app.route("/Failed/<sname>/<int:marks>")
def Failed(sname,marks):
    return f"<h1>Sry..{sname}Your Are Fail...with{marks}</h1"



if __name__ == "__main__":
    app.run(debug=True)


