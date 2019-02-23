# EverView Bot

Programme de services automatisés de type bot pour le serveur Discord *EverView*.
Developpé avec soin et attention par `Poulpy#9355`.

# Utilisation

Sous un système d'exploitation tel Windows, Linux, Android ou MacOS, exécuter le fichier `main.py` dans son dossier suffira à faire tourner le bot. Il faudra cependant veiller à remplacer l'argument `os.environ["TOKEN"]` par le token du bot dans le fichier `main.py`. **IMPORTANT : Le token ne doit pas être visible dans le repo GitHub. Dans le cas contraire, la sécurité du server est fortement compromise.**
Consultez la documentation d'Heroku pour en savoir plus sur le déploiement d'applications sur ce réseau.
les logiciels nécessaires au fonctionnement du programme sont :

    - Python (version la plus récente, min. 3.6)
    
    - Librairie `discord.py` intégrée à Python
    
    - Librairie `googletrans` intégrée à Python
    
    *Note : l'utilisation du pack de commandes bash `git cli` est recommandé pour l'intégration des modules ci-dessus dans Python.*

# Architecture

Ce programme dispose d'une architecture partitionnée en différents fichiers "modules" (ex : `fun.py`, `moderator.py`), et un fichier "index" (`main.py`). Le fichier index définit le préfixe du bot, la configuration du *logging* et l'indicateur de présence du bot. Les fichiers modules définissent l'ensemble des commandes du bot et sont indispensables à son utilisation.
Le fichier `config.json` contient un ensemble d'informations importantes pour la configuration du bot, notamment : l'id du propriétaire, le préfixe du bot, les modules à exécuter au démarrage du programme et bien d'autres. Ces valeurs seront exploitées dans différentes parties de celui-ci.

# Remarques importantes

Ce programme est une distribution modifiée et remaniée du bot Discord [Kanna](https://discord.gg/PTT9UpZ), dont une version publique accessible à tous existe. Toute modification ou copie de ce logiciel pour une utilisation personnelle ou commerciale, ainsi que toute redistribution, sont permises sous seule condition de citer son créateur original (`Poulpy#9355`). Pensez au temps que m'a pris le développement de ce projet (et qu'il continue de me prendre).
Les différentes méthodes nécessaires au fonctionnement du programme présentées dans ce texte sont susceptibles de changer sans pré-avis. Veuillez prendre contact avec un des développeurs du projet en cas de dysfonctionnement.
