import deezer as dp
client = dp.Client(app_id='mickaeltsimi@yahoo.fr', app_secret='Mickael1')

class Artiste:
  def __init__(self,nom):
    self.nom=client.get_artist(nom)
    self.nb_projets= len(self.nom.get_albums())
    self.albums=self.nom.get_albums()
  def presentation(self):
        return f"{self.nom} avec {self.nb_projets} projets (singles inclus)"
  

class details_artiste(Artiste):
  def __init__(self,nom):
    super().__init__(nom=nom)
    self.top=self.nom.get_top()
    self.lien=self.nom.get_related()
  
    


class Playlist:
    def __init__(self,nom=" "):
      self.nom=nom
      self.sons=[]
    def add_son(self, son):
      self.sons.append(son)
    def affichage(self):
        print(self.nom)
        for elt in self.sons:
            print(elt, "\n")
    def nommer(self,name):
        self.nom=name
        
class deezer_playlist(Playlist):#playlists qui existent deja sur deezer (besoin d'un id)
    def __init__(self,id_, nom=" "):
        super().__init__(nom=nom)
        self.id_=id_
        self.artistes=[]
    def generer(self):
        self.sons=client.get_playlist(self.id_).get_tracks()
    def artistes_de_la_playlist(self):
        for i in range(7):
          self.artistes.append(client.get_playlist(self.id_).get_tracks()[i].get_artist())
          
  
