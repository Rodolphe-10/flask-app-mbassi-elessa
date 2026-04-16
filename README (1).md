# 🐳 Flask App — Mbassi Elessa
### CC1 · Conduite de Projet · AGILE / DEVOPS / KANBAN
**KEYCE Informatique & Intelligence Artificielle — M1 IABD**

---

## 📁 Structure du projet

```
Flask_app/
├── app.py                          # Application Flask avec frontend designé
├── Dockerfile                      # Image Docker Python 3.9-slim
├── requirements.txt                # Dépendances Python (Flask)
├── historiques_commandes_TP1.txt   # Historique des commandes TP1
├── jenkins/
│   ├── Jenkinsfile                 # Pipeline CI/CD Jenkins (TP2)
│   └── Capture_pipeline.png        # Capture du pipeline exécuté
└── pritunl-vpn/                    # TP3 Docker Compose
    ├── docker-compose.yml          # Orchestration Pritunl + MongoDB
    ├── .env                        # Variables d'environnement
    └── volumes/
        ├── pritunl/                # Données persistantes Pritunl
        └── mongodb/                # Données persistantes MongoDB
```

---

## TP1 — Docker (Dockerfile, Image, Conteneur)

### Prérequis
- Docker installé sur la machine
- Connaissance de base en ligne de commande

### Lancer l'application

```bash
# 1. Construire l'image
docker build -t franciskago-flask-app .

# 2. Lancer le conteneur
docker run -d -p 5000:5000 --name franciskago-container franciskago-flask-app

# 3. Accéder à l'application
# Ouvrir dans le navigateur : http://localhost:5000
```

### Image DockerHub
```
https://hub.docker.com/r/kevinmbassi/flask-app-mbassi-elessa
```

---

## TP2 — CI/CD Jenkins

Pipeline automatisé en 3 étapes :

| Étape | Description |
|---|---|
| **Clonage** | Clone app.py et requirements.txt depuis GitHub |
| **Image** | Construit l'image Docker |
| **Publication** | Publie l'image sur DockerHub |

### Lancer Jenkins

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

Accès : **http://localhost:8080**

---

## TP3 — Docker Compose (Pritunl VPN + MongoDB)

### Prérequis

```bash
# Vérifier le module tun
lsmod | grep tun

# Si absent
sudo modprobe tun
```

### Lancer les services

```bash
cd pritunl-vpn

# Lancer MongoDB + Pritunl
docker-compose up -d

# Vérifier les conteneurs
docker ps
```

### Services déployés

| Service | Image | Port |
|---|---|---|
| **Pritunl** | jippi/pritunl:latest | 443, 80, 1194/udp |
| **MongoDB** | mongo:5.0 | 27017 (interne) |

Interface admin Pritunl : **https://localhost**

---

## TP4 — Gestion de projet (Trello & Jira)

- **Trello** : Tableau Kanban avec 4 colonnes (Backlog, En cours, Terminé, Bloqué)
- **Jira** : Projet Scrum **"Mbassi Elessa"** avec toutes les tâches des 4 TPs

---

## 👨‍💻 Auteur

**Mbassi Elessa** · M1 IABD · KEYCE Informatique & Intelligence Artificielle
