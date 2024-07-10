from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome to my website"


@app.route("/Welcome/<name>")
def Welcome(name):
    return f"Arigato {name}, saving me..."

@app.route("/Addition/<int:num>")
def Addition(num):
    return f"input is  {num}, output is{num+2} "

@app.route("/Addition_2/<int:num1>/<int:num2>")
def Addition_2(num1,num2):
    return f"input is  {num1}*{num2}, output is{num1*num2} "

@app.route("/about")
def about():
    return "Welcome to my about apge"

if __name__ == "__main__":
    app.run(debug=True)
