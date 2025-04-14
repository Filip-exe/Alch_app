from flask import Flask, render_template, request, redirect, session
import sqlite3
from flask_session import Session
from cs50 import SQL

def on_start():
    if True:
        pass
    else:
        db.execute("DELETE FROM vlastnictvo;")
        db.execute("INSERT INTO vlastnictvo DEFAULT VALUES;")


def novy_den_change_vlastnictvo(increment: int, suroviny: list):
    for surovina in suroviny:
        pocet = (db.execute("SELECT " + surovina + " FROM vlastnictvo WHERE username = '" + session["name"] + "';"))[0][surovina] + increment
        db.execute("UPDATE vlastnictvo SET " + surovina + " = " + str(pocet) + " WHERE username = '" + session["name"] + "';")

def uvar(suroviny):
    for surovina in suroviny:
        if (db.execute("SELECT " + surovina + " FROM vlastnictvo WHERE username = '" + session["name"] + "';"))[0][surovina] <= 0:
            return False
    novy_den_change_vlastnictvo(-1, suroviny)
    return True

def get_vlastnictvo():
    vlastnictvoDict = db.execute("SELECT * FROM vlastnictvo WHERE username = '" + session["name"] + "';")[0]
    keys =(vlastnictvoDict.keys())
    return vlastnictvoDict, keys

def get_nove_elixiry():
    return db.execute("SELECT * FROM elixiry WHERE den = " + str(get_den()) +";")

def get_zname_elixiry():
    return db.execute("SELECT * FROM elixiry WHERE den <= " + str(get_den()) +";")

def get_namiesane_elixiry():
    return db.execute("SELECT * from namiesaneElixiry WHERE username = '" + session["name"] + "';")[0]

def get_den():
    return db.execute("SELECT den FROM vlastnictvo WHERE username = '" + session["name"] + "';")[0]["den"]

def increment_den(den):
    db.execute("UPDATE vlastnictvo SET den = " + str(den+1) + " WHERE username = '" + session["name"] + "';")

def skontroluj(data):
    magistro = data.get("magistro"); common = data.get("common"); elixir = data.get("vyberElixiru")
    priznakyElixiru = db.execute("SELECT priznaky FROM elixiry WHERE elixir = '" + elixir + "';")[0]["priznaky"]
    priznakySurovin = db.execute( "SELECT " + magistro + " FROM kombinaciePriznakov WHERE Surovina = '" + common + "';")[0][magistro]
    if priznakySurovin == priznakyElixiru: return True
    else: return False

def del_data(username):
    db.execute("DELETE FROM vlastnictvo WHERE username = '" + username + "';")    
    db.execute("DELETE FROM namiesaneElixiry WHERE username = '" + username + "';")

def set_data(username):
    db.execute("INSERT INTO vlastnictvo (username) VALUES ('" + username + "');")
    db.execute("INSERT INTO namiesaneElixiry (username) VALUES ('" + username + "');")

def update_namiesane(elixir, int):
    db.execute("UPDATE namiesaneElixiry SET " + elixir  + " = " + str(int) + " WHERE username = '" + session["name"] + "';")

def check_session(username):
    vlastnici = db.execute("SELECT username FROM vlastnictvo")
    for vlastnik in vlastnici:
        if vlastnik["username"] == username:
            return check2(username)
    db.execute("INSERT INTO vlastnictvo (username) VALUES ('" + username + "');")
    check2(username)

def check2(username):
    miesaci = db.execute("SELECT username FROM namiesaneElixiry")
    for miesac in miesaci:
        if miesac["username"] == username:
            return
    db.execute("INSERT INTO namiesaneElixiry (username) VALUES ('" + username + "');")


rozvrhSuroviny = [
    [],
    ["Jed", "Bulvy", "Krystal"],
    ["Zobak", "Krysodlacia", "Zlazy", "Moc"],
    ["Obria", "Roh", "Krv"],
    ["Turmericum", "Koza", "Plesen"],
    ["Sliz", "Piesok", "Slzy"],
    ["Zobak", "Sliny", "Nigrumteum"],
    ["Krv", "Zlazy"],
    ["Jed", "Plesen", "Krysodlacia"],
    ["Koza", "Turmericum", "Piesok"],
    ["Krystal", "Nigrumteum", "Sliz"],
    ["Bulvy", "Sliny", "Moc"],
    ["Obria", "Slzy"],
]

den = 0
incrementSurovin = 4


app = Flask(__name__)
app.config["SESSION_PERNEMENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



db = SQL("sqlite:///kombinacie.db")

on_start()


@app.route("/", methods=["GET"])
def index():
    if session.get("name"):
        vlastnictvoDict, keys = get_vlastnictvo(); noveElixiry = get_nove_elixiry(); den = get_den()
        return render_template("index.html", cisloDna=den, ziskaneSuroviny=rozvrhSuroviny[den], vlastnictvoDict=vlastnictvoDict, keys=keys, noveElixiry= noveElixiry, prihlasenie=session.get("name"))
    else:
        return redirect("/register")

@app.route("/cooking", methods=["POST"])
def cooking():
    magistro = request.form.get("magistro"); common = request.form.get("common")
    if not uvar([magistro, common]):
        return render_template("nedostatok.html")
    else:
        priznaky = db.execute( "SELECT " + magistro + " FROM kombinaciePriznakov WHERE Surovina = '" + common + "';")[0][magistro]
        vlastnictvoDict, keys = get_vlastnictvo(); den=get_den()
        return render_template("cooking.html", magistro=magistro, common=common, priznaky=priznaky, cisloDna=den, ziskaneSuroviny=rozvrhSuroviny[den], vlastnictvoDict=vlastnictvoDict, keys=keys, noveElixiry=get_nove_elixiry(), prihlasenie=session.get("name"))


@app.route("/dalsiDen", methods=["POST"])
def rozvrh():
    den = get_den()
    if den + 1 < len(rozvrhSuroviny):
        increment_den(den)
        novy_den_change_vlastnictvo(incrementSurovin, rozvrhSuroviny[den+1])

    return redirect("/")

@app.route("/kniznica", methods = ["GET"])
def kniznica():
    print(get_namiesane_elixiry())
    return render_template("kniznica.html", znameElixiry = get_zname_elixiry(), namiesaneElixiry = get_namiesane_elixiry())

@app.route("/odovzdaj", methods = ["GET", "POST"])
def odovzdaj():
    if request.method == "GET":
        return render_template("odovzdaj.html")
    elif request.method == "POST":
        if skontroluj(request.form):
            elixir = request.form.get("vyberElixiru")
            vysledok = "SPRAVNE, uspesne si namiesal elixir " + elixir + " zapisem ti ho do tvojho zvitku..."
            update_namiesane(elixir, 1)
        else:
            vysledok = "NESPRAVNE! Nevies varit"
        return render_template("odovzdaj.html", vysledok=vysledok)
        
@app.route("/register", methods =["GET", "POST"])
def registracia():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("name")
        session["name"] = username
        check_session(username)
        return redirect("/")
    
@app.route("/deregister")
def deregiser():
    session.clear()
    return redirect("/")

@app.route("/reset")
def reset():
    del_data(session["name"])
    set_data(session["name"])
    return redirect("/")