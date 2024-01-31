import pygame
import random
import string

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Charger les mots depuis le fichier "mots.txt"
with open("mots.txt", "r") as file:
    mots = file.readlines()
    mot = random.choice(mots).strip().upper()

# Lettres correctement devinées
lettres_trouvees = []

# Paramètres du pendu
PICS_PENDU = [pygame.image.load("pendu1.png"), pygame.image.load("pendu2.png"), pygame.image.load("pendu3.png"), pygame.image.load("pendu4.png"), pygame.image.load("pendu5.png"), pygame.image.load("pendu6.png"), pygame.image.load("pendu7.png"), pygame.image.load("pendu8.png")]
pic_pendu = 0

# Police
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Fonction pour dessiner le jeu
def dessiner_jeu():
    win.fill(WHITE)
    # Dessiner le mot
    affichage_mot = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage_mot += lettre + " "
        else:
            affichage_mot += "_ "
    texte_mot = WORD_FONT.render(affichage_mot, 1, BLACK)
    win.blit(texte_mot, (400, 200))
    # Dessiner le titre
    texte_titre = TITLE_FONT.render("JEU DU PENDU", 1, BLACK)
    win.blit(texte_titre, (WIDTH/2 - texte_titre.get_width()/2, 20))
    # Dessiner les lettres
    for i, lettre in enumerate(string.ascii_uppercase):
        x = 20 + 40 * (i % 13)
        y = 300 + 50 * (i // 13)
        lettre_ = LETTER_FONT.render(lettre, 1, BLACK)
        win.blit(lettre_, (x, y))
    # Dessiner le pendu
    win.blit(PICS_PENDU[pic_pendu], (150, 100))
    pygame.display.update()

def main():
    global pic_pendu

    # Paramètres
    lettres_esssayees = []
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    # Boucle principale
    while run:
        clock.tick(FPS)
        dessiner_jeu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Récupérer la position de la souris
                m_x, m_y = pygame.mouse.get_pos()
                for i, lettre in enumerate(string.ascii_uppercase):
                    x = 20 + 40 * (i % 13)
                    y = 300 + 50 * (i // 13)
                    if x < m_x < x + 40 and y < m_y < y + 40:
                        if lettre not in lettres_esssayees:
                            lettres_esssayees.append(lettre)
                            if lettre in mot:
                                lettres_trouvees.append(lettre)
                                if len(lettres_trouvees) == len(set(mot)):
                                    # Le joueur a gagné
                                    print("Félicitations ! Vous avez trouvé le mot : " + mot)
                                    run = False
                            else:
                                pic_pendu += 1
                                if pic_pendu == 6:
                                    # Le joueur a perdu
                                    print("Désolé, vous avez été pendu. Le mot était : " + mot)
                                    run = False
    pygame.quit()


# Lancer le jeu
main()