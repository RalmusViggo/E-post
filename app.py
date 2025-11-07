from flask import Flask, render_template, url_for, request, redirect
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ᚺᛖᛗᛗᛖᛚᛁᚷ"

class LoginSkjema(FlaskForm):
    brukernavn = StringField("Brukernavn")
    passord = PasswordField("Passord")
    epost = StringField("E-Post")
    submit = SubmitField("Logg inn")

@app.route("/", methods=["GET", "POST"])
def index():
    login_skjema = LoginSkjema()
    
    if request.method == "POST":
        brukernavn = login_skjema.brukernavn.data
        passord = login_skjema.passord.data
        epost = login_skjema.epost.data
        
        return redirect(url_for("velkommen", brukernavn=brukernavn, epost=epost))
    
    
    
    return render_template("index.html", login_skjema=login_skjema)

@app.route("/velkommen/<brukernavn>/<epost>")
def velkommen(brukernavn, epost):
    return render_template("velkomstside.html", brukernavn=brukernavn, epost=epost)

if __name__== "__main__":
    app.run()