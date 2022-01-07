INSTALLATION DE LA LIBRAIRIE NECESSAIRE AU BON FONCTIONNEMENT DU PROGRAMME

pip install deezer-python

import deezer as dp

"""ACCES VIA LES CODES DE CONNEXION A L'API DEEZER"""

client = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')

nom_artiste=input("inserez le nom de l'artiste que vous souhaitez : ")
artiste=client.get_artist(nom_artiste)
print(artiste)

"""TRAVAIL SUR ARTISTES"""

albums_de_lartiste=artiste.get_albums()[0].get_tracks()
print(albums_de_lartiste)

for j in range(len(artiste.get_albums())):
    
    cpt=0
    alb=artiste.get_albums()[j].get_tracks()
    if len(alb)>1: #no single
        for elt in range(len(alb)):
            #print(alb[elt]) 
            if "feat." in str(alb[elt]):
                cpt+=1
        print("nom album: ",artiste.get_albums()[j]," nombre de feats: ",cpt," nombre de sons: ",len(alb))

nbr=artiste.get_albums()
for i in range (len(nbr)):
  somme =0
  for j in range(len(nbr[i].get_tracks())):
    if len(nbr[i].get_tracks())<2:
      print("C'est un single")
    else:
      
      somme=somme+nbr[i].get_tracks()[j].duration
  print("l'album",nbr[i],"dure",(somme/60),"minutes")

a=input('choisissez votre artiste de départ : ')
artiste=client.get_artist(a)
for j in artiste.get_related():
  print('------------------------')
  print(j.name)
  print('------------------------')
  for i in range(5):
    print(j.get_top()[i].title)

"""**TRAVAIL SUR PLAYLIST **"""

client2 = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')

liste=[]
id=1767932902
for i in range(len(client2.get_playlist(id).get_tracks())):
  liste.append(client2.get_playlist(id).get_tracks()[i].get_artist())
  print(client2.get_playlist(id).get_tracks()[i].get_artist())

"""CREATION DE PLAYLIST EN LIEN AVEC LES ARTISTES DU TOP France 2021

"""

l=[]
for i in range(len(client2.get_playlist(id).get_tracks())):
  print(client2.get_playlist(id).get_tracks()[i].get_artist())
  print('Playlist Découverte')
  for j in client2.get_playlist(id).get_tracks()[i].get_artist().get_related():
    print('------------------------')
    print(j.name)
    print('------------------------')
    for k in range(len(j.get_top())):
      print(j.get_top()[k].title)
      
    
    

###print(len(client2.get_playlist(id).get_tracks()[i].get_artist().get_related()))

"""TOP 5 DES SONS DES ARTISTES DU TOP 25 FRANCE"""

for i in range(len(client2.get_playlist(id).get_tracks())):
  print(client2.get_playlist(id).get_tracks()[i].get_artist())
  print(client2.get_playlist(id).get_tracks()[i].get_artist().get_top())

"""ALBUM LE PLUS Recent DES ARTISTES DU TOP 25"""

for i in range(len(client2.get_playlist(id).get_tracks())):
  print(client2.get_playlist(id).get_tracks()[i].get_artist())
  print(client2.get_playlist(id).get_tracks()[i].get_artist().get_albums()[0])
  print(client2.get_playlist(id).get_tracks()[i].get_artist().get_albums()[0].release_date)

"""GENERATEUR DE PLAYLIST"""

a=input('choisissez votre artiste de départ : ')
artiste=client.get_artist(a)
for j in artiste.get_related():
  print('------------------------')
  print(j.name)
  print('------------------------')
  for i in range(5):
    print(j.get_top()[i].title)
