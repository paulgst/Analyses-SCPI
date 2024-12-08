from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Chargez votre modèle préenregistré avec Pickle
with open('modele.pickle', 'rb') as model_file:
    model = pickle.load(model_file)
    
with open('sc_fit.pickle', 'rb') as model_file:
    sc_fit = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérez les variables d'entrée depuis le formulaire

    nb_immeubles = 130
    pct_charge = 30

    #pct_distrib_2018 = float(request.form['pct_distrib_2018'])
    pct_distrib_2018 = float(request.form['pct_distrib_2018'])
    pct_distrib_2019 = float(request.form['pct_distrib_2019'])
    pct_distrib_2020 = float(request.form['pct_distrib_2020'])
    pct_distrib_2021 = float(request.form['pct_distrib_2021'])
    
    variation_prix_2019 = pct_distrib_2019-pct_distrib_2018
    variation_prix_2020 = pct_distrib_2020-pct_distrib_2019
    variation_prix_2021 = pct_distrib_2021-pct_distrib_2020
    variation_prix_2018 = (variation_prix_2019+variation_prix_2020+variation_prix_2021)/3


    capital_var = request.form['capital']    

    categorie_var = request.form['categorie']

    capital = 0
    
    type_SCPI = 0
    
    categorie_act_log = 0
    categorie_bureaux = 0
    categorie_commerce = 0
    categorie_diversifiee = 0
    categorie_residentiel = 0
    categorie_sante_education = 0
    categorie_tourisme_loisirs = 0

    if capital_var == 'Fixe':
        capital = 1
  
        
    if categorie_var == 'Activités / Logistique':
        categorie_act_log = 1
    elif categorie_var == 'Bureaux':
        categorie_bureaux = 1
    elif categorie_var == 'Commerce':
        categorie_commerce = 1
    elif categorie_var == 'Diversifiée':
        categorie_diversifiee = 1
    elif categorie_var == 'Résidentiel':
        categorie_residentiel = 1
    elif categorie_var == 'Santé et éducation':
        categorie_sante_education = 1
    elif categorie_var == 'Tourisme et loisirs':
        categorie_tourisme_loisirs = 1
    else:
        categorie_diversifiee = 1
    

    # Effectuez la prédiction avec votre modèle
    
    
    X = [[type_SCPI, capital, nb_immeubles, pct_charge, variation_prix_2018, variation_prix_2019,
                              variation_prix_2020, variation_prix_2021, pct_distrib_2018,
                              pct_distrib_2019, pct_distrib_2020, pct_distrib_2021, categorie_act_log,categorie_bureaux,categorie_commerce,
                             categorie_diversifiee,categorie_residentiel,categorie_sante_education,categorie_tourisme_loisirs]]
    
    X_sc = sc_fit.transform(X)
    prediction = model.predict(X_sc)

    # Retournez la prédiction en tant que réponse JSON
    return render_template('index.html', prediction=round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)