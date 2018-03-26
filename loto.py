from math import factorial
import pandas as pd 
import matplotlib.pyplot as plt
import random


bolitas = list(range(1,42))

prob_acertar = (41*40*39*38*37*36)
fact_num_jugados = factorial(6)
prob_acertar = prob_acertar / fact_num_jugados

sorteos = 11 
bolitas_a_sacar = 6

contador_sorteos = 1

bolitas_sorteadas = [] 

while contador_sorteos <= sorteos:
	contador_bolitas = 1
	copia_bolitas = bolitas[:] 
	print("Tómbola:", copia_bolitas)
	print("")
	print("Sorteo N°:", contador_sorteos)
	print("")

	while contador_bolitas <= bolitas_a_sacar:
		elemento = random.choice(copia_bolitas)
		bolitas_sorteadas.append(elemento) 
		indice_de_elemento = copia_bolitas.index(elemento)
		del copia_bolitas[indice_de_elemento]
		print("Bolita sacada:", elemento)
		print("")
		print("Bolitas en tómbola:", copia_bolitas, "\n")
		contador_bolitas += 1


	contador_sorteos += 1


df = pd.DataFrame(bolitas_sorteadas, columns=["Bolitas"])
df.to_csv('lista_loto.csv', index=False)

tabla_frecuencia = pd.crosstab(index=df["Bolitas"], columns="frecuencia")

df_tab = pd.DataFrame(tabla_frecuencia)
df_tab.to_csv('lista_frec_loto.csv', index=True)



print("--MENSAJES DEL SISTEMA. Loto--\n")
print("Cantidad de sorteos simulados:", sorteos, "\n")
print("Cantidad de bolitas sorteadas en la simulación:", len(bolitas_sorteadas), "\n")
print("Simulación terminada. Revise los archivos: lista_loto.csv y lista_frec_loto.csv.")