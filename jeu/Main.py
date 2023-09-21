import pygame
from Plateau import Plateau

class Main():

    pygame.init()

    # titre de la fenetre
    pygame.display.set_caption("Notre jeu déchire !")

    # dimensions de la fenêtre
    largeur_fenetre= 884
    hauteur_fenetre = 748

    # dimensions d'une case
    taille_case = 34

    # dictionnaire des images
    images = {
        'b' : pygame.transform.scale(pygame.image.load('img/espace.png'), (taille_case, taille_case)),
        'p' : pygame.transform.scale(pygame.image.load('img/solcour.jpeg'), (taille_case, taille_case)),
        'm' : pygame.transform.scale(pygame.image.load('img/solmine.jpg'), (taille_case, taille_case)),
        'r' : pygame.transform.scale(pygame.image.load('img/solranch.jpg'), (taille_case, taille_case)),
        'j' : pygame.transform.scale(pygame.image.load('img/lesbg.jpg'), (taille_case, taille_case)),

        '1' : pygame.transform.scale(pygame.image.load('img/1.png'), (taille_case, taille_case)),
        '2' : pygame.transform.scale(pygame.image.load('img/2.png'), (taille_case, taille_case)),
        '3' : pygame.transform.scale(pygame.image.load('img/3.png'), (taille_case, taille_case)),
        '4' : pygame.transform.scale(pygame.image.load('img/4.png'), (taille_case, taille_case)),
        '5' : pygame.transform.scale(pygame.image.load('img/5.png'), (taille_case, taille_case)),
        '6' : pygame.transform.scale(pygame.image.load('img/6.png'), (taille_case, taille_case)),
    }

    p = Plateau(images, largeur_fenetre, hauteur_fenetre, taille_case) # instancie la class Plateau

    # lance le code
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # verifie si pygame n'a pas été quitté
                running = False

            if event.type == pygame.KEYDOWN:

                # modifie l'image de la case quand le dé est lancé
                if event.key == pygame.K_a: 
                    result = p.chiffre_aleat()
                    p.modifier_case(0, 0, result)

                # modifie la position du joueur en fonction des touché préssées
                elif event.key == pygame.K_LEFT:  # gauche
                    player_x, player_y = p.position_joueur # récupère la position du joueur
                    if p.plateau[player_y][player_x - 1] != 'b': # vérifie si la case de gauche n'est pas la lettre b dans la liste
                        p.position_joueur[0] -= 1
                
                elif event.key == pygame.K_RIGHT:   # droite
                    player_x, player_y = p.position_joueur
                    if p.plateau[player_y][player_x + 1] != 'b':
                        p.position_joueur[0] += 1

                elif event.key == pygame.K_UP:  # haut
                    player_x, player_y = p.position_joueur
                    if p.plateau[player_y - 1][player_x] != 'b':
                        p.position_joueur[1] -= 1
                        
                elif event.key == pygame.K_DOWN:    # bas
                    player_x, player_y = p.position_joueur
                    if p.plateau[player_y + 1][player_x] != 'b':
                        p.position_joueur[1] += 1

        p.affiche_fenetre()
        pygame.display.update()

    pygame.quit()