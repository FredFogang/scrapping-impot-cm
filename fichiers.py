import requests
import pandas as pd

def telecharger_fichier(url, nom_fichier):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi (status code 200)

        with open(nom_fichier, 'wb') as fichier:
            fichier.write(response.content)
        
        print(f"Le fichier '{nom_fichier}' a été téléchargé avec succès.")
        
        # Convertir le fichier Excel en CSV
        df = pd.read_excel(nom_fichier)
        nom_fichier_csv = nom_fichier.replace('.xlsx', '.csv')
        df.to_csv(nom_fichier_csv, index=False)
        print(f"Le fichier '{nom_fichier_csv}' a été créé avec succès.")
        
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("Erreur 404 : Le fichier demandé n'a pas été trouvé. Vérifie l'URL.")
        else:
            print(f"Erreur lors du téléchargement : {err}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation avec le chemin spécifié
url = "https://teledeclaration-dgi.cm/UploadedFiles/AttachedFiles/ArchiveListecontribuable/FICHIER%20JANVIER%202024.xlsx"
chemin = r"C:\Users\FRED FOGQNG\Downloads\PROJET\FICHIER_JUILLET_2024.xlsx"
telecharger_fichier(url, chemin)