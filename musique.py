from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
import time
import sqlite3



#barre de progression du son

def update_progress():
    current_time = pygame.mixer.music.get_pos() // 1000  # Convert milliseconds to seconds
    progress_var.set(current_time)
    fenetre.after(1000, update_progress)

def play_music():
    pygame.mixer.music.load(r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\music\ene.mp3")  
    pygame.mixer.music.play()
    update_progress()

pygame.mixer.init()
