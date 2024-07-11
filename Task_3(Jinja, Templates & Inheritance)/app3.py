from flask import Flask, render_template
from Employee import Employee_data


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")

@app.route("/Addno/<int:num>")
def Addno(num):
        return render_template('Addno.html',title="Evaluate",
                              number=num)


@app.route("/about")
def about():
    return render_template('about.html',title="About")



@app.route("/Employee")
def Employee():
         return render_template('employee.html',title="Employee",emp=Employee_data)


if __name__ == "__main__":
    app.run(debug=True)