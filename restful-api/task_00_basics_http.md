## 🌐 1. Différences entre HTTP et HTTPS

HTTP (HyperText Transfer Protocol) et HTTPS (HyperText Transfer Protocol Secure) sont deux protocoles utilisés pour la communication entre un client (navigateur, application) et un serveur web.

| Critère       | HTTP                           | HTTPS                                                     |
|---------------|--------------------------------|------------------------------------------------------------|
| Port par défaut | 80                             | 443                                                        |
| Chiffrement     | Aucun                          | SSL/TLS                                                    |
| Sécurité        | Aucune, les données voyagent en clair | Données chiffrées, protégées                       |
| Certificat      | Non requis                     | Certificat SSL obligatoire                                 |
| Utilisation     | Sites statiques ou non sensibles | Sites sensibles, traitant des données personnelles ou bancaires |
| Vitesse         | Légèrement plus rapide         | Légèrement plus lent (chiffrement)                         |
| URL             | Commence par `http://`         | Commence par `https://`                                    |

> ✅ **HTTPS est une version sécurisée de HTTP.** Il chiffre les données échangées entre le client et le serveur à l’aide de SSL/TLS. Cela empêche les attaques de type « man-in-the-middle » et protège la confidentialité des utilisateurs.

---

## 🧾 2. Structure d’une requête et d’une réponse HTTP

📌 **Outil utilisé** : Inspecteur réseau du navigateur (onglet « Network »)

### 📤 Requête HTTP typique

```
GET /index.html HTTP 1.1
Host: www.example.com
User-Agent: Mozilla 5.0
Accept: text/html
```

- **Méthode :** GET  
- **Chemin :** `/index.html`  
- **Version :** `HTTP/1.1`  
- **En-têtes :** `Host`, `User-Agent`, `Accept`, etc.

### 📥 Réponse HTTP typique

```
HTTP/1.1 200 OK
Date : Wed, 10 Jun 2025 14 :16 :00 CEST
Content-Type: text/html
Content-Lenght : 1234

<!DOCTYPE html>
<html>…</html>
```

- **Code de statut :** `200 OK` (succès)  
- **En-têtes :** type de contenu, longueur, etc.  
- **Corps de réponse :** contient le HTML ou JSON demandé (données demandées)

---

## ⚙️ 3. Méthodes HTTP courantes

| Méthode | Description                        | Exemple concret                                  |
|---------|------------------------------------|--------------------------------------------------|
| GET     | Récupère une ressource             | Chargement d’une page web, lire une API          |
| POST    | Envoie des données                 | Soumission d’un formulaire, création d’une ressource |
| PUT     | Met à jour une ressource existante | Modification d’un profil utilisateur             |
| DELETE  | Supprime une ressource             | Suppression d’un article de blog                 |
| PATCH   | Modification partielle             | Mise à jour d’un seul champ dans une base de données |

---

## 🧩 4. Codes de statut HTTP courants

### ✅ Codes de succès (1xx)
- **102 Processing** : Requête en traitement  
  _Exemple : Utilisé dans les services WebDAV pour de longues opérations (rare)_

### ✅ Codes de succès (2xx)
- **200 OK** : Requête réussie  
  _Exemple : Chargement correct d'une page web_
- **201 Created** : Ressource créée  
  _Exemple : Création d'un nouvel utilisateur via POST_

### 🔁 Redirections (3xx)
- **301 Moved Permanently** : Redirection permanente  
  _Exemple : Redirection d'une ancienne URL vers une nouvelle_
- **304 Not Modified** : Requête inchangée depuis le dernier accès  
  _Exemple : Le cache du navigateur est encore valide_

### ⚠️ Erreurs client (4xx)
- **400 Bad Request** : Requête mal formée (champ manquant dans formulaire)  
  _Exemple : Formulaire mal rempli avec données invalides_
- **403 Forbidden** : Accès refusé (droits insuffisants)  
  _Exemple : Tentative d'accès à un dossier protégé sans autorisation_
- **404 Not Found** : Ressource inexistante  
  _Exemple : Page web supprimée ou URL mal orthographiée_

### ❌ Erreurs serveur (5xx)
- **500 Internal Server Error** : Erreur côté serveur  
  _Exemple : Bug dans le code backend non géré_
- **503 Service Unavailable** : Serveur indisponible  
  _Exemple : Serveur en maintenance ou surchargé_

---

## 📝 Résumé

- 🌐 HTTP et HTTPS sont les fondements de la communication web.  
- 🔐 HTTPS garantit la sécurité des échanges.  
- 📤 Les requêtes/réponses HTTP ont une structure précise et utilisent différentes méthodes et codes de statut pour dialoguer efficacement entre client et serveur.  
- ⚡ Le protocole HTTP/1.1 est le plus courant, mais HTTP/2 et HTTP/3 sont plus performants.  
- 🛠️ Les outils comme Wireshark permettent d’observer les paquets, mais les requêtes HTTPS sont chiffrées, donc on ne peut pas voir leur contenu.
