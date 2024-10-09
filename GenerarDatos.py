import os
import cv2
import matplotlib.pyplot as plt

DATADIR = "C:\\Users\\Estefy Portillo\\Desktop\\Tes_1\\archive\\jpeg224"

#CATEGORIAS = ['benigno', 'maligno', 'indefinido']
CATEGORIAS = ['test','train']
def Generar_datos():
    for categoria in CATEGORIAS:
        # Generar la ruta completa para cada categoría y imprimirla
        ruta_completa = os.path.join(DATADIR, categoria)
        # Asegurarse de que la ruta existe
        if os.path.exists(ruta_completa):
            for imagen_nombre in os.listdir(ruta_completa):
                imagen_ruta = os.path.join(ruta_completa, imagen_nombre)
                imagen = cv2.imread(imagen_ruta)
                if imagen is not None:
                    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))  # Convertir de BGR a RGB
                    plt.show()
                else:
                    print(f"Error al cargar la imagen: {imagen_ruta}")
        else:
            print(f"La ruta {ruta_completa} no existe.")

# Llamar a la función para probarla
Generar_datos()
