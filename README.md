# Francis Kago — Flask App Docker
## CC1 · Conduite de Projet · AGILE / DEVOPS / KANBAN · KEYCE

---

## 📁 Structure du dépôt

```
francis-kago-flask-app/
├── app.py                   # Application Flask (frontend designé)
├── Dockerfile               # Image Docker Python 3.9
├── requirements.txt         # Dépendances Python
├── commands_history.txt     # Historique de toutes les commandes
├── jenkins/
│   └── Jenkinsfile          # Pipeline CI/CD Jenkins (TP2)
└── pritunl-vpn/             # TP3 Docker Compose
    ├── docker-compose.yml   # Orchestration Pritunl + MongoDB
    ├── .env                 # Variables d'environnement
    └── volumes/
        ├── pritunl/         # Données persistantes Pritunl
        └── mongodb/         # Données persistantes MongoDB
```

---

## 🐳 TP1 — Lancer l'application

```bash
# Construire l'image
docker build -t franciskago-flask-app .

# Lancer le conteneur
docker run -d -p 5000:5000 --name franciskago-container franciskago-flask-app

# Accéder à l'app
open http://localhost:5000
```

## 🔗 Image DockerHub
https://hub.docker.com/r/franciskago/franciskago-flask-app

---

## ⚙️ TP2 — Pipeline Jenkins

Le Jenkinsfile se trouve dans `jenkins/Jenkinsfile`.
3 étapes : **Clonage → Image → Publication**

---

## 🌐 TP3 — VPN Pritunl

```bash
cd pritunl-vpn

# Vérifier le module tun
lsmod | grep tun
# Si absent : sudo modprobe tun

# Créer les dossiers de volumes
mkdir -p volumes/pritunl volumes/mongodb

# Lancer
docker-compose up -d

# Interface admin : https://localhost
```

---

**Auteur** : Francis Kago · M1 IABD · KEYCE Informatique & IA
