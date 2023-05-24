import pygame
import random
import time



"""
======================================================

Classes

======================================================
"""

class Jeu:
    def __init__ (self, LARGEUR_GRILLE, HAUTEUR_GRILLE, TAILLE_CARRE):
        self.LARGEUR_GRILLE = LARGEUR_GRILLE
        self.HAUTEUR_GRILLE = HAUTEUR_GRILLE
        self.TAILLE_CARRE = TAILLE_CARRE
        
        
        # Initialisation de pygame
        pygame.init()

        # Création de la fenêtre
        self.fenetre = pygame.display.set_mode((LARGEUR_GRILLE * TAILLE_CARRE, HAUTEUR_GRILLE * TAILLE_CARRE))

        self.serpent = Serpent([(LARGEUR_GRILLE // 2, HAUTEUR_GRILLE // 2)], "droite", VERT, LARGEUR_GRILLE, HAUTEUR_GRILLE)
        self.pomme = nouvelle_pomme()
        
    def play (self):
        time.sleep (3)
        # Boucle principale
        quitter = False
        while not quitter:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitter = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.serpent.changer_direction("haut")
                    elif event.key == pygame.K_DOWN:
                        self.serpent.changer_direction("bas")
                    elif event.key == pygame.K_LEFT:
                        self.serpent.changer_direction("gauche")
                    elif event.key == pygame.K_RIGHT:
                        self.serpent.changer_direction("droite")

            # Mise à jour de l'état du jeu
            self.serpent.bouger()
            self.serpent.sortieGrille ()
            self.serpent.mordQueue()
            
            if self.serpent.gameOver:
                quitter = True
            
            if self.serpent.positions[0] == self.pomme.position:
                self.serpent.positions.append(self.pomme.position)
                self.pomme = nouvelle_pomme()
            
            if quitter:
                time.sleep (1)
                pygame.quit()
                
            # Dessin du jeu
            self.fenetre.fill(NOIR)
            self.dessiner_grille()
            self.serpent.dessiner(self.fenetre)
            self.pomme.dessiner(self.fenetre)
            pygame.display.flip()
            time.sleep(0.1)

    # Fonction qui dessine la grille
    def dessiner_grille(self):
        for x in range(self.LARGEUR_GRILLE):
            for y in range(self.HAUTEUR_GRILLE):
                pygame.draw.rect(self.fenetre, BLANC, (x * TAILLE_CARRE, y * TAILLE_CARRE, TAILLE_CARRE, TAILLE_CARRE), 1)
        
# Classe Serpent
class Serpent:
    def __init__(self, positions, direction, couleur, largeurGrille, hauteurGrille):
        self.positions = positions
        self.direction = direction
        self.couleur = couleur
        self.gameOver = False
        self.largeurGrille = largeurGrille
        self.hauteurGrille = hauteurGrille

    def dessiner(self, surface):
        for x, y in self.positions:
            pygame.draw.rect(surface, self.couleur, (x * TAILLE_CARRE, y * TAILLE_CARRE, TAILLE_CARRE, TAILLE_CARRE))

    def bouger(self):
        x, y = self.positions[0]
        if self.direction == "haut":
            y -= 1
        elif self.direction == "bas":
            y += 1
        elif self.direction == "gauche":
            x -= 1
        elif self.direction == "droite":
            x += 1
        self.positions = [(x, y)] + self.positions[:-1]
        print (self.positions)
        
    def changer_direction(self, direction):
        self.direction = direction
        
    def mordQueue (self):
        for i in range (len (self.positions)):
            j = i
            while j < len(self.positions)-1:
                j=j+1
                if self.positions [i] == self.positions[j]:
                    self.gameOver = True
                
    def sortieGrille(self):
        pos = self.positions[0]
        
        if pos[0] < 0 or pos[0] > self.largeurGrille:
            self.gameOver = True
            
        elif pos[1] < 0 or pos[1] > self.hauteurGrille:
            self.gameOver = True


# Classe Pomme
class Pomme:
    def __init__(self, position, couleur):
        self.position = position
        self.couleur = couleur

    def dessiner(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, self.couleur, (x * TAILLE_CARRE, y * TAILLE_CARRE, TAILLE_CARRE, TAILLE_CARRE))

"""
======================================================

Fonctions

======================================================
"""

# Fonction qui génère aléatoirement une nouvelle pomme sur la grille
def nouvelle_pomme():
    x = random.randint(0, LARGEUR_GRILLE - 1)
    y = random.randint(0, HAUTEUR_GRILLE - 1)
    return Pomme((x, y), ROUGE)


"""
======================================================

Fonctions

======================================================
"""

# Largeur et hauteur de la grille (en nombre de carrés)
LARGEUR_GRILLE = 80
HAUTEUR_GRILLE = 40

# Taille d'un carré (en pixels)
TAILLE_CARRE = 20

# Couleurs (triplets RGB)
NOIR = (0, 0, 0)
BLANC = (130, 130, 130)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Création du serpent et de la pomme
Game = Jeu (LARGEUR_GRILLE, HAUTEUR_GRILLE, TAILLE_CARRE)
Game.play ()




