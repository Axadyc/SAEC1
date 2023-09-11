import pygame

# Créer une classe Carte pour gérer la carte du jeu
class Carte:
    def __init__(self, largeur, hauteur, taille_case, images):
        
        self.largeur = largeur  # Nombre de colonnes de tuiles
        self.hauteur = hauteur  # Nombre de lignes de tuiles
        self.taille_case = taille_case  # Taille d'une tuile en pixels
        self.images = images  # Dictionnaire associant les lettres aux images
        self.carte_data = []  # Une liste pour stocker les données de la carte

    def charger_carte(self, fichier_carte):
        """Charge une carte à partir de ma_carte.txt"""
        
        with open(fichier_carte, "r") as fichier:  # Ouvre le fichier carte en mode lecture    
            for ligne in fichier: # Pour chaque ligne du fichier
                ligne_carte = []
                for lettre in ligne: # Pour chaque lettre de la ligne
                    if lettre in self.images: # Si la lettre est dans le dictionnaire des images
                        image = pygame.transform.scale(self.images[lettre], (self.taille_case, self.taille_case)) # Met l'inmage à la taille de la tuile grace à transform.scale
                        ligne_carte.append(image)
                
                self.carte_data.append(ligne_carte)# Ajoute l'image à la ligne de tuiles de la carte

    def dessiner(self, fenetre):
        """Dessine la carte sur la fenêtre pygame."""
        
        for y, ligne in enumerate(self.carte_data): # Pour chaque ligne de la carte (enumerate sert a bien parcourir la liste)
            for x, case in enumerate(ligne):# Pour chaque tuile de la ligne
                position_x = x * self.taille_case 
                position_y = y * self.taille_case
                
                fenetre.blit(case, (position_x, position_y)) # Dessine l'image sur la case calculée


if __name__ == "__main__":

    pygame.init()  
    largeur_fenetre = 640  # Largeur de la fenêtre en pixels 
    hauteur_fenetre = 640  # Hauteur de la fenêtre en pixels
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))  # Créer une fenêtre pygame

    # Dictionnaire d'images
    images = {
        's': pygame.image.load('img/solsaloon.png'),
        'w': pygame.image.load('img/solcour.jpeg'),
        'c': pygame.image.load('img/cactus.png'),
        'r' : pygame.image.load('img/solranch.jpg'),
        'm' : pygame.image.load('img/solmine.jpg'),
        '1' : pygame.image.load('img/d1.png'),
        '2' : pygame.image.load('img/d2.png'),
        '3' : pygame.image.load('img/d3.png'),
        '4' : pygame.image.load('img/d4.png'),
        'n' : pygame.image.load('img/espace.png'),
    }

    # # Redimensionne les image pour qu'elles ne dépassent pas 64x64 pixels
    # for lettre, image in images.items():
    #     images[lettre] = pygame.transform.scale(image, (64, 64))

    # Créer une instance de la classe Carte
    carte = Carte(20, 20, 32, images)

    # image de fond de la fenetre
    fond = pygame.image.load('img/lesbg.jpg')
    fond = pygame.transform.scale(fond, (largeur_fenetre, hauteur_fenetre)) # redimenssionne la taille de l'image en fonction de celle de la fenetre

    # Charger la carte à partir de ma_carte.txt
    carte.charger_carte('plateau/ma_carte.txt')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fenetre.blit(fond, (0,0)) # image de fond 
        carte.dessiner(fenetre) 

        pygame.display.update()  # Met à jour la fenêtre

    pygame.quit() 

# cccccccccccccccccccc
# ccmmmmmmmmmmmmmmmmcc
# cwcmmmmmmmmmmmmmmcrc
# cwwcmmmmmmmmmmmmcrrc
# cwwwcmmmmmmmmmmcrrrc
# cwwwwcmmmmmmmmcrrrrc
# cwwwwwcmmmmmmcrrrrrc
# cwwwwwwcmmmmcrrrrrrc
# cwwwwwwwcmmcrrrrrrrc
# cwwwwwwwwccrrrrrrrrc
# cwwwwwwwwccrrrrrrrrc
# cwwwwwwwcsscrrrrrrrc
# cwwwwwwcsssscrrrrrrc
# cwwwwwcsssssscrrrrrc
# cwwwwcsssssssscrrrrc
# cwwwcsssssssssscrrrc
# cwwcsssssssssssscrrc
# cwcsssssssssssssscrc
# ccssssssssssssssss14
# cccccccccccccccccc23
