import tkinter as tk
from tkinter import ttk
import pygame
import time

def update_progress():
    current_time = pygame.mixer.music.get_pos() // 1000  # Convert milliseconds to seconds
    progress_var.set(current_time)
    root.after(1000, update_progress)

def play_music():
    pygame.mixer.music.load(r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\music\ene.mp3")  # Remplacez "votre_musique.mp3" par le chemin de votre fichier audio
    pygame.mixer.music.play()
    update_progress()

root = tk.Tk()
root.title("Lecteur Audio")

# Initialisation de Pygame (assurez-vous d'avoir Pygame installé : pip install pygame)
pygame.mixer.init()

# Bouton pour démarrer la musique
play_button = tk.Button(root, text="Play Music", command=play_music)
play_button.pack(pady=20)

# Barre de progression
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill="x", padx=20, pady=10)

root.mainloop()
