from datetime import datetime

def calcular_venta_total(ventas):
    """
    Calcula la facturación total de una lista de diccionarios.
    
    Cada diccionario debe tener las claves:
      - 'precio_unitario': monto unitario (convertible a Decimal)
      - 'cantidad': cantidad vendida (convertible a int)
    
    Retorna:
      - Facturación total como Decimal.
    
    Manejo de errores:
      - Si falta una clave o el valor no es válido, se ignora esa venta.
    """
    venta_total = 0
    
    for i, venta in enumerate(ventas, start=1):
        try:
            # Validar existencia de claves
            if 'precio_unitario' not in venta or 'cantidad' not in venta:
                print(f"[Advertencia] Faltan claves en la fila {i}. Se omite.")
                continue

            # Obtener valores
            precio_raw = venta['precio_unitario']
            cantidad_raw = venta['cantidad']

            # Validar que no estén vacíos
            if precio_raw in (None, '', ' ') or cantidad_raw in (None, '', ' '):
                print(f"[Advertencia] Valores vacíos en la fila {i}. Se omite.")
                continue

            # Convertir tipos
            precio_unitario = float(precio_raw)
            cantidad = int(cantidad_raw)

            # Calcular subtotal
            subtotal = precio_unitario * cantidad
            venta_total += subtotal

        except (ValueError, TypeError) as e:
            print(f"[Error] No se pudo procesar la fila {i}: {e}")
            continue

    return venta_total


def total_unidades_vendidas(ventas):
    """
    Devuelve la suma total de unidades vendidas en la lista `ventas`.
    - Ignora filas que no tengan la clave 'cantidad' o cuyo valor no sea convertible a int.
    - Retorna un int (0 si no hay ventas válidas).
    """

    total_unidades = 0
    
    for i, venta in enumerate(ventas, start=1):
        
        try:
            if 'cantidad' not in venta:
                continue
            total_unidades += int(venta['cantidad'])
        
        except (ValueError, TypeError):
            # ignorar filas inválidas
            continue

    return total_unidades


def top_5_productos_mas_vendidos(ventas):
    """
    Devuelve una lista con hasta 5 tuplas (producto, cantidad_total) ordenadas
    de mayor a menor según la cantidad vendida.
    """
    if not ventas:
        return []

    totales = {}

    for i, venta in enumerate(ventas, start=1):
        try:
            if 'producto' not in venta or 'cantidad' not in venta:
                continue
            
            producto = venta['producto']
            cantidad = int(venta['cantidad'])
            
            # Acumular
            if producto in totales:
                totales[producto] += cantidad
            
            else:
                totales[producto] = cantidad
        
        except (ValueError, TypeError):
            continue

    # ordenar por cantidad descendente la cantidad de ventas de los productos
    ordenados = sorted(totales.items(), key=lambda x: x[1], reverse=True)

    # Obtenemos el top 5
    top_5 = ordenados[:5]
    
    return top_5


def producto_mas_vendido(ventas):
    """
    Devuelve el nombre del producto más vendido y la cantidad total vendida.
    
    Cada elemento de la lista debe tener:
      - 'producto': id del producto
      - 'cantidad': cantidad vendida (convertible a int)
    
    Si hay productos repetidos, acumula sus cantidad.
    """
    if not ventas:
        print("La lista de ventas está vacía.")
        return None

    totales = {}  # diccionario para acumular ventas por producto

    for i, venta in enumerate(ventas, start=1):
        try:
            # Validar claves
            if 'producto' not in venta or 'cantidad' not in venta:
                continue

            producto = venta['producto']
            cantidad = int(venta['cantidad'])

            # Acumular
            if producto in totales:
                totales[producto] += cantidad
            
            else:
                totales[producto] = cantidad

        except (ValueError, TypeError) as e:
            print(f"[Error] No se pudo procesar la fila {i}: {e}")
            continue

    # Si no se acumuló nada
    if not totales:
        return None

    # Buscar el producto con más cantidad vendidas
    producto_top = max(totales, key=totales.get)
    cantidad_top = totales[producto_top]

    return (producto_top, cantidad_top)


def ventas_por_rango_fechas(ventas, fecha_inicio, fecha_fin):
    """
    Filtra las ventas que se encuentran dentro del rango de fechas dado.
    
    Parámetros:
      - ventas: lista de diccionarios con clave 'fecha' en formato 'YYYY-MM-DD'.

        - fecha_inicio: fecha de inicio del rango (inclusive) como cadena 'YYYY-MM-DD'.

        - fecha_fin: fecha de fin del rango (inclusive) como cadena 'YYYY-MM-DD'.
    Retorna:
      - Lista de ventas dentro del rango de fechas.
    """

    formato_fecha = "%Y-%m-%d"
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, formato_fecha)
        fecha_fin = datetime.strptime(fecha_fin, formato_fecha)
    
    except ValueError as e:
        print(f"[Error] Formato de fecha inválido: {e}")
        return []

    ventas_filtradas = []

    for i, venta in enumerate(ventas, start=1):
        try:
            # Validar clave 'fecha'
            if 'fecha' not in venta:
                continue

            fecha_venta_str = venta['fecha']
            fecha_venta_dt = datetime.strptime(fecha_venta_str, formato_fecha)

            # Filtra la venta actual si es menor o igual al rango
            if fecha_inicio <= fecha_venta_dt <= fecha_fin:
                ventas_filtradas.append(venta)

        except ValueError as e:
            print(f"[Error] No se pudo procesar la fecha en la fila {i}: {e}")
            continue

    return ventas_filtradas


if __name__ == "__main__":
    
    # Ejemplo de uso
    ventas_ejemplo = [
        {'precio_unitario': 10.35, 'cantidad': '2'},
        {'precio_unitario': '5', 'cantidad': '4'},
        {'precio_unitario': 'invalid', 'cantidad': '3'},  # Fila inválida
        {'precio_unitario': '7.00', 'cantidad': None},    # Fila inválida
    ]
    
    # Prueba de calcular_venta_total
    total = calcular_venta_total(ventas_ejemplo)
    print(f"\nFacturación total: {total} \n"
          "DEBERIA SER:       40.7 \n")
    
    # Prueba de total_unidades_vendidas
    total_unidades = total_unidades_vendidas([
        {'cantidad': '3'},
        {'cantidad': '5'},
        {'cantidad': 'invalid'},  # Fila inválida
    ])
    print(f"\nTotal unidades vendidas: {total_unidades} \n"
          "DEBERIA SER:             8 \n")

    # Prueba de top_5_productos_mas_vendidos
    top_5 = top_5_productos_mas_vendidos([
        {'producto': 'A', 'cantidad': '3'},
        {'producto': 'B', 'cantidad': '5'},
        {'producto': 'A', 'cantidad': '2'},
        {'producto': 'C', 'cantidad': '7'},
        {'producto': 'B', 'cantidad': '1'},
        {'producto': 'D', 'cantidad': '4'},
        {'producto': 'E', 'cantidad': '6'},
        {'producto': 'F', 'cantidad': '2'},
    ])

    print(f"\nTop 5 productos más vendidos: {top_5} \n"
          "DEBERIA SER:                  [('C', 7), ('B', 6), ('E', 6), ('A', 5), ('D', 4)] \n")
    
    # Prueba de producto_mas_vendido
    producto_top = producto_mas_vendido([
        {'producto': 'A', 'cantidad': '3'},
        {'producto': 'B', 'cantidad': '5'},
        {'producto': 'A', 'cantidad': '2'},
        {'producto': 'C', 'cantidad': '7'},
        {'producto': 'B', 'cantidad': '1'},
        {'producto': 'D', 'cantidad': '4'},
        {'producto': 'E', 'cantidad': '6'},
        {'producto': 'F', 'cantidad': '2'},
    ])

    print(f"\nProducto más vendido: {producto_top} \n"
          "DEBERIA SER:          ('C', 7) \n")
    

    # Prueba de ventas_por_rango_fechas
    ventas_fechas = [
        {'fecha': '2024-01-10', 'producto': 'A', 'cantidad': '3'},
        {'fecha': '2024-02-15', 'producto': 'B', 'cantidad': '5'},
        {'fecha': '2024-03-20', 'producto': 'C', 'cantidad': '2'},
        {'fecha': '2024-04-25', 'producto': 'D', 'cantidad': '7'},
    ]
    
    ventas_filtradas = ventas_por_rango_fechas(ventas_fechas, '2024-02-01', '2024-03-31')
    
    print(f"\nVentas entre 2024-02-01 y 2024-03-31: {ventas_filtradas} \n"
          "\nDEBERIA SER: [{'fecha': '2024-02-15', 'producto': 'B', 'cantidad': '5'}, \n"
          "{'fecha': '2024-03-20', 'producto': 'C', 'cantidad': '2'}] \n")  
