import pygame
from Plateau import Plateau
from Joueur import Joueur
from random import randint


from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes



def chiffre_aleat():
        
        """
        genere un chiffre aleatoire
        """
        
        n  = randint(1, 6)
        return n 


def affiche_fenetre(p : Plateau, images : dict, taille_case : int, j : Joueur):

    """
    permet d'afficher la fenetre
    """
    
    for ligne in range(12):
            for col in range(12):
                lettre = p.plateau[ligne][col]
                if lettre in images:
                    image = images[lettre]
                    fenetre.blit(image, (col * taille_case, ligne * taille_case))

    joueur_image = images['j1']
    player_x, player_y = j.position_joueur
    fenetre.blit(joueur_image, (player_x * taille_case, player_y * taille_case))



def deplacer_joueur(j : Joueur, ancienne_position, mouvement_possible, result):

    """
    permet de deplacer le joueur sur le plateau
    """

    print(result)

    nouvelle_position = ancienne_position + result

    if nouvelle_position >= len(mouvement_possible):
        print("Le résultat est trop grand.")
    else:
        new_x, new_y = mouvement_possible[nouvelle_position]
        ancienne_position = nouvelle_position
        j.position_joueur = [new_y, new_x]

    return(ancienne_position)



def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)
 
def level_menu():
    mainmenu._open(level)



pygame.init()


surface = pygame.display.set_mode((600, 400))
 
 
mainmenu = pygame_menu.Menu('Bienvenu', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Nane : ', default='username')
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
 
loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 200, )
 
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 
update_loading = pygame.USEREVENT + 0



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
    'j1' : pygame.transform.scale(pygame.image.load('img/1.png'), (taille_case, taille_case)),
    'j2' : pygame.transform.scale(pygame.image.load('img/2.png'), (taille_case, taille_case)),

    '1' : pygame.transform.scale(pygame.image.load('img/1.png'), (taille_case, taille_case)),
    '2' : pygame.transform.scale(pygame.image.load('img/2.png'), (taille_case, taille_case)),
    '3' : pygame.transform.scale(pygame.image.load('img/3.png'), (taille_case, taille_case)),
    '4' : pygame.transform.scale(pygame.image.load('img/4.png'), (taille_case, taille_case)),
    '5' : pygame.transform.scale(pygame.image.load('img/5.png'), (taille_case, taille_case)),
    '6' : pygame.transform.scale(pygame.image.load('img/6.png'), (taille_case, taille_case)),
}

# titre de la fenetre
pygame.display.set_caption("Notre jeu déchire !")

# instanciation des classes
p = Plateau(images, largeur_fenetre, hauteur_fenetre, taille_case) # instancie la class Plateau
j = p.joueur

# ancienne position de mon joueur
ancienne_position = 0

# mouvements possible sur le plateau
mouvement_possible = [
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [10, 2], [10, 3], [9, 3], [8, 3], [7, 3], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10], [3, 10], [3, 9], [3, 8], [3, 7], [3, 6], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [10, 9], [10, 8], [9, 8], [8, 8], [7, 8], [7, 7], [7, 6], [7, 5], [8, 5], [9, 5], [10, 5], [10, 6]
    ]

# création d'une fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

fenetre.fill((255,255,255)) # couleur de la fenetre

# Tpolice de texte
ma_police = pygame.font.Font(None, 36)


# lance le code
running = True
while running:
    events = pygame.event.get()
    for event in events:

    # for event in pygame.event.get():
        if event.type == pygame.QUIT: # verifie si pygame n'a pas été quitté
            running = False

        if event.type == pygame.KEYDOWN:

            # modifie l'image de la case quand le dé est lancé
            if event.key == pygame.K_DOWN: 
                
                # mouvement(j, p)
                result = chiffre_aleat()
                ancienne_position = deplacer_joueur(j, ancienne_position, mouvement_possible, result)

                # remet la couleur de fond pour de cacher l'ancienne phrase de resultat
                fenetre.fill((255, 255, 255))

                if result == 1 :
                    texte_de = ma_police.render("vous avez fait 1", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
                if result == 2 :
                    texte_de = ma_police.render("vous avez fait 2", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
                if result == 3 :
                    texte_de = ma_police.render("vous avez fait 3", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
                if result == 4 :
                    texte_de = ma_police.render("vous avez fait 4", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
                if result == 5 :
                    texte_de = ma_police.render("vous avez fait 5", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
                if result == 6 :
                    texte_de = ma_police.render("vous avez fait 6", True, (0, 0, 0))
                    fenetre.blit(texte_de, (800, 700))
        
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
                    
    # textes         
    fenetre.blit(ma_police.render("Appuyer sur la flèche du", True, (0,0,0)), (800, 100))
    fenetre.blit(ma_police.render("bas pour lancer le dé !", True, (0,0,0)), (800, 150))
    affiche_fenetre(p, images, taille_case, j)
    pygame.display.update()

pygame.quit()