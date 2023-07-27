import pandas as pd
import json
import os

def csv_to_json(file_path, output_path):
    # lire le fichier CSV
    df = pd.read_csv(file_path, delimiter='|')
    
    # remplacer NaN par une chaine vide
    df = df.fillna('')
    
    # convertir le dataframe en une liste de dictionnaires
    documents = df.to_dict(orient='records')
    
    # Créer un dictionnaire pour les en-têtes et les documents
    data = {
        "partition_id": 1,
        "headers": {
            "original_filename": "",
            "project": "Inbound",
            "app_source": "S4",
            "hip_exchange": "",
            "line_number": 1,
            "line_count": len(documents),
            "batch_number": 102,
            "batch_start_line": 10,
            "batch_end_line": 20,
            "last_batch": True,
            "hip_timestamp": "2021-02-05T19:14:42Z",
            "hip_timezone": "UTC+2"
        },
        "documents": documents
    }
    
    # écrire le JSON dans un fichier
    with open(output_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# utilisations
# csv_to_json('input.csv', 'output.json')
# csv_to_json('S4_PO_20230724050000.txt', 'output.json')

# Pour tous les fichiers dans le répertoire spécifié
directory = "/Users/harisbaran/Documents/_Projets/Python/Python_Automation_Scripts/Python_csv_to_json/input"
for filename in os.listdir(directory):
    if filename.startswith("S4_PO_"):
        csv_file = os.path.join(directory, filename)
        json_file = os.path.join(directory, filename[:-4] + '.json') # changer l'extension à .json
        csv_to_json(csv_file, json_file)