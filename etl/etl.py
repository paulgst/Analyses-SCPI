import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml

def url_to_dataframe(debut_url,list_scpi):
    
    i = 0

    scpi_liste = []#confronter avec list_scpi
    type_SCPI = []
    categorie = []
    capital = []
    creation = []
    capitalisation = []
    nb_associes = []
    taux_occupation_financier = []
    nb_immeubles = []
    RAN = []
    pct_charge = []

    pct_distrib_2022 = []
    variation_prix_2022 = []
    pct_distrib_2021 = []
    variation_prix_2021 = []
    pct_distrib_2020 = []
    variation_prix_2020 = []
    pct_distrib_2019 = []
    variation_prix_2019 = []
    pct_distrib_2018 = []
    variation_prix_2018 = []

    for scpi in list_scpi :

        url = debut_url + scpi
        i+=1
        # Envoie une requête GET à l'URL
        response = requests.get(url)


        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()  
            text_lines = text.strip().split('\n')

            # Initialisation
            annee = None
            pourcentage_distribution = None
            variation_prix = None

            type_SCPI_var = None
            categorie_var = None       
            capital_var = None
            creation_var = None
            capitalisation_var = None
            nb_associes_var = None
            taux_occupation_financier_var = None
            nb_immeubles_var = None
            RAN_var = None
            pct_charge_var = None

            pct_distrib_2022_var=None
            variation_prix_2022_var=None
            pct_distrib_2021_var=None
            variation_prix_2021_var=None
            pct_distrib_2020_var=None
            variation_prix_2020_var=None
            pct_distrib_2019_var=None
            variation_prix_2019_var=None
            pct_distrib_2018_var=None
            variation_prix_2018_var=None

            type_SCPI_flag = 0
            categorie_flag = 0       
            capital_flag = 0
            creation_flag = 0
            capitalisation_flag = 0
            nb_associes_flag = 0
            taux_occupation_financier_flag = 0
            nb_immeubles_flag = 0
            RAN_flag = 0
            pct_charge_flag = 0

            tableau_passage = False

            for ligne in text_lines:
                #print(ligne)


                if type_SCPI_flag == 1:
                    type_SCPI_flag = 0
                    type_SCPI_var = ligne
                    #print("Type",ligne)
                if ligne == 'Type' or ligne == 'Type ':
                    type_SCPI_flag = 1
                    #print("Type flag",ligne)

                if categorie_flag == 1:
                    categorie_flag = 0
                    categorie_var = ligne
                    #print("Catégorie",ligne)
                if (ligne == 'Catégorie' or ligne == 'Catégorie ') and not ':' in ligne :
                    categorie_flag = 1

                    #print("Catégorie flag",ligne)
                if capital_flag == 1:
                    capital_flag = 0
                    capital_var = ligne
                    #print("Capital",ligne)
                if ligne == 'Capital':
                    capital_flag = 1

                if creation_flag == 1:
                    creation_flag = 0
                    creation_var = ligne
                    #print("Création",ligne)
                if (ligne == 'Création' or ligne == 'Création ' )and not ':' in ligne :
                    creation_flag = 1

                if capitalisation_flag == 1:
                    capitalisation_flag = 0
                    capitalisation_var = ligne
                    #print("Capital",ligne)
                if 'Capitalisation' in ligne and not ':' in ligne  :
                    capitalisation_flag = 1

                if nb_associes_flag == 1:
                    nb_associes_flag = 0
                    nb_associes_var = ligne
                    #print("Nombre d'associés",ligne)
                if "Nombre d'associés" in ligne and not ':' in ligne  :
                    nb_associes_flag = 1

                if taux_occupation_financier_flag == 1:
                    taux_occupation_financier_flag = 0
                    taux_occupation_financier_var = ligne
                    #print("Taux d'occupation financier",ligne)
                if "Taux d'occupation financier" in ligne and not ':' in ligne  :
                    taux_occupation_financier_flag = 1

                if nb_immeubles_flag == 1:
                    nb_immeubles_flag = 0
                    nb_immeubles_var = ligne
                    #print("Nombre d'immeubles",ligne)
                if "Nombre d'immeubles" in ligne and not "/ nombre d'immeubles" in ligne  :
                    nb_immeubles_flag = 1                         

                if RAN_flag == 1:
                    RAN_flag = 0
                    RAN_var = ligne
                    #print("Nombre d'immeubles",ligne)
                if "RAN en % du dividende" in ligne and not ':' in ligne  :
                    RAN_flag = 1 

                if pct_charge_flag == 1:
                    pct_charge_flag = 0
                    pct_charge_var = ligne
                    #print("Nombre d'immeubles",ligne)
                if "Pourcentage de charges" in ligne and not ':' in ligne  :
                    pct_charge_flag = 1 


                if 'Taux de distribution et variation du prix' in ligne:
                    tableau_passage = True
                    #print('tableau_passage')
                if tableau_passage == True:

                    # Vérifier si la ligne contient une année
                    if ligne.strip().isdigit():
                        pourcentage_distribution  = None
                        variation_prix  = None
                        annee = int(ligne.strip())
                    # Vérifier si la ligne contient un pourcentage de distribution
                    elif ligne.strip().endswith('%'):
                        #pourcentage_distribution = ligne.strip() if pourcentage_distribution is None else None
                        #variation_prix = ligne.strip() if variation_prix == None and pourcentage_distribution is not None else None
                        if variation_prix == None and pourcentage_distribution is not None:
                            variation_prix = ligne.strip()
                        if pourcentage_distribution is None:
                            pourcentage_distribution = ligne.strip()


                    if annee is not None and pourcentage_distribution is not None and variation_prix is not None:

                        if annee == 2022:
                            pct_distrib_2022_var = pourcentage_distribution
                            variation_prix_2022_var = variation_prix

                        elif annee == 2021:
                            pct_distrib_2021_var = pourcentage_distribution
                            variation_prix_2021_var = variation_prix

                        elif annee == 2020:
                            pct_distrib_2020_var = pourcentage_distribution
                            variation_prix_2020_var = variation_prix

                        elif annee == 2019:
                            pct_distrib_2019_var = pourcentage_distribution
                            variation_prix_2019_var = variation_prix

                        elif annee == 2018:
                            pct_distrib_2018_var = pourcentage_distribution
                            variation_prix_2018_var = variation_prix

            annee = None
            pourcentage_distribution = None
            variation_prix  = None

            #on alimente les listes une fois le parcours du texte

            scpi_liste.append(scpi)
            type_SCPI.append(type_SCPI_var)
            categorie.append(categorie_var)

            capital.append(capital_var)
            creation.append(creation_var)
            capitalisation.append(capitalisation_var)
            nb_associes.append(nb_associes_var)
            taux_occupation_financier.append(taux_occupation_financier_var)
            nb_immeubles.append(nb_immeubles_var)
            RAN.append(RAN_var)
            pct_charge.append(pct_charge_var)
            print(scpi)

            pct_distrib_2022.append(pct_distrib_2022_var)
            variation_prix_2022.append(variation_prix_2022_var)
            pct_distrib_2021.append(pct_distrib_2021_var)
            variation_prix_2021.append(variation_prix_2021_var)
            pct_distrib_2020.append(pct_distrib_2020_var)
            variation_prix_2020.append(variation_prix_2020_var)
            pct_distrib_2019.append(pct_distrib_2019_var)
            variation_prix_2019.append(variation_prix_2019_var)
            pct_distrib_2018.append(pct_distrib_2018_var)
            variation_prix_2018.append(variation_prix_2018_var)        


        else:
            print("Erreur lors de la requête HTTP:", response.status_code)

    dataframe = pd.DataFrame({
    'scpi_liste':scpi_liste,
    'type_SCPI':type_SCPI,
    'categorie':categorie,
    'capital':capital,
    'creation':creation,
    'capitalisation':capitalisation,
    'nb_associes':nb_associes,
    'taux_occupation_financier':taux_occupation_financier,
    'nb_immeubles':nb_immeubles,
    'RAN':RAN,
    'pct_charge':pct_charge,
    'variation_prix_2018':variation_prix_2018,
    'variation_prix_2019':variation_prix_2019,
    'variation_prix_2020':variation_prix_2020,
    'variation_prix_2021':variation_prix_2021,
    'variation_prix_2022':variation_prix_2022,
    'pct_distrib_2018':pct_distrib_2018,
    'pct_distrib_2019':pct_distrib_2019,
    'pct_distrib_2020':pct_distrib_2020,
    'pct_distrib_2021':pct_distrib_2021,
    'pct_distrib_2022':pct_distrib_2022
    })    

    return dataframe
    
def etl():
    yaml_file = "C:/Users/paulj/Documents/Projets data/SCPI-analyses/SCPI-analyses/config/config.yaml"

    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)

    url = config["url"]
    list_scpi = config["list_scpi"]

    df = url_to_dataframe(url,list_scpi)
    df.to_excel("df_brut.xlsx")
    
if __name__ == "__main__":
    etl()