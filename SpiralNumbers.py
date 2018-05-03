
#Spiral number v0 by Jean Trasud
import numpy as np

class Spiral:
    def __init__(self,donnee):
        self.donnee=donnee
        self.objectif=self.donnee**2
        self.spirale=np.zeros((self.donnee,self.donnee))
#fonction de parcours en spirale horaire
#commentaire additionnel
    def parcoursh(self):
        cote=self.donnee
        sensparcours=[[0,1],[1,0],[0,-1],[-1,0]]
        sens=0
        compt=0
        i,j=0,0
        val=self.objectif
        while val>0:
            self.spirale[i,j]=val
            val-=1
            compt+=1
            if compt==cote:
                sens=(sens+1)%4
                compt=0
                if sensparcours[sens][0]!=0:
                    cote-=1
            k,l=sensparcours[sens]
            i,j=i+k,j+l


    def affiche(self):
        print(self.spirale)
#test
essai=Spiral(8)
essai.parcoursh()
essai.affiche()
