# Tarea semana 12 Registro de Temperaturas Diarias

# Crear y llenar la matriz 3D con datos de temperatura de las 3 ciudades y los dias determinados
temperaturas = [
    [  # Quito
        [17, 17, 18, 21, 20, 21, 22],  # Semana 1
        [17, 19, 18, 19, 19, 18, 17]  # Semana 2
    ],
    [  # Guayaquil
        [29, 31, 32, 32, 30, 31, 32],  # Semana 1
        [34, 35, 35, 31, 31, 32, 30]  # Semana 2
    ],
    [  # Cuenca
        [21, 19, 22, 24, 24, 23, 23],  # Semana 1
        [20, 20, 21, 19, 20, 19, 19]  # Semana 2
    ]
]

# Paso 3: Calcular el promedio de temperaturas para cada ciudad por semana
ciudades = ['Quito', 'Guayaquil', 'Cuenca']

for i, ciudad_temperaturas in enumerate(temperaturas):
    print(f"Promedios de temperatura para {ciudades[i]}:")
    for j, semana_temperaturas in enumerate(ciudad_temperaturas):
        promedio = sum(semana_temperaturas) / len(semana_temperaturas)
        print(f"  Semana {j + 1}: {promedio:.2f} grados")
        # Se imprime un línea en blanco para separar las ciudades
    print()

# Fin del programa
