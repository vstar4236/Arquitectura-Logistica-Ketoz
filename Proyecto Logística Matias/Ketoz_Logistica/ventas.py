from database import conectar
class Registro:
  @staticmethod
  def guardar(d, p):
    c = conectar()
    c.execute('INSERT INTO envios (destino, peso, categoria, costo) VALUES (?,?,?,?)', (d, p.peso, p.cat, p.costo))
    c.commit()