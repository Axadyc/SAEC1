import pygame
from random import randint
from Joueur import Joueur



class Plateau:

    def __init__(self, images, largeur_fenetre, hauteur_fenetre, taille_case):


        self.images = images 
        self.largeur_fenetre = largeur_fenetre
        self.hauteur_fenetre = hauteur_fenetre
        self.taille_case = taille_case

        # position du joueur
        self.joueur = Joueur()

        # charge l'image de fond et redimensionne-la a la taille de la fenetre
        # self. ackground = pygame.image.load('img/plateau.png')
        # self. ackground = pygame.transform.scale(self. ackground, (largeur_fenetre, hauteur_fenetre)) # redimenssionne l'image de fond aux dimensions de la fenetre

        # création du plateau de jeu sous forme de liste
        self.plateau = [
                    [' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ','p',' ','p','p','p','p','p','p','p','p',' '],
                    [' ','p',' ','p','m',' ',' ',' ',' ','r','p',' '],
                    [' ','p',' ','p',' ','p','p','p','p','p','p',' '],
                    [' ','p',' ','p',' ','p','m',' ',' ',' ',' ',' '],
                    [' ','p',' ','p',' ','p','p','p','p','p','p',' '],
                    [' ','p',' ','p',' ',' ',' ',' ',' ','r','p',' '],
                    [' ','p',' ','p',' ','p','p','p','p',' ','p',' '],
                    [' ','p',' ','p',' ','p','m',' ','p',' ','p',' '],
                    [' ','p','m','p',' ','p',' ',' ','p','m','p',' '],
                    [' ','p','p','p',' ','p','p',' ','p','p','p',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        

    # def affiche_fenetre(self):

        
        # parcoure le plateau et affiche les images correspondantes aux lettres
        # for ligne in range(12):
        #     for col in range(12):
        #         lettre = self.plateau[ligne][col]
        #         if lettre in self.images:
        #             image = self.images[lettre]
        #             fenetre. lit(image, (col * self.taille_case, ligne * self.taille_case))

        # joueur_image = self.images['j']
        # player_x, player_y = self.joueur.position_joueur
        # fenetre. lit(joueur_image, (player_x * self.taille_case, player_y * self.taille_case))



    # pas encore mis au point

    def chiffre_aleat(self):
        
        n  = randint(1, 6)
        return n 

    def modifier_case(self, x, y, result):
        "Permet de modifier une case en fonction du chiffre renvoyée par le dé"

        if result == 1 :
            self.plateau[y][x] = self.images['2']
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

    
