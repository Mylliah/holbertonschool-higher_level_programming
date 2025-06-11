
# 🚀 Consommer une API avec `curl` en ligne de commande

Dans ce document, nous allons explorer l’utilisation de l’outil `curl` pour interagir avec des APIs REST, étape par étape, avec des explications claires et des exemples concrets.

---

## ❓ 1. Qu’est-ce que `curl` ?

**curl** (Client URL) est un outil en ligne de commande permettant de transférer des données vers ou depuis un serveur via des protocoles comme HTTP, HTTPS, FTP, etc.  
Il est très utilisé pour tester, déboguer et consommer des APIs RESTful.

---

## 💻 2. Installation et vérification de `curl`

- **Linux (Debian/Ubuntu) :**  
        
        sudo apt install curl


- **macOS :**  

        brew install curl


- **Windows :**  
Utiliser [WSL](https://docs.microsoft.com/fr-fr/windows/wsl/) ou télécharger curl pour Windows.

**Vérification :**

        curl --version


*Affiche la version de curl et les protocoles supportés.*

---

## 🔍 3. Effectuer une requête GET simple

Pour récupérer le contenu d’une page web : 
        curl http://example.com
Cela renvoie le HTML brut de la page example.com. C’est équivalent à visiter le site avec un navigateur, mais sans l'affichage.

Pour interroger une API publique (JSONPlaceholder) :
        curl https://jsonplaceholder.typicode.com/posts/1


**Exemple de sortie :**

        {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat...",
        "body": "quia et suscipit..."
        }



#### Schéma ASCII du flux

        [Terminal] --GET--> [Serveur API] <-- JSON --



---

## 📋 4. Récupérer uniquement les en-têtes HTTP

Utilisez l’option `-I` pour obtenir uniquement les en-têtes de la réponse :
        curl -I https://jsonplaceholder.typicode.com/posts


**Exemple de sortie :**

        HTTP/2 200
        content-type: application/json; charset=utf-8
        date: Wed, 11 Jun 2025 14:00:00 GMT



---

## 📤 5. Effectuer une requête POST

Pour envoyer des données et simuler la création d’une ressource :
        curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts


**Exemple de sortie :**
        {
        "title": "foo",
        "body": "bar",
        "userId": "1",
        "id": 101
        }


*Remarque : JSONPlaceholder ne crée pas réellement la ressource, il simule la création avec un id fictif.*

#### Schéma ASCII de la requête POST

        [Terminal] --POST (données)--> [Serveur API] <-- JSON (nouvel objet simulé) --



---

## ⚙️ 6. Explications des options `curl` utilisées

| Option         | Rôle                                                                 |
|----------------|---------------------------------------------------------------------|
| `-I`           | Récupère uniquement les en-têtes HTTP                               |
| `-X <METHOD>`  | Spécifie la méthode HTTP (GET, POST, PUT, DELETE, etc.)             |
| `-d`           | Envoie des données dans le corps de la requête (utilisé avec POST)   |

---

## ✨ 7. Astuce : Formater la sortie JSON

Pour améliorer la lisibilité des réponses JSON, utilisez l’outil [jq](https://stedolan.github.io/jq/) :
        curl -s https://jsonplaceholder.typicode.com/posts | jq

text

---

## 8. Résumé visuel du cycle d’une requête API avec `curl`

        +----------------+ (requête HTTP) +-------------------+
        | Terminal  | -----------------------> |  Serveur API |
        | (curl) | <--------------------- | (JSONPlaceholder) |
        +----------------+ (réponse JSON) +-------------------+



---

## 🏁 Conclusion

`curl` est un outil puissant et polyvalent pour explorer, tester et consommer des APIs REST directement depuis le terminal.  
Il permet de :

- Récupérer des ressources (**GET**)
- Envoyer des données (**POST**)
- Inspecter les en-têtes HTTP
- Automatiser des tests d’API

