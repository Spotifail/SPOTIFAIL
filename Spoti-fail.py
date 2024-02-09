from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
import time


# parametres de la fenetre 

#code

# les fentres du menu
def deuxieme_fenetre():
    # Get the current position of the first window
    x = fenetre.winfo_x()
    y = fenetre.winfo_y()

    # Hide the first window
    fenetre.withdraw()

    # Create the second window
    global fenetre2
    fenetre2 = Toplevel(fenetre)
    fenetre2['bg'] = '#330019' #bg = background
    fenetre2.geometry(f"{fenetre.winfo_width()}x{fenetre.winfo_height()}+{x}+{y}")
    fenetre2.title('SPOTI-FAI')

    button = Button(fenetre2, text="retour", command=retour2)
    button.place(x=0,y=0)


    barre_recherche = Entry(fenetre2, width=50,borderwidth=8, bg="pink", fg="white")
    barre_recherche.place(x='600',y='40')



    # fonction permettant de redimensionner la taille des images 
    def charge_redi_image(picture, largeur, hauteur):
        image = Image.open(picture)
        image_redi = image.resize((largeur, hauteur))
        photo_image = ImageTk.PhotoImage(image_redi)
        return photo_image



    # Specify the target width and height for the displayed images
    largeur = 50
    hauteur = 50

    # Assuming you have an image file named "example.png" in the current directory
    picture = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
    image_redi = charge_redi_image(picture, largeur, hauteur)

    picture2 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png"
    image_redi2 = charge_redi_image(picture2, largeur, hauteur)

    picture3 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
    image_redi3 = charge_redi_image(picture3, largeur, hauteur)





    #menu son aleatoire et zone de frame

    frame_menu_lateraleD = Frame(fenetre2, bg="purple", width=140, height=500)
    frame_barre_larteraleG = Frame(fenetre2, bg="purple", width=1400, height=600)

    frame_menu_son_milieu = Frame(fenetre2, bg="brown", width=780, height=800)

    frame_barre_horizontale = Frame(fenetre2, bg="pink", width=1400, height=500)




    # le bouton play next et previous
    play = Button(fenetre2,image=image_redi3,command=play_music)

    previous = Button(fenetre2,image=image_redi2)

    next = Button(fenetre2,image=image_redi)

        #inserer image sur un boutons  
        # Ajout de widgets à la fenêtre
    Label(fenetre2, text='researche bar', font=('Verdana', 15)).place(x='680',y='10')
    Label(fenetre2, text='Menu', font=('Verdana', 15)).place(x='10',y='20') 
        
    #le son partie 2

    # Bouton pour démarrer la musique
    # Barre de progression
    progress_var = IntVar()
    progress_bar = ttk.Progressbar(fenetre2, variable=progress_var, maximum=100, length=700)


        # Créer un objet photoimage pour utiliser l'image
    photo1 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo1 = photo1.subsample(2, 2) # redimensionne la taille de l'image

    photo2 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo2 = photo2.subsample(2, 2)

    photo3 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo3 = photo3.subsample(2, 2)
        #####
    photo4 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo4 = photo4.subsample(2, 2) # redimensionne la taille de l'image

    photo5 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo5 = photo5.subsample(2, 2)

    photo6 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo6 = photo6.subsample(2, 2)

    photo7 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo7 = photo7.subsample(2, 2) # redimensionne la taille de l'image

    photo8 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    Photo8 = photo8.subsample(2, 2)

    photo9 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    photo9 = photo9.subsample(2, 2)

    photo10 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo10 = photo10.subsample(2, 2) # redimensionne la taille de l'image

    photo11 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo11 = photo11.subsample(2, 2)

    photo12 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\2.png") 
    photo12 = photo12.subsample(2, 2)

    photo13 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo13 = photo13.subsample(2, 2) # redimensionne la taille de l'image

    photo14 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    photo14 = photo14.subsample(2, 2)

    photo15 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo15 = photo15.subsample(2, 2)

    photo16 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo16 = photo16.subsample(2, 2)



        #boutons
    button1 = Button(fenetre2, text='menu', width=16, height=8, command=deuxieme_fenetre) 
    button1.place(x='50',y='50') 

    button2 = Button(fenetre,text='playlist', width=16, height=8, command=troisieme_fenetre)
    button2.place(x='50',y='220') 

    button3 = Button(fenetre,text='favoris',width=16, height=8, command=quatrieme_fenetre)
    button3.place(x='50',y='400') 

    son_menu1 = Button(fenetre2, image=photo4)
    son_menu2 = Button(fenetre2, image=photo5)
    son_menu3 = Button(fenetre2, image=photo6)
    son_menu4 = Button(fenetre2, image=photo7)
    son_menu5 = Button(fenetre2, image=photo7)
    son_menu6 = Button(fenetre2, image=photo9)
    son_menu7 = Button(fenetre2, image=photo10)
    son_menu8 = Button(fenetre2, image=photo11)
    son_menu9 = Button(fenetre2, image=photo12)
    son_menu10 = Button(fenetre2, image=photo13)
    son_menu11= Button(fenetre2, image=photo14)
    son_menu12= Button(fenetre2, image=photo15)
    son_barre_laterale= Button(fenetre2, image=photo16)
    son_barre_horizontale= Button(fenetre2, text="playlist", width=30, height=30)


    # emplacement de la barre de progression


    #son_menu1.grid(row=0,column=0)
    son_menu1.place(x='400', y='100')
    #son_menu2.grid(row=1,column=0)
    son_menu2.place(x='600', y='100')
    #son_menu3.grid(row=2,column=2)
    son_menu3.place(x='800', y='100')
    #son_menu4.grid(row=3,column=3)
    son_menu4.place(x='1000', y='100')
    #son_menu5.grid(row=0,column=0)
    son_menu5.place(x='400', y='250')
    #son_menu6.grid(row=0,column=0)
    son_menu6.place(x='600', y='250')
    #son_menu7.grid(row=1,column=1)
    son_menu7.place(x='800', y='250')
    #son_menu8.grid(row=2,column=2)
    son_menu8.place(x='1000', y='250')
    #son_menu9.grid(row=3,column=3)
    son_menu9.place(x='400', y='400')
    #son_menu10.grid(row=4,column=4)
    son_menu10.place(x='600', y='400')
    #son_menu11.grid(row=2,column=1)
    son_menu11.place(x='800', y='400')
    #son_menu12.grid(row=2,column=1)
    son_menu12.place(x='1000', y='400')

    son_barre_laterale.place(x='30', y='660')
    son_barre_horizontale.place(x='1170', y='90')

        #les boutons next .....
    previous.place(x=600, y=670)
    play.place(x=700, y=670)
    next.place(x=800, y=670)
    # emplacement de la barre de progression 
    progress_bar.place(x=400, y=750)

    frame_menu_lateraleD.place(x=40, y=30)
    frame_barre_larteraleG.place(x=1150, y=30)
    frame_menu_son_milieu.place(x=350, y=80)
    frame_barre_horizontale.place(x=0,y=650)





    # Lier la fonction de rappel à l'événement de fermeture de la deuxième fenêtre
    fenetre4.protocol("WM_DELETE_WINDOW", dans_fenetre2)
def dans_fenetre2():
    # Fermer la première fenêtre lorsque la seconde est fermée
    fenetre.destroy()
def troisieme_fenetre():
    # Get the current position of the first window
    x = fenetre.winfo_x()
    y = fenetre.winfo_y()

    # Hide the first window
    fenetre.withdraw()

    # Create the second window
    global fenetre3
    fenetre3 = Toplevel(fenetre)
    fenetre3['bg'] = '#D46A6A' #bg = background
    fenetre3.geometry(f"{fenetre.winfo_width()}x{fenetre.winfo_height()}+{x}+{y}")
    fenetre3.title('SPOTI-FAIL')

    button = Button(fenetre3, text="retour", command=retour2)
    button.place(x=0,y=0)


    barre_recherche = Entry(fenetre3, width=50,borderwidth=8, bg="pink", fg="white")
    barre_recherche.place(x='600',y='40')



    # fonction permettant de redimensionner la taille des images 
    def charge_redi_image(picture, largeur, hauteur):
        image = Image.open(picture)
        image_redi = image.resize((largeur, hauteur))
        photo_image = ImageTk.PhotoImage(image_redi)
        return photo_image



    # Specify the target width and height for the displayed images
    largeur = 50
    hauteur = 50

    # Assuming you have an image file named "example.png" in the current directory
    picture = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
    image_redi = charge_redi_image(picture, largeur, hauteur)

    picture2 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png"
    image_redi2 = charge_redi_image(picture2, largeur, hauteur)

    picture3 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
    image_redi3 = charge_redi_image(picture3, largeur, hauteur)





    #menu son aleatoire et zone de frame

    frame_menu_lateraleD = Frame(fenetre3, bg="purple", width=140, height=500)
    frame_barre_larteraleG = Frame(fenetre3, bg="purple", width=1400, height=600)

    frame_menu_son_milieu = Frame(fenetre3, bg="brown", width=780, height=800)

    frame_barre_horizontale = Frame(fenetre3, bg="pink", width=1400, height=500)




    # le bouton play next et previous
    play = Button(fenetre3,image=image_redi3,command=play_music)

    previous = Button(fenetre3,image=image_redi2)

    next = Button(fenetre3,image=image_redi)

        #inserer image sur un boutons  
        # Ajout de widgets à la fenêtre
    Label(fenetre3, text='researche bar', font=('Verdana', 15)).place(x='680',y='10')
    Label(fenetre3, text='Menu', font=('Verdana', 15)).place(x='10',y='20') 
        
    #le son partie 2

    # Bouton pour démarrer la musique
    # Barre de progression
    progress_var = IntVar()
    progress_bar = ttk.Progressbar(fenetre3, variable=progress_var, maximum=100, length=700)


        # Créer un objet photoimage pour utiliser l'image
    photo1 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo1 = photo1.subsample(2, 2) # redimensionne la taille de l'image

    photo2 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo2 = photo2.subsample(2, 2)

    photo3 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo3 = photo3.subsample(2, 2)
        #####
    photo4 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo4 = photo4.subsample(2, 2) # redimensionne la taille de l'image

    photo5 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo5 = photo5.subsample(2, 2)

    photo6 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo6 = photo6.subsample(2, 2)

    photo7 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo7 = photo7.subsample(2, 2) # redimensionne la taille de l'image

    photo8 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    Photo8 = photo8.subsample(2, 2)

    photo9 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    photo9 = photo9.subsample(2, 2)

    photo10 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
    photo10 = photo10.subsample(2, 2) # redimensionne la taille de l'image

    photo11 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
    photo11 = photo11.subsample(2, 2)

    photo12 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\2.png") 
    photo12 = photo12.subsample(2, 2)

    photo13 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
    photo13 = photo13.subsample(2, 2) # redimensionne la taille de l'image

    photo14 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
    photo14 = photo14.subsample(2, 2)

    photo15 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo15 = photo15.subsample(2, 2)

    photo16 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
    photo16 = photo16.subsample(2, 2)



        #boutons
    button1 = Button(fenetre3, text='menu', width=16, height=8, command=deuxieme_fenetre) 
    button1.place(x='50',y='50') 

    button2 = Button(fenetre,text='playlist', width=16, height=8, command=troisieme_fenetre)
    button2.place(x='50',y='220') 

    button3 = Button(fenetre,text='favoris',width=16, height=8, command=quatrieme_fenetre)
    button3.place(x='50',y='400') 

    son_menu1 = Button(fenetre3, image=photo4)
    son_menu2 = Button(fenetre3, image=photo5)
    son_menu3 = Button(fenetre3, image=photo6)
    son_menu4 = Button(fenetre3, image=photo7)
    son_menu5 = Button(fenetre3, image=photo7)
    son_menu6 = Button(fenetre3, image=photo9)
    son_menu7 = Button(fenetre3, image=photo10)
    son_menu8 = Button(fenetre3, image=photo11)
    son_menu9 = Button(fenetre3, image=photo12)
    son_menu10 = Button(fenetre3, image=photo13)
    son_menu11= Button(fenetre3, image=photo14)
    son_menu12= Button(fenetre3, image=photo15)
    son_barre_laterale= Button(fenetre3, image=photo16)
    son_barre_horizontale= Button(fenetre3, text="playlist", width=30, height=30)


    # emplacement de la barre de progression


    #son_menu1.grid(row=0,column=0)
    son_menu1.place(x='400', y='100')
    #son_menu2.grid(row=1,column=0)
    son_menu2.place(x='600', y='100')
    #son_menu3.grid(row=2,column=2)
    son_menu3.place(x='800', y='100')
    #son_menu4.grid(row=3,column=3)
    son_menu4.place(x='1000', y='100')
    #son_menu5.grid(row=0,column=0)
    son_menu5.place(x='400', y='250')
    #son_menu6.grid(row=0,column=0)
    son_menu6.place(x='600', y='250')
    #son_menu7.grid(row=1,column=1)
    son_menu7.place(x='800', y='250')
    #son_menu8.grid(row=2,column=2)
    son_menu8.place(x='1000', y='250')
    #son_menu9.grid(row=3,column=3)
    son_menu9.place(x='400', y='400')
    #son_menu10.grid(row=4,column=4)
    son_menu10.place(x='600', y='400')
    #son_menu11.grid(row=2,column=1)
    son_menu11.place(x='800', y='400')
    #son_menu12.grid(row=2,column=1)
    son_menu12.place(x='1000', y='400')

    son_barre_laterale.place(x='30', y='660')
    son_barre_horizontale.place(x='1170', y='90')

        #les boutons next .....
    previous.place(x=600, y=670)
    play.place(x=700, y=670)
    next.place(x=800, y=670)
    # emplacement de la barre de progression 
    progress_bar.place(x=400, y=750)

    frame_menu_lateraleD.place(x=40, y=30)
    frame_barre_larteraleG.place(x=1150, y=30)
    frame_menu_son_milieu.place(x=350, y=80)
    frame_barre_horizontale.place(x=0,y=650)





    # Lier la fonction de rappel à l'événement de fermeture de la deuxième fenêtre
    fenetre4.protocol("WM_DELETE_WINDOW", dans_fenetre3)
def dans_fenetre3():
    # Fermer la première fenêtre lorsque la seconde est fermée
    fenetre.destroy()


def quatrieme_fenetre():
    # Get the current position of the first window
    x = fenetre.winfo_x()
    y = fenetre.winfo_y()

    # Hide the first window
    fenetre.withdraw()

    # Create the second window
    global fenetre4
    fenetre4 = Toplevel(fenetre)
    fenetre4['bg'] = '#D46A6A' #bg = background
    fenetre4.geometry(f"{fenetre.winfo_width()}x{fenetre.winfo_height()}+{x}+{y}")
    fenetre4.title('SPOTI-FAIL')

    button = Button(fenetre4, text="retour", command=retour3)
    button.place(x=0,y=0)


    barre_recherche = Entry(fenetre4, width=50,borderwidth=8, bg="pink", fg="white")
    barre_recherche.place(x='600',y='40')


    barre_recherche = Entry(fenetre4, width=50,borderwidth=8, bg="pink", fg="white")
    barre_recherche.place(x='600',y='40')

    play_image = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png")
    play = Button(fenetre4,image=play_image, width=50,height=50)

    previous_image = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png")
    previous = Button(fenetre4,image=previous_image, width=50,height=50)

    next_image = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png")
    next = Button(fenetre4,image=next_image, width=50,height=50)
    previous.place(x=600, y=670)
    play.place(x=700, y=670)
    next.place(x=800, y=670)

        #boutons
    button1 = Button(fenetre4, text='menu', width=16, height=8, command=deuxieme_fenetre) 
    button1.place(x='50',y='50') 

    button2 = Button(fenetre4,text='playlist', width=16, height=8, command=troisieme_fenetre)
    button2.place(x='50',y='220') 

    button3 = Button(fenetre4,text='favoris',width=16, height=8, command=quatrieme_fenetre)
    button3.place(x='50',y='400') 
    
    #menu son aleatoire et zone de frame
    frame_menu_lateraleD = Frame(fenetre4, bg="purple", width=140, height=500)
    frame_barre_larteraleG = Frame(fenetre4, bg="purple", width=1400, height=600)
    frame_menu_son_milieu = Frame(fenetre4, bg="brown", width=780, height=800)
    frame_barre_horizontale = Frame(fenetre4, bg="pink", width=1400, height=500)
    son_barre_horizontale= Button(fenetre4, text="bla", width=30, height=30)


    
    son_barre_laterale= Button(fenetre4, image=photo16)
    son_barre_horizontale.place(x='1170', y='90')

    

    son_barre_laterale.place(x='30', y='660')
    frame_menu_lateraleD.place(x=40, y=30)
    frame_barre_larteraleG.place(x=1150, y=30)
    frame_menu_son_milieu.place(x=350, y=80)
    frame_barre_horizontale.place(x=0,y=650)


    # Lier la fonction de rappel à l'événement de fermeture de la deuxième fenêtre
    fenetre4.protocol("WM_DELETE_WINDOW", dans_fenetre4)
def dans_fenetre4():
    # Fermer la première fenêtre lorsque la seconde est fermée
    fenetre.destroy()


# sert a retourner dans l acceuil
def retour1():
    # Destroy the second window
    fenetre2.destroy()

    # Show the first window
    fenetre.deiconify()

def retour2():
    # Destroy the second window
    fenetre3.destroy()

    # Show the first window
    fenetre.deiconify()

def retour3():
    # Destroy the second window
    fenetre3.destroy()

    # Show the first window
    fenetre.deiconify()

#barre de progression du son

def update_progress():
    current_time = pygame.mixer.music.get_pos() // 1000  # Convert milliseconds to seconds
    progress_var.set(current_time)
    fenetre.after(1000, update_progress)

def play_music():
    pygame.mixer.music.load(r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\music\ene.mp3")  # Remplacez "votre_musique.mp3" par le chemin de votre fichier audio
    pygame.mixer.music.play()
    update_progress()

pygame.mixer.init()



# fenetre principale 
    
    
fenetre = Tk()
fenetre.geometry('1400x800')
fenetre.title('SPOTI-FAIL')
fenetre['bg'] = '#330019' #bg = background
fenetre.resizable(height=False, width= False) # on ne peut pa modifier ni la largeur et longueur

    #heritage voir comment ca marche 


    #barre de recherche

barre_recherche = Entry(fenetre, width=50,borderwidth=8, bg="pink", fg="white")
barre_recherche.place(x='600',y='40')



# fonction permettant de redimensionner la taille des images 
def charge_redi_image(picture, largeur, hauteur):
    image = Image.open(picture)
    image_redi = image.resize((largeur, hauteur))
    photo_image = ImageTk.PhotoImage(image_redi)
    return photo_image



# Specify the target width and height for the displayed images
largeur = 50
hauteur = 50

# Assuming you have an image file named "example.png" in the current directory
picture = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
image_redi = charge_redi_image(picture, largeur, hauteur)

picture2 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png"
image_redi2 = charge_redi_image(picture2, largeur, hauteur)

picture3 = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png"
image_redi3 = charge_redi_image(picture3, largeur, hauteur)





#menu son aleatoire et zone de frame

frame_menu_lateraleD = Frame(fenetre, bg="purple", width=140, height=500)
frame_barre_larteraleG = Frame(fenetre, bg="purple", width=1400, height=600)

frame_menu_son_milieu = Frame(fenetre, bg="brown", width=780, height=800)

frame_barre_horizontale = Frame(fenetre, bg="pink", width=1400, height=500)




# le bouton play next et previous
play = Button(fenetre,image=image_redi3,command=play_music)

previous = Button(fenetre,image=image_redi2)

next = Button(fenetre,image=image_redi)

    #inserer image sur un boutons  
    # Ajout de widgets à la fenêtre
Label(fenetre, text='researche bar', font=('Verdana', 15)).place(x='680',y='10')
Label(fenetre, text='Menu', font=('Verdana', 15)).place(x='10',y='20') 
    
#le son partie 2

# Bouton pour démarrer la musique
# Barre de progression
progress_var = IntVar()
progress_bar = ttk.Progressbar(fenetre, variable=progress_var, maximum=100, length=700)


    # Créer un objet photoimage pour utiliser l'image
photo1 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
photo1 = photo1.subsample(2, 2) # redimensionne la taille de l'image

photo2 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
photo2 = photo2.subsample(2, 2)

photo3 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
photo3 = photo3.subsample(2, 2)
    #####
photo4 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
photo4 = photo4.subsample(2, 2) # redimensionne la taille de l'image

photo5 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
photo5 = photo5.subsample(2, 2)

photo6 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
photo6 = photo6.subsample(2, 2)

photo7 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
photo7 = photo7.subsample(2, 2) # redimensionne la taille de l'image

photo8 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
Photo8 = photo8.subsample(2, 2)

photo9 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
photo9 = photo9.subsample(2, 2)

photo10 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\3.png") 
photo10 = photo10.subsample(2, 2) # redimensionne la taille de l'image

photo11 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
photo11 = photo11.subsample(2, 2)

photo12 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\2.png") 
photo12 = photo12.subsample(2, 2)

photo13 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\8.png") 
photo13 = photo13.subsample(2, 2) # redimensionne la taille de l'image

photo14 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\9.png") 
photo14 = photo14.subsample(2, 2)

photo15 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
photo15 = photo15.subsample(2, 2)

photo16 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\6.png") 
photo16 = photo16.subsample(2, 2)



    #boutons
button1 = Button(fenetre, text='menu', width=16, height=8, command=troisieme_fenetre) 
button1.place(x='50',y='50') 

button2 = Button(fenetre,text='playlist', width=16, height=8, command=troisieme_fenetre)
button2.place(x='50',y='220') 

button3 = Button(fenetre,text='favoris',width=16, height=8, command=quatrieme_fenetre)
button3.place(x='50',y='400') 

son_menu1 = Button(fenetre, image=photo4)
son_menu2 = Button(fenetre, image=photo5)
son_menu3 = Button(fenetre, image=photo6)
son_menu4 = Button(fenetre, image=photo7)
son_menu5 = Button(fenetre, image=photo7)
son_menu6 = Button(fenetre, image=photo9)
son_menu7 = Button(fenetre, image=photo10)
son_menu8 = Button(fenetre, image=photo11)
son_menu9 = Button(fenetre, image=photo12)
son_menu10 = Button(fenetre, image=photo13)
son_menu11= Button(fenetre, image=photo14)
son_menu12= Button(fenetre, image=photo15)
son_barre_laterale= Button(fenetre, image=photo16)
son_barre_horizontale= Button(fenetre, text="playlist", width=30, height=30)


# emplacement de la barre de progression


#son_menu1.grid(row=0,column=0)
son_menu1.place(x='400', y='100')
#son_menu2.grid(row=1,column=0)
son_menu2.place(x='600', y='100')
#son_menu3.grid(row=2,column=2)
son_menu3.place(x='800', y='100')
#son_menu4.grid(row=3,column=3)
son_menu4.place(x='1000', y='100')
#son_menu5.grid(row=0,column=0)
son_menu5.place(x='400', y='250')
#son_menu6.grid(row=0,column=0)
son_menu6.place(x='600', y='250')
#son_menu7.grid(row=1,column=1)
son_menu7.place(x='800', y='250')
#son_menu8.grid(row=2,column=2)
son_menu8.place(x='1000', y='250')
#son_menu9.grid(row=3,column=3)
son_menu9.place(x='400', y='400')
#son_menu10.grid(row=4,column=4)
son_menu10.place(x='600', y='400')
#son_menu11.grid(row=2,column=1)
son_menu11.place(x='800', y='400')
#son_menu12.grid(row=2,column=1)
son_menu12.place(x='1000', y='400')

son_barre_laterale.place(x='30', y='660')
son_barre_horizontale.place(x='1170', y='90')

    #les boutons next .....
previous.place(x=600, y=670)
play.place(x=700, y=670)
next.place(x=800, y=670)
# emplacement de la barre de progression 
progress_bar.place(x=400, y=750)

frame_menu_lateraleD.place(x=40, y=30)
frame_barre_larteraleG.place(x=1150, y=30)
frame_menu_son_milieu.place(x=350, y=80)
frame_barre_horizontale.place(x=0,y=650)


fenetre.mainloop() # creer une boucle infini comme dans pygame 


# on dirai que le grid n'est pas necessaire cai je crée juste des boutons pour l'instant











#cours
"""
buttonframe = Frame(fenetre)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky= W+E)

btn2 = Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=1, column=0, sticky= W+E)

btn3 = Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=2, column=0, sticky= W+E)

btn4 = Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=3, column=0, sticky= W+E)

buttonframe.pack(fill='x')"""




'''
textbox = Text(fenetre, font=('Arial', 16))
textbox.pack()'''


"""
#bouton
def fenetre2():
    fenetre = Tk()
    fenetre.geometry('1400x800')
    fenetre.title('SPOTI-FAIL')
    fenetre['bg'] = 'green' #bg = background
    fenetre.resizable(height=False, width= False) # on ne peut pa modifier ni la largeur et longueur

    label = Label(fenetre , text="bla bla bla", font =("verdana", 20,)) # designer le Label

    label.place(x='50', y='50') #meilleure facon de placer que Pack

    



    fenetre.mainloop() # creer une boucle infini comme dans pygame 

bouton = Button(fenetre, text="click me!", bg='blue', fg='white', command=fenetre2) #commmande permet d'executer un commande it's obvious
bouton.place(x='700', y='400')

#entree utilisateur

def funct():
    if ma_variable.get() == "emany" and mdp.get() == "muteb":
        exp1['text'] = 'BIENVENUE CHEF BG DE LA CALLE '     #get pour stocker la variable de l'utilisateur 
    else:
        exp1['text'] = 'BEURK ELLE EST PORTUGAISE'
ma_variable = StringVar()
mdp = StringVar()

exp1 = Label(fenetre , text="taper votre id et mdp", font =("verdana", 20,)) # designer le Label
exp1.pack()

entree1 = Entry(fenetre, textvariable= ma_variable)
entree1.pack()

entree2 = Entry(fenetre, textvariable= mdp)
entree2.pack()

bouton1 = Button(fenetre, text="click me!", bg='blue', fg='white', command=funct) #commmande permet d'executer un commande it's obvious
bouton1.pack()

c = Button(fenetre,text="Quit", font =("verdana", 10,),command=fenetre.quit)
c.place(x='1350', y='750')
"""




