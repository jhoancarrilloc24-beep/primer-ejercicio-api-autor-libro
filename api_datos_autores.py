class Api_lista_autores:
    def __init__(self):
        self.Api_lista_autores= []
        
    def guardar_autores(self, lista_autor):
        self.Api_lista_autores.append(lista_autor)
        print(self.Api_lista_autores) 

    def mostrar_autores(self):
        print(self.Api_lista_autores)

        for i in range(len(self.Api_lista_autores)):
            print("imprimir por pocicion")
            print(self.Api_lista_autores[i])

            for J in range(len(self.Api_lista_autores[i])):
                print("imprimir por pocicion interna")
                print(self.Api_lista_autores[i][J])
