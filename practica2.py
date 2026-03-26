import random

class NodeD:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    #if num is not isinstance(num,int):
    #  raise TypeError("Size debe ser un objeto tipo numerico")
    self.__size = num


  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value): # Adicionar al principio

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.__head.prev = newnode #Nueva linea para enlazar como previo el nodo nuevo
      self.__head = newnode
    self.__size += 1

  def append(self,value): # Adicionar al final
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail #asigno el previo del nuevo nodo
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1

  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      newNode = NodeD(value)
      newNode.next = nextNode #Enlazo el next del nuevo nodo, que es el next del previo
      newNode.prev = prevNode # Enlazo el previo del nuevo nodo
      nextNode.prev = newNode # Enlazo el previo del next original
      prevNode.next = newNode
      self.__size +=1

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__head.prev = None
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def pop(self):

    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      popped_node = self.__tail
      prev_tail_node = self.__tail.prev

      self.__tail = prev_tail_node
      self.__tail.next = None
      self.__size -= 1
      popped_node.prev = None
      return popped_node


  def generate(self, num, min, max):
    for _ in range(num):
      self.append(random.randint(min,max))



class Vehiculo:
  def __init__(self, placa, tipo, prioridad, revisado):
    self.placa = placa
    self.tipo = tipo
    self.prioridad = prioridad
    self.revisado = revisado


  def __str__(self):
    return f"{self.placa} - {self.tipo} - {self.prioridad} - {self.revisado}"

via: DoublyLinkedList = DoublyLinkedList()

via.append(Vehiculo("RTU128", "auto", 1, False))
via.append(Vehiculo("ATJ167", "camion", 4, False))
via.append(Vehiculo("TTC497", "moto", 2, False))
via.append(Vehiculo("AHA459", "auto", 5, False))
via.append(Vehiculo("ATH009", "auto", 2, False))
via.append(Vehiculo("AEU123", "moto", 1, False))
via.append(Vehiculo("ILH054", "auto", 3, False))
via.append(Vehiculo("APL923", "camion", 2, False))
via.append(Vehiculo("AFF567", "camion", 5, False))
via.append(Vehiculo("RRS109", "moto", 1, False))
via.append(Vehiculo("STL043", "camion", 3, False))


def paso_preferencial(via: DoublyLinkedList):
  if via.head is None:
    return

  last_moved = None
  current = via.head

  while current is not None:
    next_node = current.next
    tipo = current.value.tipo
    prioridad = current.value.prioridad

    if tipo == "moto" and prioridad == 1:
      if current.prev is not None:
        current.prev.next = current.next
        if current.next is not None:
          current.next.prev = current.prev
        else:
          via.tail = current.prev

        if last_moved is None:
          current.prev = None
          current.next = via.head
          if via.head is not None:
            via.head.prev = current
            via.head = current
          else:
            current.prev = last_moved
            current.next = last_moved.next
            if last_moved.next is not None:
              last_moved.next.prev = current
            else:
              via.tail = current
              last_moved.next = current
            last_moved = current
        else:
          if last_moved is None:
            last_moved = current

    current = next_node



def eliminar_camiones(via:DoublyLinkedList):
  current = via.head

  while current is not None:
    next_node = current.next
    tipo = current.value.tipo
    prioridad = current.value.prioridad

    if tipo == "camion" and prioridad > 3:
      if current.prev is not None:
        current.prev.next = current.next
        if current.next is not None:
          current.next.prev = current.prev
        else:
          via.tail = current.prev
      else:
        via.head = current.next
        if via.head is not None:
          via.head.prev = None
        else:
          via.tail = None

    current = next_node



def simular_accidente(via, placa_inicio, placa_fin):
  current = via.head
  nodo_a = None
  nodo_b = None

  while current is not None:
    if current.value.placa == placa_inicio:
      nodo_a = current
    if current.value.placa == placa_fin:
      nodo_b = current
    current = current.next

  if nodo_a is None or nodo_b is None:
    print("Una o ambas placas no existen.")
    return

  a_esta_antes_que_b = False
  auxiliar = nodo_a
  while auxiliar is not None and not a_esta_antes_que_b:
      if auxiliar == nodo_b:
          a_esta_antes_que_b = True
      auxiliar = auxiliar.next

  if a_esta_antes_que_b:
      vehiculo_inicial = nodo_a
      vehiculo_final = nodo_b
  else:
      vehiculo_inicial = nodo_b
      vehiculo_final = nodo_a

  contador_eliminados = 0
  vehiculos_intermedios = vehiculo_inicial.next

  while vehiculos_intermedios is not None and vehiculos_intermedios != vehiculo_final:
      contador_eliminados += 1
      vehiculos_intermedios = vehiculos_intermedios.next

  vehiculo_inicial.next = vehiculo_final
  vehiculo_final.prev = vehiculo_inicial

  via.size = via.size - contador_eliminados

  print(f"Se eliminaron {contador_eliminados} vehículos entre {placa_inicio} y {placa_fin}.")



def invertir_orden(via: DoublyLinkedList):
  current = via.head
  autos = 0
  motos = 0

  while current is not None:
    if current.value.tipo == "moto":
      motos += 1
    elif current.value.tipo == "auto":
      autos +=1
    current = current.next

  if autos > motos:
    nodo_temporal = None
    current = via.head

    while current is not None:
      nodo_temporal = current.prev
      current.prev = current.next
      current.next = nodo_temporal
      current = current.prev

    if nodo_temporal is not None:
      via.tail = via.head
      via.head = nodo_temporal.prev



def reorganizar_prioridad(via: DoublyLinkedList):
    if not via.head or not via.head.next:
      return
    current = via.head.next

    while current:
      siguiente = current.next
      if current.prev and current.value.prioridad < current.prev.value.prioridad:
        current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        else:
          via.tail = current.prev

        nodo_temporal = current.prev
        while nodo_temporal and current.value.prioridad < nodo_temporal.value.prioridad:
          nodo_temporal = nodo_temporal.prev

        if nodo_temporal is None:
          current.next = via.head
          current.prev = None
          if via.head:
            via.head.prev = current
          via.head = current
        else:
          current.next = nodo_temporal.next
          current.prev = nodo_temporal
          if nodo_temporal.next:
            nodo_temporal.next.prev = current
          nodo_temporal.next = current

      current = siguiente



print("1. Estado de la via: ")
print(via)
print("2. Dar paso preferencial:")
paso_preferencial(via)
print(via)
print("3. Eliminar camiones con prioridad mayor a 3:")
eliminar_camiones(via)
print(via)
print("4. Simular accidente entre 2 placas: ")
print("Antes: ")
print(via)
simular_accidente(via, "RRS109", "RTU128")
print(via)
print("5. Invertir el orden de la vía solo si hay más autos que motos")
print("Antes: ")
print(via)
print("Después: ")
invertir_orden(via)
print(via)
print("6. Reorganizar por prioridad:")
reorganizar_prioridad(via)
print(via)




#COLA
import random

class Node:
  __slots__ = ('__value','__next')

  def __init__(self,value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class LinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    self.__size = num

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def append(self,value): # Adicionar al final
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      self.__tail = newnode
    self.__size += 1


  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return None
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode




class Queue:

  def __init__(self):
    self.__queue = LinkedList()


  def enqueue(self, e):
    self.__queue.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la cola"
    else:
      first_node = self.__queue.popfirst()
      return first_node.value

  def is_empty(self):
    return  self.__queue.size == 0

  def len(self):
    return  self.__queue.size


  def firs(self):
    return self.__queue.head.value

  def __str__(self):
    result = [str(nodo.value) for nodo in self.__queue]
    return ' -- '.join(result)




def semaforo_con_cola(via: DoublyLinkedList):
  colaSemaforo: Queue = Queue()
  colaRevision: Queue = Queue()

  current = via2.head
  contador = 0
  while current is not None and contador < 6:
    contador += 1
    if contador <= 6:
      colaSemaforo.enqueue(current.value)
    current = current.next


  tiempo = 0
  contador_vehiculos = 0
  while colaSemaforo.is_empty() == False and contador_vehiculos < 6:
    vehiculo_actual = colaSemaforo.dequeue()
    if vehiculo_actual.tipo == "camion" and vehiculo_actual.prioridad > 3 and vehiculo_actual.revisado == False:
      vehiculo_actual.revisado = True
      colaRevision.enqueue(vehiculo_actual)
      print(f"{vehiculo_actual.placa} enviado a revisión")
      continue

    tiempo += 30
    contador_vehiculos +=1
    print(f"{vehiculo_actual.placa} pasó el semáforo en tiempo {tiempo}")

    current = via2.head
    while current is not None:
      if current.value == vehiculo_actual:
        if current.prev is not None:
          current.prev.next = current.next
        else:
          via2.head = current.next

        if current.next is not None:
          current.next.prev = current.prev
        else:
          via2.tail = current.prev
        break

      current = current.next


    while colaRevision.is_empty() == False:
      colaSemaforo.enqueue(colaRevision.dequeue())

      print(f"Tiempo total: {tiempo}")
      print(f"Vehículos que pasaron: {contador_vehiculos}")



via2 = DoublyLinkedList()

via2.append(Vehiculo("RTU128", "auto", 1, False))
via2.append(Vehiculo("ATJ167", "camion", 4, False))
via2.append(Vehiculo("TTC497", "moto", 2, False))
via2.append(Vehiculo("AHA459", "auto", 5, False))
via2.append(Vehiculo("ATH009", "auto", 2, False))
via2.append(Vehiculo("AEU123", "moto", 1, False))
via2.append(Vehiculo("ILH054", "auto", 3, False))
via2.append(Vehiculo("APL923", "camion", 2, False))
via2.append(Vehiculo("AFF567", "camion", 5, False))
via2.append(Vehiculo("RRS109", "moto", 1, False))
via2.append(Vehiculo("STL043", "camion", 3, False))


print("7. Simulación de semáforo con cola de revisión:")
semaforo_con_cola(via)
print(via)




