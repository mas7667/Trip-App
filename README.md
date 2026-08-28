# ProSport Voyages

**ProSport Voyages** est une application web de gestion de voyages sportifs développée avec Django. Elle permet aux gestionnaires de planifier des voyages, d’y associer des événements, et aux utilisateurs de s’y inscrire via une interface conviviale.

---

## Fonctionnalités principales

- Gestion des voyages et événements associés
- Filtrage des événements par voyage
- Formulaire d’inscription pour les participants
- Tableau de bord dynamique avec statistiques et indicateurs de progression
- Interface administrateur pour la gestion des utilisateurs et des données
- Interface utilisateur responsive avec Bootstrap

---

## Technologies utilisées

- Backend : Django 5.1.5
- Frontend : HTML5, CSS3, Bootstrap 5
- Base de données : SQLite (dev) / PostgreSQL (production)
- Outils : Python 3, Git, GitHub

---

## Captures d’écran

## Installation et vérification

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

Variables de production : `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` et `DJANGO_ALLOWED_HOSTS`.

Les opérations de création, modification et suppression des voyages et événements sont réservées aux superutilisateurs. Un utilisateur authentifié ne peut gérer que ses propres réservations.
