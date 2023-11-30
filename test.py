from Rectangle1 import Rectangle, Parallelepipede 
import copy
rec0 = Rectangle()  
rec1 = Rectangle(12, 5)  
recc = copy.copy(rec1) 

print(rec0.Equals(rec1))

print("Permitre is :", rec0.Perimetre())
print("Permitre is :", rec1.Perimetre())
print("Permitre is :", recc.Perimetre())
print("Surface is :", rec0.Surface())
print("Surface is :", recc.Surface())
print("Surface is :", recc.Surface())

print(rec0.ToString())
print(rec1.ToString())
print(recc.ToString())


par0 = Parallelepipede()  
par1 = Parallelepipede(12, 5, 12)
parc = copy.copy(par1)  

print(par0.Equals(par1))

print("Volume is :", par0.Volume())
print("Volume is :", par1.Volume())
print("Volume is :", parc.Volume())
print("Surface is :", par0.Surface())
print("Surface is :", par1.Surface())
print("Surface is :", parc.Surface())

print(par0.ToString())
print(par1.ToString())
print(parc.ToString())
