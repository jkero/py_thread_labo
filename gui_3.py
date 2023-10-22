# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:38:11 2020

D'après http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_parallelisation/thread.html

@author: jk
"""
import tkinter as TK
import threading, time, random, copy
from datetime import datetime
from random import choices
from collections import deque

NUMGUICHETS = 4
threadLock = threading.Lock()
prio = [True, False]
# un dictionnaire pour les types et billets
prefixes = ['A','B','C','D','E','F','G','H','J','K','Z']
dico = {'spec1':['A','B','C'],
        'spec2':['D','E','F'],
        'normal':['G', 'H','J','K','Z']}

#autre moyen de classer les cas à la saisie

dico2 = {'prio':['spec1','spec2','normal'],
         'base':['spec1','spec2','normal']
    }

competences = ['prio', 'spec1', 'spec2', 'normal']

thread_resultat = []

liste_cas = [[[], [], []], [[], [], []]]
'''format de cette liste basé sur prio et types #rangee 0 = prio, rangee 1 = base
    [0][0].append -> tous les prioritaires de type spec1
    [0][1].append -> tous les prioritaires de type spec2
    [0][3].append -> tous les prioritaires de type normal
    [1]][0].append -> tous les base de type spec1
    [1][1].append -> tous les base de type spec2
    [1][3].append -> tous les base de type normal   
'''
liste_guichets = []#liste des objets guichets travailler avec index - num guichet
liste_thread = [] #contient les thread guichet pour controler

suivi_ticket = dict.fromkeys(prefixes,0)

class Cas:
    '''
    Contient les objetcs cas passés par le gardien (et insérés par le système)
    '''
    def __init__(self, type, prio, t): #type= spec1, spec2 .. ou normal; prio = true or false
        self.type = type
        self.prio = prio
        self.date_creation = datetime.now()
        self.date_reclass = self.date_creation
        self.debut_traitm = self.date_creation
        self.fin_traitm = self.date_creation
        self.ticket_num = t
        self.traite = False
        
    def en_string(self):
        '''
        READABLE FORMAT
        '''
        print ("type : " + self.type +
        "\t" + "prio : " + str(self.prio) +
        "\t" + "ticket : " + self.ticket_num +
        "\t" + "cree le : " + str(self.date_creation) +
        "\t" + "reclass le : " + str(self.date_reclass) +
        "\t" + "debut_tr : " + str(self.debut_traitm) +
        "\t" + "fin_tr : " + str(self.fin_traitm))
        
class Guichet:
    def __init__(self, num):
        self.num = num
        self.competences = self.genere_competences()
        self.ouverture = datetime.now()
        self.historique = []#liste de cas traités
        
        
    def historique(self):
        print ("cas traités : \n" )
        for cas in self.historique:
            print ("\n type : " + self.type +
        "\t" + "prio : " + str(self.prio) +
        "\t" + "ticket : " + self.ticket_num +
        "\t" + "cree le : " + str(self.date_creation) +
        "\n" + "reclass le : " + str(self.date_reclass) +
        "\t" + "debut_tr : " + str(self.debut_traitm) +
        "\t" + "fin_tr : " + str(self.fin_traitm))
        
    def genere_competences(self):
        #creer random n competences pour ce guichet
        a=set(choices([competences[0],''],k=1) + choices(competences[-3:],k=random.randint(1,2)))
        return list(a)
        
        
# définition du thread
# class MonThread (threading.Thread) :
#     def __init__ (self, win, res) :
#         threading.Thread.__init__ (self)
#         self.win = win  
#         self.res = res

#     def run (self) :
#         ajoute_cas()    
#         self.win.event_generate ("<<thread_fini>>", x = h)

class ThreadAjouteCas (threading.Thread) :
    def __init__ (self, win,res) :
        threading.Thread.__init__ (self)
        self.win = win  


    def run (self) :
        cpt = 0
        for i in range (1, 15) :
            h = random.randint (1,2)
            time.sleep (h)
            threadLock.acquire()
            ajoute_cas()
            print(" --------------- cas "+str(i) + " delai " + str(h))
            threadLock.release()
            cpt = i
        self.win.event_generate ("<<thread_fini>>", x = i)
        
class ThreadGuichetOuvert(threading.Thread) :
    def __init__ (self, win, guichet, texte) :
        threading.Thread.__init__ (self)
        self.win = win  
        self.guichet = guichet
        self.name = "G" + str(self.guichet.num)
        self.label = texte

    def run (self) :
        h = random.randint (5,9)
        time.sleep (h)
        check = 0
        run = 0
        while self.compte_cas() > 0 and check <= run:
            threadLock.acquire()
            pige_prochain_cas(self.guichet)
            print(" --------------- guichet " +self.name + " lancé ...")
            run = self.compte_cas()
            check+=1
            threadLock.release()
            print(" --------------- guichet " +self.name + " fermé ...")     
            time.sleep(random.randint(1,3))
            
        self.label.config (text = " --------------- guichet " + self.name + " fermé ...")
        s = stats()
        text3.config( text = str(s) )
        
    def stop_me(self):
        self.running = False
        print(" --------------- guichet " +self.name + " fermé ...")
    
    def compte_cas(self):
        c = len(liste_cas[0][0]) +\
            len(liste_cas[0][1]) +\
            len(liste_cas[0][2]) +\
            len(liste_cas[1][0]) +\
            len(liste_cas[1][1]) +\
            len(liste_cas[1][2])                    
        return c


def lance_thread () :
    text .config (text = "Tx1 thread démarré")
    text2.config (text = "Tx2 thread démarré")
    bouton.config (state = TK.DISABLED)
# on lance le thread
    m = ThreadAjouteCas(root,thread_resultat)
    m.start ()

def thread_fini_fonction (e) :
    print("la fenêtre sait que le thread est fini")
# on change la légende de la zone de texte
    text .config (text = "thread fini + résultat " + str (thread_resultat))
    text2.config (text = "thread fini + résultat (e.x) " + str (e.x))
# on réactive le bouton de façon à pouvoir lancer un autre thread
    bouton.config (state = TK.NORMAL)
    print(stats())

def cas_aleat ():
    le_type = random.choice(list(dico.keys()))
    la_prio = random.choice(prio)
    #//TODO genere ticket sequentiel
    le_num_ticket = seq_ticket(le_type)
    cas = Cas(le_type, la_prio, le_num_ticket)   
    print(cas.en_string())
    return cas
                  
def ajoute_cas ():
    c = cas_aleat()
    if c.prio == True:
        if c.type == 'spec1':
            liste_cas[0][0].append(c);
        if c.type == 'spec2':
            liste_cas[0][1].append(c);
        if c.type == 'normal':
            liste_cas[0][2].append(c);
    else:
        if c.type == 'spec1':
            liste_cas[1][0].append(c);
        if c.type == 'spec2':
            liste_cas[1][1].append(c);
        if c.type == 'normal':
            liste_cas[1][2].append(c);
    
    s = stats()
    text3.config( text = str(s) )
#TODO: apres avoir généré le type de cas, il faut le classe dans une des listes sp1 sp2 ou normal
# ensuite : appeler manager pour trier les 3 listes en 1 seule.
#un guichet examine la liste: si self


def stats():
    text2.config(text = "liste contient " +
                 str((
                     len(liste_cas[0][0]) + 
                     len(liste_cas[0][1]) +
                     len(liste_cas[0][2]) +
                     len(liste_cas[1][0]) + 
                     len(liste_cas[1][1]) +
                     len(liste_cas[1][2])
                     )))
    statis = {'ps1':0,'ps2':0,'pn':0,'s1':0,'s2':0,'n':0}
    statis['ps1'] += len(liste_cas[0][0])
    statis['ps2'] += len(liste_cas[0][1])
    statis['pn'] +=  len(liste_cas[0][2])
    statis['s1'] += len(liste_cas[1][0])
    statis['s2'] += len(liste_cas[1][1])
    statis['n'] += len(liste_cas[1][2])
    return statis   

def stats_histo():
    statis = {'ps1':0,'ps2':0,'pn':0,'s1':0,'s2':0,'n':0}
    statis['ps1'] += len(liste_cas[0][0])
    statis['ps2'] += len(liste_cas[0][1])
    statis['pn'] +=  len(liste_cas[0][2])
    statis['s1'] += len(liste_cas[1][0])
    statis['s2'] += len(liste_cas[1][1])
    statis['n'] += len(liste_cas[1][2])
    
    print(statis)   

    for guichet in liste_guichets:
        print("G" + str(guichet.num) + " ("+ str(guichet.competences)  + ")")
        for cas_histo in guichet.historique:
            print("\t" + cas_histo.ticket_num)
            print("\t" + str(cas_histo.prio) + "/" + cas_histo.type)
                
def seq_ticket(le_type):
    prefixe = random.choice(list(dico[le_type]))
    num = suivi_ticket[prefixe] + 1
    le_num = prefixe + str(num)
    suivi_ticket[prefixe] = num
    print(suivi_ticket)
    return(le_num)

    
def pick(g, t, n):
    guichet = None
    for i in liste_guichets: #affecter un guichet specifique
        if i.num == n:
            guichet = i
    th = ThreadGuichetOuvert(root,guichet,t)
    t.config(text = g['text'] + " ouvert")
    th.start()              
    #passer object guichet à thread_guichet
    
    
def pige_prochain_cas(obj_guichet):#il faut la cote 'prio' pour traiter des cas prio (mais pas exclusivement les prio) -- if 2e ligne
    print("\n\nG" + str(obj_guichet.num) + " ("+ str(obj_guichet.competences) +") pige dans la liste")
    if ('prio' in obj_guichet.competences and traite_cas(obj_guichet,0,"prio")) or traite_cas(obj_guichet,1,"base"):
        print("\tG" + str(obj_guichet.num) + " a trouvé un cas")
    else:
        print("\tG" + str(obj_guichet.num) + " n'a rien trouvé")
    

def traite_cas(obj_guichet, cpt_type, passe):
    done = False
    print(stats())
    print("  **** cherche cas " + passe)
    for groupe_type in range(0,len(liste_cas[cpt_type])):
        print("     groupe " + str(groupe_type))
        if len(liste_cas[cpt_type][groupe_type]) > 0: #il y a des prio
            print("         **** explore types")
            for cas in liste_cas[cpt_type][groupe_type]:
                print(cas.type)
                if cas.type in obj_guichet.competences:
                    print("       **** trouve un cas de sa competence")
                    affiche_t.config(text = "        ! ! G" + str(obj_guichet.num) + " traite " + cas.ticket_num)
                    print("        ! ! G" + str(obj_guichet.num) + " traite " + cas.ticket_num)
                    cas.debut_traitm = datetime.now()
                    cas.traite = True
                    obj_guichet.historique.append(cas)
                    print(stats())
                    liste_cas[cpt_type][groupe_type].remove(cas)
                    print(stats())
                    done = True
                    break;
            if done:
                break;
            else:
                print(" **** G" + str(obj_guichet.num) + " ne trouve rien dans " + passe + " ou est incompétent :" + str(obj_guichet.competences))
    return done                
             
    
def ajoute_guichets():
    for i in range(1, NUMGUICHETS +1):         
        g = Guichet(i)
        print("cree guichet" + str(g.num) + " (" + str(g.competences) + ")") 
        liste_guichets.append(g)

def contient(la_liste, le_nom):
    res = False
    for i in la_liste:
        if i.name == le_nom:
            res = i
            break;
    return res
# on crée la fenêtre
if __name__ == '__main__':
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
    
    #TOTO comment automatiserceci? Noms des objets sont inaccessibles -> mettre dans parent frame?
    #NUMGUICHETS = 4 final?
    g1 = TK.Button(root, text = "G1", command = lambda: pick(g1, g1_t, 1))
    
    
    
    g1.pack() 
    g1_t = TK.Label (root, text = "fermé")
    g1_t.pack()
    
    g2 = TK.Button(root, text = "G2", command = lambda:  pick(g2, g2_t, 2))
    g2.pack() 
    g2_t = TK.Label (root, text = "fermé")
    g2_t.pack()
    
    g3 = TK.Button(root, text = "G3", command = lambda:  pick(g3, g3_t, 3))
    g3.pack() 
    g3_t = TK.Label (root, text = "fermé")
    g3_t.pack()
    
    g4 = TK.Button(root, text = "G4", command = lambda:  pick(g4, g4_t, 4))
    g4.pack() 
    g4_t = TK.Label (root, text = "fermé")
    g4_t.pack()
    
    affiche_t = TK.Label (root, text = "aucun cas en traitement")
    affiche_t.pack()
    
    
    ajoute_guichets()
    
    #TODO classe guicher avec prop compétences
    # trouver moyen de référencer objets dynamiques (v et t dans loop??)    
    
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



























