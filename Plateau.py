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
    largeur_fenetre = 1152  # Largeur de la fenêtre en pixels 
    hauteur_fenetre = 768  # Hauteur de la fenêtre en pixels
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))  # Créer une fenêtre pygame

    # Dictionnaire d'images
    images = {
        'v': pygame.image.load('python/tank.png'),
        'w': pygame.image.load('python/fond.jpg'),
        'r': pygame.image.load('python/ciel.jpg')
    }

    # # Redimensionne les image pour qu'elles ne dépassent pas 64x64 pixels
    # for lettre, image in images.items():
    #     images[lettre] = pygame.transform.scale(image, (64, 64))

    # Créer une instance de la classe Carte
    carte = Carte(18, 12, 64, images)

    # Charger la carte à partir de ma_carte.txt
    carte.charger_carte('python/ma_carte.txt')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fenetre.fill((0, 0, 0)) # couleir de fond noir
        carte.dessiner(fenetre) 

        pygame.display.update()  # Met à jour la fenêtre

    pygame.quit() 