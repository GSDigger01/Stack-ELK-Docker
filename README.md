<p align="center">
  <img src="Cover.png" alt="Stack ELK via Docker" width="50%">
</p>

# 📦 Déploiement de la stack ELK avec collecte de données via API Amazon

---

## 🔧 À propos du projet

Ce dépôt contient l’ensemble des fichiers de configuration nécessaires pour :

- Déployer la stack **ELK** (Elasticsearch, Logstash, Kibana) via `docker-compose`
- Collecter et transformer des données issues d’une API Amazon avec un script Python
- Exporter ces données au format `.csv` pour analyse
- Et en bonus : planifier l’exécution automatique des tâches via un **job scheduler**

---

## ⚙️ Composants principaux

### 🐳 Stack ELK
- Déploiement de la suite ELK avec `docker-compose`
- Configuration de **Logstash** pour parser et injecter les données dans **Elasticsearch**
- Visualisation des logs et des métriques dans **Kibana**

### 🐍 Extraction & transformation de données
- Script Python pour :
  - Se connecter à une **API Amazon**
  - Récupérer les données de produits ou ventes
  - Nettoyer / transformer les données
  - Exporter vers un fichier `.csv`

### ⏱️ Automatisation
- Mise en place d’un **job de planification** (cron ou équivalent) pour exécuter le pipeline à intervalle régulier

---

## 🧰 Outils & technologies

- Docker & Docker Compose  
- Elasticsearch, Logstash, Kibana  
- Python (requests, pandas)  
- Job scheduler (Cron, Task Scheduler, etc.)

---

