from paquetes import Paquete
from ventas import Registro
def menu():
  while True:
    try:
      d = input('Destino (o salir): ')
      if d=='salir': break
      p = Paquete(float(input('Peso (kg): ')))
      Registro.guardar(d, p)
      print(f'✅ Reporte para CEO: {p.cat} | Costo: ${p.costo}')
    except ValueError: print('❌ Error de digitación. Intente de nuevo.')
if __name__ == '__main__': menu()