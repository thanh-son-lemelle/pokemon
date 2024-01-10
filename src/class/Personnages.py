class Personnages: 
    def __init__(self, nom, x, y):
        self.__nom = nom
        self.x = x
        self.y = y

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def gauche(self):
        self.x -=1
    
    def droite(self):
        self.x +=1

    def bas(self):
        self.y +=1

    def haut(self):
        self.y -=1

    def position(self):
        return (self.x, self.y)
    
personnage = Personnages("nom", 10, 10)

position = personnage.position()

print(personnage.get_nom())
print(position)