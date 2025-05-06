import time
import subprocess

def lancer_jeu(fichier, nom_jeu):
    print(f"\n🎮 Lancement de {nom_jeu}...")
    time.sleep(1)
    try:
        subprocess.run(["python", fichier], check=True)
        print(f"✅ {nom_jeu} terminé !\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur dans {nom_jeu} : {e}")
    time.sleep(1)

def main():
    print("🧠 Bienvenue dans le HackHub Multi-Jeux 💥\n")
    time.sleep(1)

    jeux = [
        ("mastermind/mastermind.py", "Mastermind"),
        ("index.py", "Crack the Code"),
        ("Fils_électriques/Fils.py", "Jeu 3"),
        ("Dossier/code.py", "Jeu 4")
    ]

    for fichier, nom in jeux:
        lancer_jeu(fichier, nom)

    print("🏁 Tous les jeux sont terminés ! GG 👾")

if __name__ == "__main__":
    main()
