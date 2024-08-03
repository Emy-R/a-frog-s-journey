from fenetre_jeu import *
import pygame
import pygame.freetype

nom_personnage = """PHRYGE"""
dico_histoire = {
    "introduction": [
        """Oh, salut ! Tiens, tu sais ce que sont les Jeux Olymiques ? Laisse nous t'éclairer !""",
        """Il y a très longtemps, dans un pays lointain appelé la Grèce antique, les gens adoraient""",
        """leurs dieux et déesses à travers toutes sortes de célébrations. Mais les Jeux Olympiques,""",
        """c'était la crème de la crème ! C'était comme la plus grosse fête sportive de l'année !""",
        """   """,
        """Imaginez-vous, les Grecs se réunissaient à Olympie, une petite ville tranquille, pour des""",
        """jeux incroyables en l'honneur de Zeus, le roi des dieux. Ils voulaient montrer à Zeus qu'ils""",
        """étaient en super forme et qu'ils savaient faire des trucs dingues comme courir super vite ou""",
        """lancer des trucs super loin !"""
        """   """
        """À l'époque, les Jeux Olympiques étaient un peu comme un mélange de compétition sportive et de""",
        """festival de la bonne humeur. Tout le monde laissait de côté les disputes et les histoires de""",
        """familles pour venir s'amuser ensemble."""
        """   """
        """Hé, Phryge, tu te souviens de la course de stadion ? C'était la première course des Jeux, et""",
        """les mecs couraient comme des dingues sur une distance qui correspondait à un stade. D'où le nom,""",
        """"stadion" ! Ça devait être trop cool à voir !"""
        """   """
        """Ouais, Pari, et tu te rappelles de Philippidès ? Ce gars-là, il était une vraie légende ! Il a couru""",
        """de Marathon à Athènes, soit plus de 40 kilomètres, pour annoncer la victoire des Grecs. Imagine le""",
        """cardio qu'il devait avoir !"""
        """   """
        """Au fil du temps, les Jeux Olympiques ont traversé des hauts et des bas, mais ils ont toujours gardé cet""",
        """esprit de fair-play et d'unité entre les peuples. En 1896, un super-héros appelé Pierre de Coubertin a""",
        """ramené les Jeux Olympiques à la vie à Athènes, et depuis, c'est devenu le rendez-vous incontournable de""",
        """tous les sportifs du monde !"""
        """   """
        """Et voilà comment les Jeux Olympiques sont devenus cette méga-fête sportive qu'on connaît aujourd'hui !""",
        """Paris 2024 est prêt à accueillir la prochaine édition, et on a hâte de vous y voir !"""
    ],
    "chapitre_1": [
        """..."""
    ],
    "chapitre_2": [
        """..."""
    ],
    "chapitre_4": [
        """..."""
    ]
}

fond_ecran_intro = "Picture1.png"
fond_ecran_jeu_chap = "Picture1.png"

police_ecriture = pygame.freetype.Font("story_font.otf", 32)
police_nom_perso = pygame.freetype.Font("story_font.otf", 40)

clock = pygame.time.Clock()

def story(chap):
    if chap == 1:
        menu_fond = pygame.image.load(fond_ecran_intro).convert()
    else:
        menu_fond = pygame.image.load(fond_ecran_jeu_chap).convert()
    menu_fond = pygame.transform.scale(menu_fond, (1920, 1080))
    screen.blit(menu_fond, (0, 0))
    pygame.display.flip()

    pygame.display.flip()
    longueur = 0
    text_number = 0

    running = True  # Variable pour contrôler la boucle principale
    while running:
        screen.blit(menu_fond, (0, 0))
        clock.tick(20)
        rect_nom, rect = police_nom_perso_FONT.render(nom_personnage, (0, 0, 0))
        screen.blit(rect_nom, (125, 665))
        if text_number == 0:
            text_surface0, rect = police_ecriture_FONT.render(story_dict["story_" + str(chap)][text_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            longueur += 1
        if longueur >= len(story_dict["story_" + str(chap)][text_number]) and text_number < len(story_dict["story_" + str(chap)]) - 1:
            text_number += 1
            longueur = 0
        if text_number >= 1:
            text_surface0, rect = police_ecriture_FONT.render(story_dict["story_" + str(chap)][text_number - 1], (0, 0, 0))
            text_surface1, rect = police_ecriture_FONT.render(story_dict["story_" + str(chap)][text_number][0:longueur], (0, 0, 0))
            screen.blit(text_surface0, (150, 725))
            screen.blit(text_surface1, (150, 775))
            longueur += 1
        pygame.display.flip()

