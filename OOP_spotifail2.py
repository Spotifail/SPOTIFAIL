from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
import time
import sqlite3




fenetre = Tk()
fenetre.geometry('1400x800')
fenetre.title('SPOTI-FAIL')
fenetre['bg'] = '#D46A6A' #bg = background
fenetre.resizable(height=False, width= False) # on ne peut pa modifier ni la largeur et longueur

    #heritage voir comment ca marche 


    #barre de recherche

barre_recherche = Entry(fenetre, width=50,borderwidth=8, bg="pink", fg="white")
barre_recherche.place(x='600',y='40')




class SON_MENU:
    def __init__(self, photo, list):
        self.photo = photo
        self.list = list

    def change_photo(self, )







