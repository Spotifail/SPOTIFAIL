from tkinter import *
from PIL import Image, ImageTk

# parametres de la fenetre 

#code

fenetre = Tk()
fenetre.geometry('1400x800')
fenetre.title('SPOTI-FAIL')
fenetre['bg'] = '#D46A6A' #bg = background
fenetre.resizable(height=False, width= False) # on ne peut pa modifier ni la largeur et longueur

#heritage voir comment ca marche 


#barre de recherche
"""
def funct():
    if ma_variable.get() == "emany" and mdp.get() == "muteb":
        exp1['text'] = 'BIENVENUE CHEF BG DE LA CALLE '     #get pour stocker la variable de l'utilisateur 
    else:
        exp1['text'] = 'BEURK ELLE EST PORTUGAISE'
"""
barre_recherche = Entry(fenetre, width=50,borderwidth=8, bg="pink", fg="white")
barre_recherche.place(x='600',y='40')





#menu son aleatoire et zone de frame

frame_menu_lateraleD = Frame(fenetre, bg="purple", width=140, height=500)
frame_barre_larteraleG = Frame(fenetre, bg="purple", width=1400, height=600)

frame_menu_son_milieu = Frame(fenetre, bg="gray", width=780, height=8)

frame_barre_horizontale = Frame(fenetre, bg="pink", width=1400, height=500)






#inserer image sur un boutons  
# Ajout de widgets à la fenêtre
Label(fenetre, text='researche bar', font=('Verdana', 15)).place(x='680',y='10') 
  
#les bouton play, previous, next 
def clickplay():
    pass # veux faire en sorte que quand ca appuie ca change avec l'image du pause

#redimentionner image 

play_image_pil = Image.open(r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\play.png")

# Resize the image to your desired size
desired_width = 50
desired_height = 50
play_image_resized = play_image_pil.resize((desired_width, desired_height))
# Convert the resized image to a Tkinter PhotoImage
play_image = ImageTk.PhotoImage(play_image_resized)

play = Button(fenetre,image=play_image, width=50,height=50)

previous_image = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\previous.png")
previous = Button(fenetre,image=previous_image)

next_image = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\next,previous, pause\next.png")
next = Button(fenetre,image=next_image)

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

photo8 = PhotoImage(file = r"C:\Users\EMANY MAKAP\Desktop\PROJEET N2\image\random\7.png") 
photo8 = photo8.subsample(2, 2)

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

#boutons
button1 = Button(fenetre, image=photo1) 
button1.place(x='50',y='50') 

button2 = Button(fenetre, image=photo2)
button2.place(x='50',y='220') 

button3 = Button(fenetre, image=photo3)
button3.place(x='50',y='400') 

son_menu1 = Button(fenetre, image=photo4)
son_menu2 = Button(fenetre, image=photo5)
son_menu3 = Button(fenetre, image=photo6)
son_menu4 = Button(fenetre, image=photo7)
son_menu5 = Button(fenetre, image=photo8)
son_menu6 = Button(fenetre, image=photo9)
son_menu7 = Button(fenetre, image=photo10)
son_menu8 = Button(fenetre, image=photo11)
son_menu9 = Button(fenetre, image=photo12)
son_menu10 = Button(fenetre, image=photo13)
son_menu11= Button(fenetre, image=photo14)
son_menu12= Button(fenetre, image=photo15)


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

#les boutons next .....
play.place(x=750, y=100)

frame_menu_lateraleD.place(x=40, y=30)
frame_barre_larteraleG.place(x=1150, y=30)
frame_menu_son_milieu.place(x=350, y=8)
frame_barre_horizontale.place(x=0,y=650)

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



fenetre.mainloop() # creer une boucle infini comme dans pygame 

