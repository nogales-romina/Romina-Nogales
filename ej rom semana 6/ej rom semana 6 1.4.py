print("Ejercicio 1\n")
canciones_dia = ("Blinding Lights", "Heat Naves", "Anti-Hero")
canciones_noche = ("levitating", "As It Was")

playlist_completa = canciones_dia + canciones_noche
print(canciones_dia)
print(canciones_noche)
print(playlist_completa)

print ("\nEjercicio 2\n")
ubicaciones_norte = ((19.5, -99.2), (19.6, -99.3))
ubicaciones_sur = ((19.4, -99.1), (19,3, -99.4))
todas_ubicaciones = ubicaciones_norte + ubicaciones_sur
print(ubicaciones_norte)
print(ubicaciones_sur)
print(todas_ubicaciones,"\n")

print("\nEjercicio 3 - Repetición\n")
emojis = ("💕", "🫀")
cartel = emojis * 5
print (emojis)
print(cartel,"\n")

print("\nEjercicio 4 - Longitud\n")

seguidores_tiktok = 1500
seguidores_insta = 2300
seguidores_fb = 950
seguidores_total = seguidores_tiktok + seguidores_insta + seguidores_fb 
seguidores = (seguidores_tiktok, seguidores_insta, seguidores_fb)
cantidad_redes = len(seguidores)
print("Seguidores en TikTok:", seguidores_tiktok)
print("Seguidores en Instagram:", seguidores_insta)
print("Seguidores en Facebook:", seguidores_fb)
print("Total de seguidores:", seguidores_total)
print("Cantidad de redes sociales:", cantidad_redes)

print("\nEjercicio 5 - count In")
resultados_partidas = ("gané", "perdi", "gané", "gané", "perdi", "gané", "empate") 
veces_gane = resultados_partidas.count ("gané") 
print ("He ganado:",veces_gane)

print("InEjercicio 6 - indexin")
ranking = ("Marcelo",
"Mariana", "Vane", "Abi", "Fer", "Marcelo", "orlando")
mi_posicion = ranking.index("Mariana")
print("Estov en la posicion: ", mi_posicion,"\n")

print("InEjercicio 7 - slicing ln")
juegos = ("Ninecraft", "Fortnite", "Roblox", "Among Us", "Valorant", "GTA V", "ACNH", "Call of Duty")
ultimos_tres = juegos[2:5]
print(ultimos_tres)

print("Inejercicio 8 - recorrer tupla\n")
canciones = ("EVES CLOSED","The Fate of ophelia", "when Did You Get Hot?", "Golden")
for cancion in canciones:
    print(cancion)

print("InEjercicio 9 - verificar si un elemento existe\n")
grupo_proyecto = ("Meli","Alex", "Mia", "Andrea")
print("Integrantes del equipo", grupo_proyecto)
print ("\n¿Mia está en el grupo?")
print("Mia" in grupo_proyecto)
print("Injorlando está en el grupo?")
print ("orlando" in grupo_proyecto)

print("\nEjercicio 10 - ordenar la tupla\n")
puntuaciones = (580, 250, 1040, 390, 750, 2480, 870, 138, 938)
puntuaciones_ordenadas = tuple(sorted(puntuaciones))
print(puntuaciones_ordenadas)