"""ACCES VIA LES CODES DE CONNEXION A L'API DEEZER"""

client = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')

print("Welcome to deezer-python",
          "\nLes meilleures playlists vous attendent ici!!")
    
bdd=[]
bdd_playlist=[]
while True:

    print("\n Que voulez-vous?",
      "A - Des infos sur un artiste",
      "B - Générer une playlist",
      "C - Voir l'historique de vos recherches",
      "D - Quitter",
      sep="\n")
    action=input()
    
    while (action.lower()!="a" and action.lower()!="b" and action.lower()!="c" and action.lower()!="d"):
        action=input()
    
    if (action.lower() == "a"):
        nom_artiste=input("inserez le nom de l'artiste que vous souhaitez : ")
        #artiste=client.get_artist(input("inserez le nom de l'artiste que vous souhaitez : "))
        artiste=Artiste(nom_artiste)
        bdd.append(artiste.nom)
        print(artiste.presentation())
        #print(artiste, "Nombre de projets (singles inclus): ",len(artiste.get_albums()))
        print("Albums et leurs informations: \n")
        limite=artiste.nb_projets
        if (limite > 7):
            limite=7
        for j in range(limite):#infos sur les albums de l'artiste
            cpt=0
            somme =0
            alb=artiste.albums[j].get_tracks()
            if len(alb)>1: #no single
                for elt in range(len(alb)):
                    somme=somme+alb[elt].duration 
                    if "feat." in str(alb[elt]):
                        cpt+=1
                print("nom album: ",artiste.albums[j]," nombre de feats: ",cpt," nombre de sons: ",len(alb),
                      "durée en minutes: ",somme/60,'------------------------',sep="\n")
                    
    elif (action.lower() == "d"):
        break
    
    elif (action.lower() == "b"):
        print("Trouvons ensemble la playlist parfaite pour vous! Faites votre choix:",
          "a- Playlist à partir d'un artiste",
          "b - les morcceaux les plus écoutés en ce moment",
          "c - Playlist découverte à partir du top France",
          "d - Sorties récentes",
          sep="\n")
        pl=input()
        while (pl!="a" and pl!="b" and pl!="c" and pl!="d"):
            pl=input()
            
        if (pl == "a"):
            p_a=Playlist(1)
            a=input('choisissez votre artiste de départ : ')
            artiste_playlist=details_artiste(a)
            bdd.append(artiste_playlist.nom)
            print("Si vous aimez ",artiste_playlist.nom, ", vous aimerez forcément ces morceaux: \n")
            for j in range(5):
              print('------------------------')
              print(artiste_playlist.lien[j].name)
              print('------------------------')
              for i in range(3):
                print(artiste_playlist.lien[j].get_top()[i].title)
                p_a.add_son(artiste_playlist.lien[j].get_top()[i])#ajout du morceau a la playlist
                
            #nommer la playlist
            nom=input("Donnez un nom à votre playlist: ")
            p_a.nommer(nom)
            bdd_playlist.append(p_a.nom)
        elif (pl == "b"):
            client2 = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')
            id=1767932902#top 25 FRANCE
            p_b=deezer_playlist(id)
            p_b.generer()
            for i in range(9):
              print(p_b.sons[i],"\n")
            #nommer la playlist
            nom=input("Donnez un nom à votre playlist: ")
            p_b.nommer(nom)
            bdd_playlist.append(p_b.nom)
            
        elif (pl == "c"):
            client2 = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')
            id=1767932902#top 25 FRANCE
            p_c=deezer_playlist(id)
            p_c.generer()
            p_c.artistes_de_la_playlist()
            for i in range(3):
              print(p_c.artistes[i],"\n")
              for j in range(3):
                print('------------------------')
            
                for k in range(1):
                  print(p_c.artistes[i].get_related()[j].name,": ", p_c.artistes[i].get_related()[j].get_top()[k].title)
                print('------------------------')
            #nommer la playlist
            nom=input("Donnez un nom à votre playlist: ")
            p_c.nommer(nom)
            bdd_playlist.append(p_c.nom)
        else:
            print("Ces albums récents pourraient vous plaire; jetez-y un coup d'oeil! \n")
            client2 = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')
            id=1767932902#top 25 FRANCE
            p_d=deezer_playlist(id)
            p_d.generer()
            p_d.artistes_de_la_playlist()
            for i in range(7):
              print(p_d.artistes[i])
              print(p_d.artistes[i].get_albums()[0])
              print(p_d.artistes[i].get_albums()[0].release_date)
            #nommer la playlist
            nom=input("Donnez un nom à votre playlist: ")
            p_d.nommer(nom)
            bdd_playlist.append(p_d.nom)
    
    else:
        if (len(bdd)==0):
            print("aucun artiste encore recherché. Qu'attendez-vous!?")
        else:
            print("Liste des artistes recherchés:")
            for obj in bdd:
                print(obj,"\n")
        
        if (len(bdd_playlist)==0):
            print("aucune playlist pour l'instant. commencez dès à présent!")
        else:
            print("Vos playlists déja créées:")
            for obj in bdd_playlist:
                print(obj,"\n")
    
    
    
