# SmartJustice Africa

## 🇨🇲 Système de Justice Digitale pour le Cameroun

SmartJustice Africa est une plateforme digitale complète conçue pour moderniser et optimiser le système judiciaire camerounais. Elle offre une solution intégrée pour la gestion des tribunaux, le suivi des dossiers, la cartographie judiciaire et la sécurisation des données.

## ✨ Fonctionnalités Principales

### 🏛️ **Gestion des Tribunaux**
- Cartographie interactive des tribunaux camerounais
- Statistiques en temps réel par juridiction
- Suivi des dossiers et taux de traitement
- Gestion des magistrats et ressources

### 📊 **Tableau de Bord**
- Dashboard complet avec métriques clés
- Visualisation des données judiciaires
- Rapports et analyses statistiques
- Interface responsive et moderne

### 🔒 **Sécurité et Audit**
- Système d'authentification sécurisé
- Traçabilité complète des actions (audit trail)
- Gestion des alertes de sécurité
- Chiffrement des données sensibles

### 📢 **Signalements**
- Plateforme de signalement anonyme
- Catégorisation des signalements (corruption, violation, fuite)
- Suivi en temps réel des traitements
- Interface sécurisée et confidentielle

### 🌐 **API REST**
- API complète pour l'intégration
- Documentation automatique
- Authentification par token
- Endpoints pour tous les modules

## 🛠️ Technologies Utilisées

- **Backend**: Django 6.0.4
- **Base de données**: SQLite (en développement)
- **API**: Django REST Framework
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Cartographie**: Folium, Leaflet
- **Sécurité**: Cryptography, python-dotenv
- **Charts**: Chart.js

## 🚀 Installation et Configuration

### Prérequis
- Python 3.8+
- Git
- Virtualenv (recommandé)

### Installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/votre-username/smartjustice-africa.git
cd smartjustice-africa
```

2. **Créer l'environnement virtuel**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration de l'environnement**
```bash
cp .env.example .env
# Éditer .env avec vos paramètres
```

5. **Migrations de base de données**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

Accéder à l'application sur `http://127.0.0.1:8000`

## 📁 Structure du Projet

```
smartjustice_africa/
├── config/                 # Configuration Django
├── audit/                  # Module d'audit
├── cartographie/           # Module cartographique
├── dashboard/              # Tableau de bord
├── securite/               # Module sécurité
├── signalement/            # Module signalements
├── api/                    # API REST
├── templates/              # Templates HTML
├── static/                 # Fichiers statiques
├── media/                  # Fichiers médias
└── manage.py              # Script de gestion Django
```

## 🔧 Configuration

### Variables d'environnement (.env)
```env
SECRET_KEY=votre-cle-secrete
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ENCRYPTION_KEY=votre-cle-de-chiffrement
```

### Paramètres Django
- **DEBUG**: Mode développement
- **SECRET_KEY**: Clé secrète Django
- **DATABASES**: Configuration base de données
- **INSTALLED_APPS**: Applications activées

## 📊 API Endpoints

### Cartographie
- `GET /api/tribunaux/` - Liste des tribunaux
- `GET /api/tribunaux/{id}/` - Détails d'un tribunal

### Signalements
- `POST /api/signalements/` - Créer un signalement
- `GET /api/signalements/{id}/` - Consulter un signalement

### Sécurité
- `GET /api/alertes/` - Liste des alertes
- `GET /api/audit/` - Journal d'audit

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit les changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Équipe

- **Développeur Principal**: Cyrille Etobe
- **Email**: cyrilleetobe@gmail.com

## 🇨🇲 Contexte Camerounais

Ce système est spécifiquement conçu pour répondre aux défis du système judiciaire camerounais :
- Modernisation de la gestion judiciaire
- Amélioration de la transparence
- Lutte contre la corruption
- Accès facilité aux services judiciaires

---

**🇨🇲 SmartJustice Africa - Modernisons la justice camerounaise ensemble ! ⚖️**