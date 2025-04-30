import time
from mastermind import mastermind  # L'importation doit pointer vers le sous-dossier


def lancer_jeu(jeu_module, nom_jeu):
    print(f"\n🎮 Lancement de {nom_jeu}...")
    time.sleep(1)
    jeu_module.run()  # Appel de la fonction run() du jeu
    print(f"✅ {nom_jeu} terminé !\n")
    time.sleep(1)

def main():
    print("🧠 Bienvenue dans le HackHub Multi-Jeux 💥\n")
    time.sleep(1)

    # Liste des jeux à lancer
    jeux = [
        (mastermind, "Mastermind"),
        (index, "Crack the Code"),  # Jeu contenu dans index.py
    ]

    # Lancement de Mastermind en premier
    lancer_jeu(mastermind, "Mastermind")

    import index  # Ton deuxième jeu (index.py)
    
    # Une fois Mastermind terminé, lancer index
    lancer_jeu(index, "Crack the Code")

    print("🏁 Tous les jeux sont terminés ! GG 👾")

if __name__ == "__main__":
    main()