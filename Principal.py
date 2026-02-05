from Libro_modelo import Libro_modelo
from Autor_modelo import autor_modelo
from libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

obj_api_autores = Api_lista_autores()
obj_bd = base_datos_libro()

#zona de autores
obj_autor = autor_modelo("lusi martis", "24/07/1009", "estadounidense")
obj_autor1 = autor_modelo("pilatos", "20/02/1001", "griego")
lista_dotos_autor = [obj_autor]
lista_dotos_autor = [obj_autor1]
obj_api_autores.guardar_autores(lista_dotos_autor)

#zona de libros

obj_libro = Libro_modelo("18 de diciembre", "354 hojas", "Narnia", "aventura")
obj_libro2 = Libro_modelo("30 de octubre", "400 hojas", "Harry Potter", "fantasia")

#guardar autores en api

obj_api_autores.guardar_autores([obj_autor])
obj_api_autores.guardar_autores ([obj_autor1])

#guardar libros

obj_bd.guardar_libro(obj_libro)
obj_bd.guardar_libro(obj_libro2)

#mostrar pocicion de autor

obj_api_autores.mostrar_autores()

#mostrar info del autor 

obj_autor.ver_info()
obj_autor1.ver_info()
obj_libro2.mostrar_cantidad_hojas()
obj_libro2.mostrar_tematica()