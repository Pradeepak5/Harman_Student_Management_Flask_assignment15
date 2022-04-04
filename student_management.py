from flask import Flask, render_template

student=Flask(__name__)

@student.route("/")
def Login_details():
    return render_template("studentLogin.html")

@student.route("/register")
def Register():
    return render_template("register.html")

@student.route("/search")
def Search():
    return render_template("search.html")

@student.route("/delete")
def Delete():
    return render_template("delete.html")

if __name__=="__main__":
    student.run()

