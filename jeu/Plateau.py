import pygame
from random import randint


class Plateau:

    def __init__(self, images, largeur_fenetre, hauteur_fenetre, taille_case):

        self.images = images 
        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre
        self.taille_case = taille_case

        # départ du joueur
        self.position_joueur = [1, 0]

        # création d'une fenêtre Pygame
        self.fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

        # charge l'image de fond et redimensionne-la a la taille de la fenetre
        self.background = pygame.image.load('img/plateau.png')
        self.background = pygame.transform.scale(self.background, (largeur_fenetre, hauteur_fenetre)) # redimenssionne l'image de fond aux dimensions de la fenetre

        # création du plateau de jeu sous forme de liste
        self.plateau = [
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','b','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','','','','']]
    
        

    def affiche_fenetre(self):

        # affiche l'image de fond
        self.fenetre.blit(self.background, (0, 0)) # blit sert a lire et placer une image dans la fenetre

        # parcoure le plateau et affiche les images correspondantes aux lettres
        for ligne in range(22):
            for col in range(26):
                lettre = self.plateau[ligne][col]
                if lettre in self.images:
                    image = self.images[lettre]
                    self.fenetre.blit(image, (col * self.taille_case, ligne * self.taille_case))

        joueur_image = self.images['j']
        player_x, player_y = self.position_joueur
        self.fenetre.blit(joueur_image, (player_x * self.taille_case, player_y * self.taille_case))




    # pas encore mis au point

    def modifier_case(self, x, y, result):
        "Permet de modifier une case en fonction du chiffre renvoyée par le dé"

        if result == 1 :
            self.plateau[y][x] = self.images['1'] # Change la lettre/chiffre du plateau par 1 a la position demandée
        elif result == 2 : 
            self.plateau[y][x] = self.images['2']
        elif result == 3 : 
            self.plateau[y][x] = self.images['3']
        elif result == 4 : 
            self.plateau[y][x] = self.images['4']
        elif result == 5 : 
            self.plateau[y][x] = self.images['5']
        elif result == 6 : 
            self.plateau[y][x] = self.images['6']


    def chiffre_aleat(self):
        
        nb = randint(1, 6)
        return nb
