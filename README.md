# Stratégie globale :

Utiliser l’algorithme du min/max à profondeur donnée optimisé par la méthode alpha beta pruning. A chaque fois qu’un joueur va jouer nous allons calculer l’arbre des possibilités qui s’offrent à lui, chaque branche de l’arbre étant un sous arbre correspondant au coût possible et ce répété sur 4 tours (donc 4 niveaux sur les branches de l’arbre originel) par soucis de réalisme en temps de calcul. Pour chaque case, nous allons attribuer un poids au coup possible qui sera défini selon le barème ci-dessous. Le score d’une branche sera la somme des  poids qui auront été sélectionnés pour chaque tour en sachant qu’un tour sur deux ce poids sera négatif puisqu’il correspondra à une potentielle riposte de l’adversaire. Nous intégrerons le pruning dans la mesure où nous vérifierons que le score maximal (ou minimal selon le tour) n’est pas atteint auquel cas nous pouvons arrêter de calculer les prochains arbres.

Barème d’attribution des poids appliqué sur des lignes, des colonnes et des diagonales:

* Si la place libre a deux pions de la couleur du joueur adjacents et un espace libre soit après ces deux pions soit du côté opposé -> score de 100

* Si la place libre a un seul pion de la couleur du joueur adjacent et un espace libre ce pion ou un espace de l’autre côté -> score de 10

* Si la place libre a trois pions de la couleur du joueur adjacents et un espace libre soit après ces deux pions soit du côté opposé -> score de 1000

Nous avons décidé de valeur de poids très éloignées afin d’éviter les confusions entre le choix d’un poids ou d’un autre


# Resources 

https://fr.wikipedia.org/wiki/Algorithme_minimax

https://pageperso.lis-lab.fr/~liva.ralaivola/teachings20062005/reversi/MinMaxL2.pdf

https://eeisti.fr/grug/ING-1/Info%20/Programmation%20C/Cours/25_Minmax.pdf


Run the server : cd src/ && uvicorn main:app --reload

# Docker

## Build 

sudo docker build --no-cache -t puissance4:1 .

## Run

sudo docker run -p 8000:8000 puissance4:1
