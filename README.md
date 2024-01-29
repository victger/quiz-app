# Cinemascope - Application de Quiz sur le Cinéma
![image](https://github.com/victger/quiz-app/assets/132302057/81b96bdb-1f29-4e80-9812-2eec4bb456a8)


## Description

Cinemascope est une application web destinée aux passionnés de cinéma. Elle offre un quiz interactif composé de 10 questions variées, permettant aux utilisateurs de tester leurs connaissances cinématographiques. L'application se divise en deux parties principales : une section administrative pour la gestion des questions et une section publique pour participer au quiz.

## Fonctionnalités

- **Quiz Cinéma :** Un quiz interactif composé de 10 questions pour les amateurs de cinéma.
- **Gestion des Questions (Partie Admin) :** Permet la création, la mise à jour et la suppression des questions du quiz.
- **Participation au Quiz (Partie Publique) :** Accès libre au quiz pour tous les utilisateurs.
- **Interface Utilisateur Intuitive :** Une expérience utilisateur fluide et engageante.

## Technologies Utilisées

- **Backend :**
  - Flask : Micro-framework web pour le développement d'applications avec Python.
  - SQLite : Outil SQL et Mapping Objet-Relationnel (ORM) pour Python.

- **Frontend :**
  - Vue.js : Framework JavaScript progressif pour la construction d'interfaces utilisateur.

  [![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
  [![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)


  [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)
  [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
  
- **Schéma de la base de donnée :**
  ![image](https://github.com/victger/quiz-app/assets/132302057/3b77fb1c-027d-4adb-86ad-c0353f51bf10)

## Configuration

1. **Configuration du Backend :**
   - Installez les dépendances : `pip install -r requirements.txt`
   - Configurez la base de données : `python db.py`
   - Lancez le serveur Flask : `flask run`

2. **Configuration du Frontend :**
   - Installez les dépendances : `npm install`
   - Lancez le serveur de développement : `npm run dev`

## Configuration Docker

### Backend

1. Accédez au répertoire du backend :
    ```bash
    cd quiz-api
    ```

2. Construisez l'image Docker :
    ```bash
    docker build -t nom-utilisateur/cinemascope-backend .
    ```

3. Exécutez le conteneur Docker :
    ```bash
    docker run -p 5000:5000 nom-utilisateur/cinemascope-backend
    ```

### Frontend

1. Accédez au répertoire du frontend :
    ```bash
    cd quiz-ui
    ```

2. Construisez l'image Docker :
    ```bash
    docker build -t nom-utilisateur/cinemascope-frontend .
    ```

3. Exécutez le conteneur Docker :
    ```bash
    docker run -p 3000:80 nom-utilisateur/cinemascope-frontend
    ```

Adaptez `nom-utilisateur` et `cinemascope` selon vos préférences.

## Accès à l'Application

- Backend : [http://localhost:5000](http://localhost:5000)
- Frontend : [http://localhost:3000](http://localhost:3000)

## Utilisation

- Accédez à l'application web à l'adresse `http://localhost:3000`.
- Dans la partie publique, participez au quiz et testez vos connaissances en cinéma er consulter votre score.
- Dans la partie admin, gérez les questions du quiz (ajout, modification, suppression de question).

## Licence

Ce projet est sous licence [MIT](LICENSE).

### Projet réalisé par 
- GHATGHUT Abdelraouf
- Victor GERARD
- Louis CHAUVIN
