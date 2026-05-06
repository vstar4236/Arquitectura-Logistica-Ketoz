class Paquete:
  def __init__(self, p):
    self.peso = p
    self.cat = 'Documento' if p<2 else 'Paqueteria' if p<=20 else 'Carga'
    self.costo = 5000 if self.cat=='Documento' else 15000 if self.cat=='Paqueteria' else 50000