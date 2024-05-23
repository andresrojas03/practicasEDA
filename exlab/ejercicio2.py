import random
size = 12
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLLC:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def remove_node(self, node):
        if node == self.head:
            self.head = None
            self.tail = None
        else:
            if node == self.head:
                self.head = self.head.next
                self.tail.next = self.head
                self.head.prev = self.tail
            elif node == self.tail:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
    
    def capturar(self, k):
        if self.head is None:
            return
        current_node = self.head
        position = 0
        captures = 0
        size = self.get_size()

        # Conjunto para mantener registro de los nodos capturados
        captured_nodes = set()

        while True:
            if current_node.data == 'P':
                if current_node not in captured_nodes:
                    search_node = current_node.next
                    for i in range(1, k + 1):
                        if search_node not in captured_nodes:
                            if search_node.data == 'T':
                                print(f'CDLL[{position}]-CDLL[{(position + i) % size}]')
                                captures += 1
                                captured_nodes.add(current_node)  #agregar el policia al conjunto
                                captured_nodes.add(search_node)   #agregar el ladron al conjunto
                                break
                            search_node = search_node.next

                    #si no se encontro un ladron recorriendo la lista hacia el frente
                    if search_node.data != 'T':
                        search_node = current_node.prev
                        for i in range(1, k + 1):
                            if search_node not in captured_nodes:
                                if search_node.data == 'T':
                                    print(f'CDLL[{position}]-CDLL[{(position - i + size) % size}]')
                                    captures += 1
                                    captured_nodes.add(current_node)  
                                    captured_nodes.add(search_node)   
                                    break
                                search_node = search_node.prev
            #actualizacion del nodo para seguir con la busqueda
            current_node = current_node.next
            position += 1

            if current_node == self.head:
                break

        print(f'El número total de ladrones capturados por los policías será {captures}')


    def get_size(self):
        if self.head is None:
            return 0
        size = 1
        current_node = self.head
        while current_node.next != self.head:
            size += 1 
            current_node = current_node.next
        return size

    def printL(self):
        if self.head is None:
            print('Empty')
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()


cdll = DLLC()
k = int(input('ingrese la distancia maxima: '))
for i in range(size):
    if random.randint(0,1) == 0:
        cdll.insert('T')
    else:
        cdll.insert('P')
print('Lista de los policias y ladrones: ')
cdll.printL()
cdll.capturar(k)