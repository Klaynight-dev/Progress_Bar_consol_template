from random import *
import sys
import time

class Progressall():
    # Sous-classe pour une barre de progression basée sur le nombre d'éléments à importer
    class allprogress():
        # Fonction pour afficher une barre de progression en fonction du nombre d'éléments
        def progressbar(it, prefix="", size=60, file=sys.stdout):
            count = len(it)
            # Fonction pour afficher visuellement la progression
            def show(j):
                x = int(size*j/count)
                file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, " "*(size-x), j, count))
                file.flush()
                file.write("\r")
            show(0)
            # Boucle pour simuler le chargement des éléments avec différentes temporisations
            for i, item in enumerate(it):
                yield item
                show(i+1)
                file.write("\r")
            file.flush()
        
        time_set=-2
        
        # Simulation de l'importation des éléments avec des temporisations différentes à chaque étape
        for i in progressbar(range(15), "Importation des éléments : ", 40):
            if time_set <= 1:
                time.sleep(0.3)
                time_set = time_set + 1
            if time_set <= 10:
                time.sleep(0.1)
                time_set = time_set + 1
            if time_set <= 15:
                time.sleep(0.2)
                time_set = time_set + 1
        time.sleep(1)

    # Sous-classe pour une barre de progression générique
    class ProgressBar:
        '''
        Barre de progression générique
        '''
        def __init__ (self, valmax, maxbar, title):
            # Modification : ajuster la valeur maximale de la barre et la longueur maximale de la barre
            if valmax == 0:
                valmax = 1
            if maxbar > 200:
                maxbar = 200
            self.valmax = valmax
            self.maxbar = maxbar
            self.title = title
        
        # Mettre à jour la barre de progression avec une valeur spécifique
        def update(self, val):
            import sys
            # Formatage
            if val > self.valmax:
                val = self.valmax
            
            # Calcul du pourcentage et du remplissage de la barre
            perc = round((float(val) / float(self.valmax)) * 100)
            scale = 100.0 / float(self.maxbar)
            bar = int(perc / scale)
      
            # Affichage de la barre de progression
            out = '\r %20s [%s%s] %3d %%' % (self.title, '=' * bar, ' ' * (self.maxbar - bar), perc)
            sys.stdout.write(out)

    # Création d'une instance de la classe ProgressBar
    Bar = ProgressBar(100, 60, 'Chargement :')
    time_set = -5

    # Simulation d'une barre de progression générique avec différentes temporisations
    for i in range(101):
        Bar.update(i)
        if time_set <= 1:
            time.sleep(0.3)
            time_set = time_set + 1
        if time_set <= 10:
            time.sleep(0.1)
            time_set = time_set + 1
        if time_set <= 15:
            time.sleep(0.2)
            time_set = time_set + 1
        if time_set <= 75:
            time.sleep(0.1)
            time_set = time_set + 1
        if time_set <= 95:
            time.sleep(0.01)
            time_set = time_set + 1