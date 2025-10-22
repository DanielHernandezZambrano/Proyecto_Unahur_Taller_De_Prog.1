<p align="center">
  <img src="data/reporte_venta.webp" alt="Vista previa del reporte de ventas" width="500"/>
</p>

## Proyecto: Reportes de Ventas — UNAHUR (Taller de Programación 1)

Un conjunto de scripts en Python para cargar datos de ventas desde un CSV, calcular métricas
y generar un reporte en formato TXT y CSV.

Este proyecto es una entrega práctica que incluye:

- `main.py` — Orquestador: carga los datos y llama al generador de reporte.
- `carga_de_datos.py` — Función para leer `data/ventas.csv` y convertir las filas a diccionarios con tipos correctos.
- `analisis_de_datos.py` — Funciones que realizan cálculos: facturación total, unidades vendidas, top de productos, filtrado por fechas.
- `generador_de_reporte.py` — Produce un archivo `reporte_ventas.txt` y un CSV paralelo con el resumen.
- `data/ventas.csv` — Ejemplo de datos (debe existir para que `main.py` funcione).

## Requisitos

El proyecto fue escrito usando solo la librería estándar de Python (csv, datetime, os). No se requieren paquetes externos.

Si usas un entorno virtual, crea uno con:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Y luego instala dependencias (si se agrega alguna en el futuro):

```powershell
pip install -r requirements.txt
```

## Estructura del CSV esperado (`data/ventas.csv`)

El lector en `carga_de_datos.py` espera un CSV con encabezados exactos (columnas):

- `fecha` — formato YYYY-MM-DD (por ejemplo, 2024-02-15)
- `id_producto` — identificador del producto
- `producto` — nombre o código del producto
- `cantidad` — número entero
- `precio_unitario` — número (puede contener decimales)

Ejemplo de fila:

```csv
fecha,id_producto,producto,cantidad,precio_unitario
2024-02-15,1001,Camiseta,3,349.99
```

Si el archivo no está presente o tiene errores de lectura, `carga_de_datos.cargar_ventas` retornará una lista vacía y `main.py` mostrará un mensaje informando que no se cargaron ventas.

## Uso

1) Desde la raíz del proyecto (donde está `main.py`) ejecuta:

```powershell
python .\main.py
```

2) El script realizará lo siguiente:

- Cargará `data/ventas.csv` con `carga_de_datos.cargar_ventas`.
- Calculará métricas con las funciones de `analisis_de_datos.py`.
- Generará `reporte_ventas.txt` (en la raíz del proyecto) y un CSV paralelo `reporte_ventas.csv` con el mismo resumen.

Al finalizar verás por consola la ruta del reporte generado.

## Qué calcula el reporte

- Facturación total (suma de precio_unitario * cantidad)
- Cantidad total de unidades vendidas
- Producto más vendido (por cantidad acumulada)
- Top 5 de productos más vendidos

El `reporte_ventas.txt` está pensado para ser legible por humanos y el CSV paralelo contiene la misma información en una fila.

## Ejemplos y pruebas

Los módulos incluyen bloques `if __name__ == '__main__'` con ejemplos y pruebas simples. Puedes ejecutar cada módulo por separado para ver sus mensajes de prueba:

```powershell
python .\analisis_de_datos.py
python .\carga_de_datos.py
python .\generador_de_reporte.py
```

## Autor / Licencia

Proyecto de práctica — Taller de Programación 1 (UNAHUR). Código compartido tal cual para uso educativo.

