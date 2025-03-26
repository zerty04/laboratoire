import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import time


passwords = ["shadow", "access", "matrix", "glitch", "cyber", "neon"]
password = random.choice(passwords)  
attempts = 5 

# animation du début
def boot_animation():
    boot_messages = [
        "Initializing system...",
        "Loading kernel modules...",
        "Connecting to secure server...",
        "Decrypting classified data...",
        "Accessing restricted files...",
        "Running security protocols...",
        "No intrusions detected.",
        "System ready. Awaiting command...",
    ]
    for msg in boot_messages:
        terminal.config(state=tk.NORMAL)
        terminal.insert(tk.END, f"{msg}\n", "boot")
        terminal.config(state=tk.DISABLED)
        terminal.see(tk.END)
        root.update()
        time.sleep(random.uniform(0.2, 0.5))
    terminal.config(state=tk.NORMAL)
    terminal.insert(tk.END, "\n", "output")
    terminal.config(state=tk.DISABLED)

# === Fonction de vérification du mot de passe ===
def check_password():
    global attempts
    guess = entry.get().strip().lower()
    
    terminal.config(state=tk.NORMAL)
    terminal.insert(tk.END, f"> {guess}\n", "command")
    terminal.config(state=tk.DISABLED)
    terminal.see(tk.END)
    
    if guess == "hint":
        response = f"Le mot de passe commence par '{password[0]}' et contient {len(password)} lettres."
    elif guess == "list":
        response = "Liste des mots de passe possibles : " + ", ".join(passwords)
    elif guess.startswith("hack "):
        attempt = guess.split(" ", 1)[1]  # Récupère le mot après "hack "
        if attempt == password:
            response = "Accès autorisé ! Vous avez piraté le système ! 🔓"
            messagebox.showinfo("Hacking réussi", response)
            root.quit()
        else:
            attempts -= 1
            if attempts > 0:
                response = f"Accès refusé ! Tentatives restantes : {attempts}"
            else:
                response = f"Échec du hack ! Le mot de passe était : {password}"
                messagebox.showerror("Game Over", response)
                root.quit()
    else:
        response = "Commande invalide. Utilisez :\n- 'hint' pour un indice\n- 'list' pour voir les mots possibles\n- 'hack [mot]' pour tenter un hack."
    
    terminal.config(state=tk.NORMAL)
    terminal.insert(tk.END, f"{response}\n\n", "output")
    terminal.config(state=tk.DISABLED)
    terminal.see(tk.END)
    entry.delete(0, tk.END)

# Interface graphique 
root = tk.Tk()
root.title("Hacker Terminal")
root.configure(bg="black")
root.geometry("900x550")
root.resizable(True, True)

# Zone de texte défilante pour afficher le terminal
terminal = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="black", fg="green", 
                                     insertbackground="green", font=("Courier New", 14, "bold"),
                                     borderwidth=2, relief=tk.SUNKEN, state=tk.DISABLED)
terminal.tag_config("boot", foreground="lightgreen", font=("Courier New", 12))
terminal.tag_config("command", foreground="lime", font=("Courier New", 14, "bold"))
terminal.tag_config("output", foreground="lightgreen", font=("Courier New", 13))
terminal.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Entrée utilisateur
entry_frame = tk.Frame(root, bg="black")
entry_frame.pack(pady=5, padx=10, fill=tk.X)

entry = tk.Entry(entry_frame, bg="black", fg="green", insertbackground="green", 
                 font=("Courier New", 14, "bold"), borderwidth=2, relief=tk.SUNKEN)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
entry.bind("<Return>", lambda event: check_password())

# Bouton d'envoi
send_button = tk.Button(entry_frame, text="Execute", command=check_password, bg="black", fg="green", 
                        font=("Courier New", 10, "bold"), borderwidth=2, relief=tk.RAISED, activebackground="darkgreen")
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Rendre la fenêtre responsive
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
terminal.pack(fill=tk.BOTH, expand=True)
entry_frame.pack(fill=tk.X)

# Effet de démarrage
entry.focus()
root.after(500, boot_animation)
root.mainloop()