
import csv
from datetime import datetime

from analisis_de_datos import calcular_venta_total, total_unidades_vendidas, producto_mas_vendido, top_5_productos_mas_vendidos


def leer_ventas_csv(path):
	ventas = []
	with open(path, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			ventas.append(row)
	return ventas


def generar_y_exportar_reporte(ventas, reporte_path='reporte_ventas.txt'):
	"""Genera el reporte en TXT y CSV a partir de la lista de ventas.

	Retorna la ruta del archivo TXT generado.
	"""

	# Cálculos
	venta_total = calcular_venta_total(ventas)
	unidades = total_unidades_vendidas(ventas)
	prod_top = producto_mas_vendido(ventas)
	top5 = top_5_productos_mas_vendidos(ventas)

	fecha_reporte = datetime.now().strftime('%d/%m/%Y')

	# Formato
	lineas_reporte = []
	lineas_reporte.append('--- Reporte de Ventas E-commerce ---')
	lineas_reporte.append('')
	lineas_reporte.append(f'Fecha del Reporte: {fecha_reporte}')
	lineas_reporte.append('')
	lineas_reporte.append('--- Resumen General ---')

	# Facturación con dos decimales y signo $
	try:
		fact_str = f"$ {float(venta_total):.2f}"
	except Exception:
		fact_str = f"$ {venta_total}"

	lineas_reporte.append(f'Facturación Total: {fact_str}')
	lineas_reporte.append(f'Cantidad Total de Unidades Vendidas: {unidades}')

	prod_top_str = prod_top[0] if prod_top else 'N/A'

	lineas_reporte.append(f'Producto Más Vendido: {prod_top_str}')
	lineas_reporte.append('')
	lineas_reporte.append('--- Top 5 Productos Más Vendidos ---')
	for i in range(5):
		if i < len(top5):
			lineas_reporte.append(f"{i+1}. {top5[i][0]}")
		else:
			lineas_reporte.append(f"{i+1}. ")
	lineas_reporte.append('')
	lineas_reporte.append('---------------------------------------')

	# Escribir archivo txt
	with open(reporte_path, 'w', encoding='utf-8') as archivo:
		for linea in lineas_reporte:
			archivo.write(linea + '\n')

	# Generar CSV paralelo
	generar_csv(reporte_path, venta_total, unidades, prod_top_str, top5, fecha_reporte)

	return reporte_path


def generar_csv(reporte_path, facturacion, unidades, prod_top_str, top5, fecha_reporte):
	"""Genera un CSV con una sola fila con los mismos datos del reporte.

	Campos: fecha,facturacion_total,cant_total_de_unid_vendidas,prod_mas_vendido,lista_top5_prod_mas_vendidos
	La lista top5 se guarda como JSON en la última columna para preservar la lista de strings.
	"""

	csv_path = reporte_path.replace('.txt', '.csv')

	try:
		facturacion_csv = f"{float(facturacion):.2f}"
	except Exception:
		facturacion_csv = str(facturacion)

	lista_top5_nombres = [p for p, _ in top5]
	# Representar la lista en un formato legible: [item1, item2, ...]
	lista_top5_str = '[' + ', '.join(lista_top5_nombres) + ']'

	with open(csv_path, 'w', encoding='utf-8', newline='') as cf:
		writer = csv.writer(cf)
		writer.writerow(['fecha', 'facturacion_total', 'cant_total_de_unid_vendidas', 'prod_mas_vendido', 'lista_top5_prod_mas_vendidos'])
		writer.writerow([fecha_reporte, facturacion_csv, unidades, prod_top_str, lista_top5_str])

	return csv_path


if __name__ == '__main__':
	csv_path = 'data/ventas.csv'
	ventas = leer_ventas_csv(csv_path)
	out = generar_y_exportar_reporte(ventas)
	print(f'Reporte generado: {out}')

