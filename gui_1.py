# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:38:11 2020

D'après http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_parallelisation/thread.html

@author: jk
"""
import tkinter as TK
import threading, time, random, copy
from datetime import datetime
from random import choice
from collections import deque

prio = [True, False]
# un dictionnaire pour les types et billets
prefixes = ['A','B','C','D','E','F','G','H','J','K','Z']
dico = {'spec1':['A','B','C'],
        'spec2':['D','E','F'],
        'normal':['G', 'H','J','K','Z']}

liste_cas = deque()

suivi_ticket = dict.fromkeys(prefixes,0)

class Cas:
    def __init__(self, type, prio, t): #type= spec1, spec2 .. ou normal; prio = true or false
        self.type = type
        self.prio = prio
        self.date_creation = datetime.now()
        self.date_reclass = self.date_creation
        self.debut_traitm = self.date_creation
        self.fin_traitm = self.date_creation
        self.ticket_num = t
        
    def en_string(self):
        print ("type : " + self.type +
        "\n" + "prio : " + str(self.prio) +
        "\n" + "ticket : " + self.ticket_num +
        "\n" + "cree le : " + str(self.date_creation) +
        "\n" + "reclass le : " + str(self.date_reclass) +
        "\n" + "debut_tr : " + str(self.debut_traitm) +
        "\n" + "fin_tr : " + str(self.fin_traitm))

# définition du thread
class MonThread (threading.Thread) :
    def __init__ (self, win, res) :
        threading.Thread.__init__ (self)
        self.win = win  
        self.res = res

    def run (self) :
        ajoute_cas()    
        self.win.event_generate ("<<thread_fini>>", x = h)

class AjouteCas (threading.Thread) :
    def __init__ (self, win) :
        threading.Thread.__init__ (self)
        self.win = win  
        self.res = res

    def run (self) :
        ajoute_cas()


thread_resultat = []

def lance_thread () :
    text .config (text = "Tx1 thread démarré")
    text2.config (text = "Tx2 thread démarré")
    bouton.config (state = TK.DISABLED)
# on lance le thread
    m = MonThread (root, thread_resultat)
    m.start ()

def thread_fini_fonction (e) :
    print("la fenêtre sait que le thread est fini")
# on change la légende de la zone de texte
    text .config (text = "thread fini + résultat " + str (thread_resultat))
    text2.config (text = "thread fini + résultat (e.x) " + str (e.x))
# on réactive le bouton de façon à pouvoir lancer un autre thread
    bouton.config (state = TK.NORMAL)

def cas_aleat ():
    le_type = random.choice(list(dico.keys()))
    la_prio = random.choice(prio)
    #//TODO genere ticket sequentiel
    le_num_ticket = seq_ticket(le_type)
    cas = Cas(le_type, la_prio, le_num_ticket)   
    print(cas.en_string())
    return cas
                  
def ajoute_cas ():
    liste_cas.append(cas_aleat())
    text2.config (text = "liste contient " + str(len(liste_cas)))
    s = stats()
    text3.config( text = str(s) )

  
def stats():
    statis = {'s1':0,'s2':0,'n':0,'p':0}
    for object in liste_cas:
        if object.type == 'spec1':
            statis['s1'] += 1
        if object.type == 'spec2':
            statis['s2'] += 1
        if object.type == 'normal':
           statis['n'] += 1
        if object.prio == True:
           statis['p'] += 1
    return statis   
                
def seq_ticket(le_type):
    prefixe = random.choice(list(dico[le_type]))
    num = suivi_ticket[prefixe] + 1
    le_num = prefixe + str(num)
    suivi_ticket[prefixe] = num
    print(suivi_ticket)
    return(le_num)

guichets = {}
def genere_guichet():
    max_num = 4
  
    for i in range(1, max_num):
        guichets['G' + str(i)] = ['s1'] #TODO // attribution des guichets se fera par gui.
    print (guichets)
    
def pick(g):
    print(g)
    c = liste_cas.popleft()
    print (c.en_string())
    #//TODO call manager pour classer par priorites
    
    
    

genere_guichet()
# on crée la fenêtre
root   = TK.Tk ()
bouton = TK.Button (root, text = "thread départ", command = lance_thread)
text   = TK.Label (root, text = "rien")
text2  = TK.Label (root, text = "rien")
text3 = TK.Label(root, text = 'resultats')
bouton2 = TK.Button (root, text = "Ajouter un cas", command = ajoute_cas)
print (bouton2.nametowidget(bouton2))
bouton.pack ()
bouton2.pack ()
text.pack ()
text2.pack ()
text3.pack ()
for g in guichets.keys():
    v = TK.Button(root, text = g, command = lambda: pick(g))
    v.pack()   
    print (v.nametowidget(v))


# on associe une fonction à un événement <<thread_fini>> propre au programme
root.bind ("<<thread_fini>>", thread_fini_fonction)

# on active la boucle principale de message
root.mainloop ()

'''
Me créer un classe "cas" et une structure pour contenir des cas.

class Cas:
    def __init__(self, type, prio): #type= spec1, spec2 .. ou normal; prio = true or false
        self.type = type
        self.prio = prio
        self.date_creation = date.now()
        self.date_reclass = date_creation
        self.debut_traitm = date_creation
        self.fin_traitm = date_creation
     
règles d'opération:
    
    1- gardien à l'entrée accueille visiteur et insère son cas dans le système (le systeme cree 3 files) (il lui donne un billet numéroté)
       ce gardien effectue un filtrage pour établir si le client est prioritaire ou alors s'il a besoin de passer
       à un guichet spécialisé (supposition: certains guichets ne traitent que des cas spécifiques) donc le cas est créé avec 
       type et prio + données chrono. il affiche le total et le type  des cas passés devant lui.
       
       ?DEQUE: envoyer les normaux à droite et les specs à gauche : S1,S2,Sx, NNNNNN -> chrono
       
    2- TODO: générer un numéro de billet l'affecter à cas. (spec1 = [A ou B ou C], spec2 = [D ou E ou F], normal = G à Z; tous suivis de 0 à 99)
    
    3- manager: lit les x files (app a un nombre dynamique de guichets et de spécialisations)
    
        manager trie une liste résultante (A) OU alors (B) les n listes restent telles quelles et les guichets doivent regarder les listes différents pour choisir leur cas
        
        A: une seule liste: cas Sx placés en tête de liste par ordre prio.sx.chrono. ensuite les cas normaux par ordre chrono.
        
        manager invoqué/notifié à chaque ajout de cas: il place le dernier cas entré. Raison de faire un thread ?
    
    4- guichet: le guichet a des caractéristiques dynamiques de traitement de cas: il a les propriétés Sx e/ou N, ce qui veut dire qu'il peut piger dans l'ordre :
        Sx, Sx+1, finalement N. Donc, il doit lire la liste et popper le premier cas qu'il peut exécuter (affiche le num sur gui).
        Pour la demo: thread de traitement t = random(10 à 30 secs + next(g)).
        
        un guichet peut être fermé manuellement.
        
        un guichet peut changer de compétence (à l'état fermé).
               
        
        
    5- chaque accès aux listes bloque cette liste (lock?).

    6- le manager fait des stats de traitement par guichet.        
        
'''



























