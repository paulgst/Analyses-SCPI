Le but ici est de livrer une analyse et une tentative de prédiction des rendements que peut offir les SCPI. Pour cela, j'ai extrait et utilisé les données du site https://www.centraledesscpi.com/scpi/

Les parts de SCPI représentent un investissement immobilier dont le risque est modéré et dont les revenus sont assurés par le pourcentage de distribution (loyers) et la plus-value que l'on peut faire au moment de la revente des parts correspondant à la variation du prix d'acquisition. En général, il y a des frais de souscription et des frais de gestion mais les pourcentages de distribution sont calculés par rapport au prix total, donc net de ces frais.

On va réaliser :

- la collecte des données
- le preprocessing des données
- la data analyse
- la prédiction du pourcentage de distribution grâce au machine learning
- un classement des SCPI les plus rentables en prennant compte le pourcentage de distribution et la revalorisation du capital investi
- la mise en place d'une API et d'un portail internet

Voici quelques définitions concernant le jeu de données que l'on a construit :

- Type de SCPI : SCPI à rendement (issu essentiellement des loyers perçus) ou de plus-value (réalisé sur l'acquisation et la vente des actifs)
- Catégorie : concerne quels sont essentiellement les types de locaux acquis (bureaux, commerce, santé, etc...)
- Capital : une SCPI à capital variable permet d'acheter des parts dont le prix varie en fonction du marché immobilier, alors qu'une SCPI à capital fixe permet d'acheter des parts dont le prix varie en fonction de leurs attraits auprès des investisseurs.
- Taux d'occupation financier : total des loyers et indemnités facturés divisés par le total des loyers qui seraient facturés si les locaux étaient intégralement loués.
- RAN : Report À Nouveau, correpondant à une réserve financière

