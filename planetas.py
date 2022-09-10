numeros = [ 1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10 ]

arreglo = [ 28, "Sebastián", 8, "Barón" ]

planetas = [ "Mercurio", 1, "Venus", 2, "Tierra", 3, "Marte", 4, 
              
              "Jupiter", 5, "Saturno", 6, "Urano", 7, "Neptuno", 8, 
              
              "Plutón", 9 ]

arregloslice = arreglo[ 1 : 3 ]

arregloslice1 = planetas[ 1 : 10 ]

arregloslice2 = planetas[ 1 : -1 ]

arregloslice3 = planetas[ 5 : 10 ]

numeros.sort( )

nombres = ['Tierra', 'Nibiru', 'Kepler']

nombres.sort( )

print( nombres )

arregloextendido = numeros

arregloextendido.extend( planetas )

arregloextendido.index( "Tierra", 1 )

planetas.sort( key = str.lower )