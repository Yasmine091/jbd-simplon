# JBD Simplon

## Guide d'installation
* Pour installer et configurer le site, fais ceci dans le terminal :
```
    git clone git@gitlab.com:Yasmine091/jbd-simplon.git
    cd jbd-simplon/
    sudo pip3 install -r requirements.txt
    cd core/
    cp example.settings.py settings.py
```
* Modifie les valeurs dans le fichier settings.py
* Puis reviens au terminal et fais ceci :
```
    cd ..
    python3 manage.py migrate
    python3 manage.py runserver
```

## Dépendances
* Django >> https://
* PostgreSQL >> https://
* BootStrap >>  https://

## Version en ligne
* https://journal-de-bord-simplon.herokuapp.com

## Ressources du projet
* MCD >> https://gitlab.com/Yasmine091/jbd-simplon/-/blob/master/Ressources/MCD.png
* Maquette (Desktop) >> https://gitlab.com/Yasmine091/jbd-simplon/-/blob/master/Ressources/Wireframe_Desktop.png
* Maquette (Mobile) >> https://gitlab.com/Yasmine091/jbd-simplon/-/blob/master/Ressources/Wireframe_Mobile.png