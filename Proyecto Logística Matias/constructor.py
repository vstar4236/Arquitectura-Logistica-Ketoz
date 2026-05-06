import os, sqlite3

# 👇 1. PEGA LA RUTA DE LA CARPETA DONDE ESTÁS TRABAJANDO
ruta_maestra = r"C:\Users\kwdy\OneDrive\Documentos\Proyectos PowerBI\Proyecto Logística Matias" 

carpeta = os.path.join(ruta_maestra, "Ketoz_Logistica")
os.makedirs(carpeta, exist_ok=True)

archivos = {
    "datos.py": "destinos = ['Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Bucaramanga']",
    "database.py": "import sqlite3\ndef conectar(): return sqlite3.connect('logistica.db')",
    "paquetes.py": "class Paquete:\n  def __init__(self, p):\n    self.peso = p\n    self.cat = 'Documento' if p<2 else 'Paqueteria' if p<=20 else 'Carga'\n    self.costo = 5000 if self.cat=='Documento' else 15000 if self.cat=='Paqueteria' else 50000",
    "ventas.py": "from database import conectar\nclass Registro:\n  @staticmethod\n  def guardar(d, p):\n    c = conectar()\n    c.execute('INSERT INTO envios (destino, peso, categoria, costo) VALUES (?,?,?,?)', (d, p.peso, p.cat, p.costo))\n    c.commit()",
    "main.py": "from paquetes import Paquete\nfrom ventas import Registro\ndef menu():\n  while True:\n    try:\n      d = input('Destino (o salir): ')\n      if d=='salir': break\n      p = Paquete(float(input('Peso (kg): ')))\n      Registro.guardar(d, p)\n      print(f'✅ Reporte para CEO: {p.cat} | Costo: ${p.costo}')\n    except ValueError: print('❌ Error de digitación. Intente de nuevo.')\nif __name__ == '__main__': menu()"
}

for nom, cont in archivos.items():
    with open(os.path.join(carpeta, nom), "w", encoding="utf-8") as f: f.write(cont.strip())

os.chdir(carpeta)
conn = sqlite3.connect('logistica.db')
conn.execute("CREATE TABLE IF NOT EXISTS envios (id INTEGER PRIMARY KEY, destino TEXT, peso REAL, categoria TEXT, costo REAL)")
datos_mock = [('Bogota', 1.5, 'Documento', 5000), ('Medellin', 15.0, 'Paqueteria', 15000), ('Cali', 45.0, 'Carga', 50000), ('Bogota', 0.5, 'Documento', 5000), ('Barranquilla', 18.0, 'Paqueteria', 15000), ('Bucaramanga', 55.0, 'Carga', 50000), ('Bogota', 12.0, 'Paqueteria', 15000), ('Cali', 1.0, 'Documento', 5000), ('Medellin', 60.0, 'Carga', 50000), ('Barranquilla', 1.2, 'Documento', 5000), ('Bogota', 25.0, 'Carga', 50000), ('Cali', 14.0, 'Paqueteria', 15000), ('Medellin', 0.8, 'Documento', 5000), ('Bucaramanga', 19.0, 'Paqueteria', 15000), ('Bogota', 5.0, 'Paqueteria', 15000)]
conn.executemany("INSERT INTO envios (destino, peso, categoria, costo) VALUES (?,?,?,?)", datos_mock)
conn.commit(); conn.close()
print(f"✅ ¡ÉXITO! Proyecto Ketoz actualizado en: {carpeta}")