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
        


    
