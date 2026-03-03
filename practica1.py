class Node:
  def __init__(self, value):
    self.value = value
    self.next: Node = None #referencia del nodo que le sigue

  def __repr__(self) -> str:
    return f"{self.value} -> {self.next}"

class LinkedList:
  def __init__(self):
    self.head: Node = None
    self.size: int = 0

  def append(self, elemento, current=None):
    if current is None:
      if self.head is None:
          self.head = Node(elemento)
          self.size += 1
          return
      return self.append(elemento, self.head)

    if current.next is None:
        current.next = Node(elemento)
        self.size += 1
        return

    self.append(elemento, current.next)


  def promedio(self, current = None, suma = 0, cantidad = 0):
    if current is None:
      if self.head is None:
        return 0

      return self.promedio(self.head, 0, 0)

    if current.next is None:
      suma += current.value.nivel_riesgo
      cantidad +=1
      return suma/cantidad

    return self.promedio(current.next, suma + current.value.nivel_riesgo, cantidad + 1)


  def secuencia_larga(self, current=None, maxima=""):
    if current is None:
      if self.head is None:
        return
      return self.secuencia_larga(self.head, maxima)

    if len(current.value.secuencia) > len(maxima):
      maxima = current.value.secuencia

    if current.next is None:
      return maxima

    return self.secuencia_larga(current.next, maxima)

  def __repr__(self) -> str:
    return f"{self.head}"


class Secuencia:
  def __init__(self, id, nombre_muestra, secuencia, nivel_riesgo):
    self.id = id
    self.nombre_muestra = nombre_muestra
    self.secuencia = secuencia
    self.nivel_riesgo = nivel_riesgo
    self.subcadenas_lista = []

  def contar_patron(self, patron, i=0):
    if i > len(self.secuencia) - len(patron):
      return 0

    if (self.secuencia[i] == patron[0] and self.secuencia[i+1] == patron[1]):
      return 1 + self.contar_patron(patron, i + 1)

    return self.contar_patron(patron, i + 1)

  def subcadenas(self, i=0, j=None):
    if j is None:
      j = i+1

    if i >= len(self.secuencia):
      return self.subcadenas

    if j > len(self.secuencia):
      return self.subcadenas(i + 1, i + 2)

    self.subcadenas_lista.append(self.secuencia[i:j])
    return self.subcadenas(i, j + 1)


  def mas_nucleoditos(self, i = 0):
    if i > len(self.secuencia):
      return 0

    if self.secuencia[i] == "A":
      valor = 1

    if self.secuencia[i] == "T":
      valor = -1
    else:
      valor = 0

    if i == len(self.secuencia) -1:
      if valor > 0:
        return True
      return False
    else:
      siguiente = self.mas_nucleoditos(i+1)
      if siguiente:
        total = valor +1
      else:
        total = valor
      if total > 0:
        return True
      else:
        return False


  def mutacion_genetica(self, i=0):
    if i >= len(self.secuencia):
      return ""

    if self.secuencia[i] == 'A':
      nuevo = 'T'
    else:
      if self.secuencia[i] == 'T':
        nuevo = 'A'
      else:
        nuevo = self.secuencia[i] #queda igual

    return nuevo + self.mutacion_genetica(i + 1)


  def __repr__(self) -> str:
    return f"Id: {self.id}, Nombre de muestra: {self.nombre_muestra}, Secuencia: {self.secuencia}, Nivel de riesgo: {self.nivel_riesgo}"


s1: Secuencia = Secuencia(1,"RR", "ATGATAT", 1)
s2: Secuencia = Secuencia(2,"RA", "ATGATATAT", 2)
l: LinkedList = LinkedList()
l.append(s1)
l.append(s2)

print("Lista: ")
print(l)
print("Contar patron AT: ")
print(s1.contar_patron("AT"))
print("Promedio de nivel de riesgo: ")
print(l.promedio())
print("Secuencia más larga: ")
print(l.secuencia_larga())
print("Subcadenas:")
s1.subcadenas()
print(s1.subcadenas_lista)
print("Contiene más nucleótidos A que T:")
print(s1.mas_nucleoditos())
print("Mutacion genetica:")
print("Antes:")
print(s1.secuencia)
print("Despues: ")
print(s1.mutacion_genetica())