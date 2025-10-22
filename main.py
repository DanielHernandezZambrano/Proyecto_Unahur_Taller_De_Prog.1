from datetime import datetime
import carga_de_datos
from generador_de_reporte import generar_y_exportar_reporte
import os

# Ruta del archivo CSV
ruta_csv = os.path.join("data", "ventas.csv") 

# Carga de datos:
ventas = carga_de_datos.cargar_ventas(ruta_csv)

# Si no se cargaron ventas, salir del programa
if not ventas:
    print("No se cargaron ventas. Saliendo del programa.")

else:

    """GENERACIÓN DE REPORTE:"""

    ruta_reporte = generar_y_exportar_reporte(ventas)
    
    print(f"\nReporte generado en: {ruta_reporte}\n"
          "Y en formato CSV también. "
          "Programa finalizado.\n")

