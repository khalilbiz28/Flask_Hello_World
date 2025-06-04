#Testin Testing TP2
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
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme_et_parite(valeur1, valeur2):
    resultat = valeur1 + valeur2
    if resultat % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
    
    return f"<h2>La somme des deux valeurs est : {resultat}</h2>" \
           f"<h3>Cette somme est un nombre {parite}.</h3>"

@app.route('/somme_tout/<path:valeurs>')
def somme_toutes_valeurs(valeurs):
    try:
        # Récupération des valeurs sous forme de liste de chaînes
        liste_str = valeurs.split('/')
        # Conversion en entiers
        liste_int = [int(val) for val in liste_str]
        # Calcul de la somme
        total = sum(liste_int)
        return f"<h2>La somme de toutes les valeurs est : {total}</h2>"
    except ValueError:
        return "<h3>Erreur : Veuillez entrer uniquement des nombres entiers dans l’URL.</h3>"

@app.route('/max_val/<path:valeurs>')
def valeur_maximale(valeurs):
    try:
        # Récupération des valeurs sous forme de liste de chaînes
        liste_str = valeurs.split('/')
        # Conversion en entiers
        liste_int = [int(val) for val in liste_str]
        # Recherche de la valeur maximale avec une boucle
        max_val = liste_int[0]
        for val in liste_int:
            if val > max_val:
                max_val = val
        return f"<h2>La valeur maximale saisie est : {max_val}</h2>"
    except ValueError:
        return "<h3>Erreur : Veuillez entrer uniquement des nombres entiers dans l’URL.</h3>"

@app.route('/cv')
def afficher_cv():
    return render_template('cv.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
