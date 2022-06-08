from Nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def vacio(self):
        return self.cabeza == None

    # ======================= METODO PARA INGRESAR NODOS ==========================================
    def ingresar(self, dato):
        Nuevo = Nodo(dato)
        if self.vacio():
            self.cabeza = self.cola = Nuevo
            self.cola.siguiente = self.cabeza
        else:
            Nuevo.siguiente = self.cabeza
            self.cabeza.anterior = Nuevo
            self.cabeza = Nuevo
        self.unirnodos()

    def unirnodos(self):
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza

    # ========================= METODO PARA IMPRIMIR ============================================
    def imprimir(self):
        print("NUMEROS EN LA LISTA :0")
        aux = self.cabeza
        while(aux != None):
            print(aux.dato)

            if(aux.siguiente == self.cabeza):
                return  # PARA EL FINAL QUE YA NO SIGA
            aux = aux.siguiente

    # ========================= METODO PARA BUSCAR ============================================

    def buscar(self, dato):
        print("================================================================")
        print(":0 TU NUMERO ANTERIOR, ACTUAL Y SIGUIENTE SON: ")
        aux = self.cabeza
        while(aux != None):
            if(aux.dato == dato):
                print("ANTERIOR: " + str(aux.anterior.dato))
                print("ACTUAL: " + str(aux.dato))
                print("SIGUIENTE: " + str(aux.siguiente.dato))

            # print(aux.valor)
            if(aux.siguiente == self.cabeza):
                return  # PARA EL FINAL QUE YA NO SIGA

            aux = aux.siguiente
