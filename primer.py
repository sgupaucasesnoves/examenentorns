
#Aquest programa determina si un nombre és enter.

def comprova_si_es_primer (num) : 

	 for x in range (2,num-1) :  
 
	 	if num%x == 0 : return False 

	 return True 

print("Escriu un nombre: ")

n = int (input())

if comprova_si_es_primer(n) == True : 

	print("El nombre és primer")

else : 

	print("El nombre no és primer")


input("Atura")
