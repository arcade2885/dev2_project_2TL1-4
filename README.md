# Soirée Quiz

## Prérequis

- Python 3
- Tkinter, généralement inclus avec Python

Aucune dépendance Python externe n'est nécessaire.

## Lancer l'application

Depuis le dossier racine du projet, exécutez :

```powershell
python src\main.py
```

Le menu principal propose les actions suivantes :

1. **Gérer les équipes** : créer une équipe, réinitialiser les scores, supprimer une équipe par son identifiant ou supprimer toutes les équipes.
2. **Afficher les équipes** : consulter les équipes enregistrées et leurs scores.
3. **Question** : ouvrir l'interface du quiz, choisir une question, afficher sa réponse et gérer les jokers. Après la question, attribuer un point à une équipe en saisissant son identifiant.
4. **Quitter** : enregistrer les équipes et fermer le jeu.

## Données

Les données sont stockées dans le dossier `data/` :

- `equipe.json` contient les équipes, leur identifiant, leur nom, leur score et l'état de leur joker.
- `question.json` contient les questions, leurs réponses, leur nombre de points et leur difficulté.

Les fichiers doivent contenir un objet JSON avec une clé `equipes` ou `questions`, dont la valeur est une liste. Exemple :

```json
{
  "equipes": [
    {
      "id": 1,
      "nom": "Équipe A",
      "scoreTotal": 0,
      "jokerUtilise": false
    }
  ]
}
```

```json
{
  "questions": [
    {
      "id": 1,
      "question": "Quelle est la capitale de la France ?",
      "reponse": "Paris",
      "points": 1,
      "difficulte": "Facile"
    }
  ]
}
```

Les équipes sont sauvegardées dans `equipe.json` lors de leurs modifications et à la fermeture du jeu. Pour utiliser le mode question, ajoutez au moins une question dans `question.json`.

## Lancer les tests

Depuis le dossier racine du projet :

```powershell
python -m unittest discover -s tests -v
```

## Structure du projet

```text
data/
  equipe.json       # Équipes et scores sauvegardés
  question.json     # Questions du quiz
src/
  classement.py     # Affichage du classement
  equipe.py         # Gestion des équipes
  gui.py            # Interface graphique du quiz
  joker.py          # Règles des jokers
  main.py           # Menu et lancement du jeu
  question.py       # Modèle des questions
  storage.py        # Lecture et écriture des fichiers JSON
tests/              # Tests unitaires
```
