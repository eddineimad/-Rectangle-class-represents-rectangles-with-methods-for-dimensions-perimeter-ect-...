class Rectangle():
    _count = 0  
    def __init__(self, longueur = 0, largeur = 0):
        self.__longueur = longueur 
        self.__largeur = largeur
        Rectangle._count += 1  

    def Getlongueur(self) :
        return self.__longueur  # Getter for length
    
    def setlongueur(self, longueur) :
        self.__longueur = longueur  # Setter for length

    def Getlargeur(self) :
        return self.__largeur  # Getter for width
    
    def setlargeur(self, largeur) :
        self.__largeur = largeur # Setter for width

    def Getcount(self) :
        return Rectangle._count   # Getter for the count of Rectangle objects
    
    def Equals(self, Rec1) : 
        if self.__largeur == Rec1.__largeur and self.__longueur == Rec1.__longueur :
            return True
        else : 
            return False
        
    def Perimetre(self):
        P = (self.__largeur + self.__longueur) * 2 
        return P
    
    def Surface(self) :
        return self.__largeur * self.__longueur 
    
    def ToString (self) :
        return "Width :" + str(self.Getlargeur()) + ";  Length :" + str(self.Getlongueur()) +"; NbrRectangle :"+ str(self.Getcount()) +"."
    
class Parallelepipede (Rectangle) :
    _count1 = 0 
    def __init__(self, longueur = 0, largeur = 0, hauter = 0 ):
        super().__init__(longueur, largeur) 
        self.__hauter = hauter  
        Parallelepipede._count1 += 1 

    def Gethauter(self) :
        return self.__hauter  # Getter for height
    
    def sethauter(self, hauter) :
        self.__hauter = hauter  # Setter for height

    def Getcount1(self) :
        return Parallelepipede._count1   # Getter for count

    def Equals(self, par) :   
        if self.Getlargeur() == par.Getlargeur() and self.Getlongueur() == par.Getlongueur() and self.__hauter == par.__hauter :
            return True
        else : 
            return False
        
    def Surface(self):
        return (super().Surface() + self.__hauter * self.Getlargeur() + self.__hauter * self.Getlongueur())*2
       
    def ToString (self) :
        return "Width :" + str(self.Getlargeur()) + ";  Length :" + str(self.Getlongueur())+ "; height :"+ str(self.Getcount1()) +"; NbrParallelepipede :"+ str(self.Getcount()) +"."
    
    def Volume (self) :
        return  self.Getlargeur() * self.Getlongueur() * self.__hauter
        