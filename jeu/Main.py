import pygame
from Plateau import Plateau
from Joueur import Joueur
from random import randint

def chiffre_aleat():
    
    n  = randint(1, 6)
    return n 

def affiche_fenetre(p : Plateau, images : dict, taille_case : int, j : Joueur):
    for ligne in range(12):
            for col in range(12):
                lettre = p.plateau[ligne][col]
                if lettre in images:
                    image = images[lettre]
                    fenetre.blit(image, (col * taille_case, ligne * taille_case))

    joueur_image = images['j']
    player_x, player_y = j.position_joueur
    fenetre.blit(joueur_image, (player_x * taille_case, player_y * taille_case))


def mouvement(j : Joueur, p : Plateau):

    player_x, player_y = j.position_joueur
    result = chiffre_aleat()
    print(result)
    if result == 1:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 1
    if result == 2:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 2
    if result == 3:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 3
    if result == 4:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 4
    if result == 5:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 5
    if result == 6:
        if p.plateau[player_y + 1][player_x] == 'p':
            j.position_joueur[1] += 6

pygame.init()

# dimensions de la fenêtre
largeur_fenetre= 1100
hauteur_fenetre = 768

# dimensions d'une case
taille_case = 64

# dictionnaire des images
images = {
    'b' : pygame.transform.scale(pygame.image.load('img/espace.png'), (taille_case, taille_case)),
    'p' : pygame.transform.scale(pygame.image.load('img/solcour.jpeg'), (taille_case, taille_case)),
    'm' : pygame.transform.scale(pygame.image.load('img/solmine.jpg'), (taille_case, taille_case)),
    'r' : pygame.transform.scale(pygame.image.load('img/solranch.jpg'), (taille_case, taille_case)),
    'j' : pygame.transform.scale(pygame.image.load('img/1.png'), (taille_case, taille_case)),

    '1' : pygame.transform.scale(pygame.image.load('img/1.png'), (taille_case, taille_case)),
    '2' : pygame.transform.scale(pygame.image.load('img/2.png'), (taille_case, taille_case)),
    '3' : pygame.transform.scale(pygame.image.load('img/3.png'), (taille_case, taille_case)),
    '4' : pygame.transform.scale(pygame.image.load('img/4.png'), (taille_case, taille_case)),
    '5' : pygame.transform.scale(pygame.image.load('img/5.png'), (taille_case, taille_case)),
    '6' : pygame.transform.scale(pygame.image.load('img/6.png'), (taille_case, taille_case)),
}

# titre de la fenetre
pygame.display.set_caption("Notre jeu déchire !")


p = Plateau(images, largeur_fenetre, hauteur_fenetre, taille_case) # instancie la class Plateau
j = p.joueur

# création d'une fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

fenetre.fill((255,255,255)) # couleur de la fenetre

# lance le code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # verifie si pygame n'a pas été quitté
            running = False

        if event.type == pygame.KEYDOWN:

            # modifie l'image de la case quand le dé est lancé
            if event.key == pygame.K_DOWN: 
                mouvement(j, p)


    affiche_fenetre(p, images, taille_case, j)
    pygame.display.update()

pygame.quit()