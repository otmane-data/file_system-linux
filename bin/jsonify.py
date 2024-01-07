#!/bin/python3

import json

dict = {"status": "off",
        "connected_user": None,
        "time": "not configured"
        }
with open("./status.json","w") as f:
        json.dump(dict,f,indent=4)

utilisateur = {
         "nom_utilsateur" : None,
         "mot_de_passe" : "",
}
with open("./utilisateur.json","w") as f:
        json.dump(utilisateur,f,indent=4)
