from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
import time
import sqlite3
from spotifailfinal import *


def charge_redi_image(picture, largeur, hauteur):
    image = Image.open(picture)
    image_redi = image.resize((largeur, hauteur))
    photo_image = ImageTk.PhotoImage(image_redi)
    return photo_image




