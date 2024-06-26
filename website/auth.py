from flask import Blueprint, render_template,request

auth = Blueprint('auth',__name__) #defined a blueprint

@auth.route('/appointment', methods=['GET','POST'])
def appoint():
    return  render_template("Appointment.html")

@auth.route('/1st-dose', methods=['GET','POST'])
def appoint1():
    return  render_template("Appointment1.html")

@auth.route('/2nd-dose', methods=['GET','POST'])
def dose2():
    return  render_template("Appointment2.html")

@auth.route('/booster', methods=['GET','POST'])
def booster():
    return  render_template("Booster.html")

@auth.route('/how-to-get-vaccinated')
def info():
    return  render_template("about.html")

@auth.route('/survey1', methods=['GET','POST'])
def survey():
    return  render_template("Survey 1.html")

@auth.route('/survey2', methods=['GET','POST'])
def survey2():
    return  render_template("survey2.html")

@auth.route('/survey3', methods=['GET','POST'])
def survey3():
    return  render_template("survey3.html")

@auth.route('/PS1', methods=['GET','POST'])
def ps1():
    return  render_template("PS1.html")

