# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:38:35 2020

@author: jk

prototype de file d'attente genre Bureau des véhicules. 

Class cas
    un client arrive, déclare ses besoins. param: (prio | !prio)(normal | spec) = 4 types.

Class gardien
    c'est le gardien qui entre les cas dans la file appropriée (ou via proxy ou autre pattern)

Class guichet
    consommateurs autonomes de cas, threads? popout les cas des files (ou une file résultante gérée par pattern x).
    il y a des guichets traitant une ou l'autre des 4 possibilités de types selon leur création, ou plusieurs à la fois.

Class fileSpec
    essentiellement une structure contenant les cas. ordonné chrono.

Class fileNormal
    essentiellement une structure contenant les cas. ordonné chrono.

Class manager 
    ouvre les guichets et les configure selon état des files.
    
    gestion des 3 files et conversion en une seule?
    
        file unique: pattern strategy au moment de décider quel cas choisir:
        1- cas prio
        2- cas spec
        3-temps d'attente? -> si un cas normal a attendu  > x temps, alors modifier/ajouter guichet pour traiter cas normal
        4- si file vide alors modifier guichet spécifique?
        
        5 files autonomes? -> iter notifier après temps max > x.
    

"""

import threading, time, random, copy

# définition du thread
class MonThread (threading.Thread) :
    def __init__ (self, win, res) :
        threading.Thread.__init__ (self)
        self.win = win  # on mémorise une référence sur la fenêtre
        self.res = res

    def run (self) :
        for i in range (0, 10) :
            n = random.randint (0,5)
            print("thread %d delai %d" % (i, n))
            time.sleep (n)

          # afin que le thread retourne un résultat
          # self.res désigne thread_resultat qui reçoit un nombre de plus
        h = random.randint (0,100)
        self.res.append (h)

          # on lance un événement <<thread_fini>> à la fenêtre principale
          # pour lui dire que le thread est fini, l'événement est ensuite
          # géré par la boucle principale de messages
          # on peut transmettre également le résultat lors de l'envoi du message
          # en utilisant un attribut de la classe Event pour son propre compte
        self.win.event_generate ("<<thread_fini>>", x = h)

thread_resultat = []
tic = 0
toc = 0

def lance_thread () :
    global thread_resultat
    global tic
      # fonction appelée lors de la pression du bouton
      # on change la légnde de la zone de texte
    text .config (text = "thread démarré")
    text2.config (text = "thread démarré")
      # on désactive le bouton pour éviter de lancer deux threads en même temps
    bouton.config (state = TK.DISABLED)
      # on lance le thread
    m = MonThread (root, thread_resultat)
    tic = time.perf_counter()
    print(tic)
    m.start ()


def thread_fini_fonction (e) :
    global thread_resultat
    global toc
    # fonction appelée lorsque le thread est fini
    print("la fenêtre sait que le thread est fini")
      # on change la légende de la zone de texte
    toc = time.perf_counter()
    print(toc)
    print(toc - tic)
    text .config (text = "thread fini + résultat " + str (thread_resultat))
    text2.config (text = "t. exéc. = %s" % str (round(toc - tic,4)))
      # on réactive le bouton de façon à pouvoir lancer un autre thread
    bouton.config (state = TK.NORMAL)


import tkinter as TK

# on crée la fenêtre
root   = TK.Tk ()
bouton = TK.Button (root, text = "thread départ", command = lance_thread)
text   = TK.Label (root, text = "rien")
text2  = TK.Label (root, text = "rien")
bouton.pack ()
text.pack ()
text2.pack ()

# on associe une fonction à un événement <<thread_fini>> propre au programme
root.bind ("<<thread_fini>>", thread_fini_fonction)

# on active la boucle principale de message
root.mainloop ()