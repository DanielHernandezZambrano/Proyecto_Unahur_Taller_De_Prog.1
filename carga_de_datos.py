import csv

def cargar_ventas(ruta_archivo):
    """
    Carga los datos de ventas desde un archivo CSV.

    Parámetros:
    ruta_archivo (str): La ruta al archivo CSV que contiene los datos de ventas.

    Retorna:
    datos = []
    lista de diccionarios: Una lista donde cada diccionario representa una fila del archivo CSV.
    """

    datos = []
    
    try:
        with open(ruta_archivo, encoding='utf-8') as archivo:
            
            lector = csv.DictReader(archivo)
            
            # Itera sobre cada fila del archivo CSV
            for fila in lector:

                # Convierte los valores numéricos a los tipos adecuados en la fila iterada:
                fila_convertida ={
                    'fecha': fila['fecha'],
                    'id_producto': fila['id_producto'],
                    'producto': fila['producto'],
                    'cantidad': int(fila['cantidad']),
                    'precio_unitario': float(fila['precio_unitario'])
                }
                
                # Agrega la fila convertida a la lista de datos
                datos.append(fila_convertida)

        return datos
    
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return []
    
    except Exception as e:
        print(f"Error al leer el archivo {ruta_archivo}: {e}")
        return []



if __name__ == "__main__":
    ruta_csv = "data/ventas.csv"
    cargar_ventas(ruta_csv)