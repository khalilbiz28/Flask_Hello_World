from flask import Flask
from flask import render_template
from flask import json
import sqlite3                                                                     
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return f"<h2>Le carré de votre valeur est : {val_user * val_user}</h2>"

@app.route('/somme/<int:val1>/<int:val2>')
def somme(val1, val2):
    resultat = val1 + val2
    if resultat % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
    return f"<h2>La somme de {val1} et {val2} est : {resultat}</h2><p>Ce nombre est {parite}.</p>"

@app.route('/somme_multiple/', defaults={'nombres': ''})
@app.route('/somme_multiple/<path:nombres>')
def somme_multiple(nombres):
    try:
        liste = [int(n) for n in nombres.split('/') if n.strip() != '']
        resultat = sum(liste)
        return f"<h2>Les valeurs : {liste}</h2><p>La somme de ces valeurs est : {resultat}</p>"
    except ValueError:
        return "<h2>Erreur : Veuillez entrer uniquement des nombres entiers dans l’URL.</h2>"

@app.route('/valeur_maximale/', defaults={'nombres': ''})
@app.route('/valeur_maximale/<path:nombres>')
def valeur_maximale(nombres):
    try:
        # Convertir chaque nombre de l'URL en une liste d'entiers
        liste = [int(n) for n in nombres.split('/') if n.strip() != '']
        
        # Trouver la valeur maximale
        max_valeur = max(liste)
        
        return f"<h2>Les valeurs sont : {liste}</h2><p>La valeur maximale parmi ces valeurs est : {max_valeur}</p>"
    except ValueError:
        return "<h2>Erreur : Veuillez entrer uniquement des nombres entiers dans l’URL.</h2>"

@app.route('/cv')
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
  app.run(debug=True)   #commit222
