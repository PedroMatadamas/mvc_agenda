class View:
    def mostrar_contacto(self, contacto):
        print('**************** Datos del contacto **************** ')
        print('Nombre', contacto.nombre)
        print('Telefono', contacto.tel)
        print('Correo', contacto.correo)
        print('direccion', contacto.dir)
        print('******************************** ')

    def mostrar_contactos(self, contactos):
        print('**************** Contactos **************** ')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('******************************** ')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha agregado a la base de datos!')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha borrado de la base de datos!')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado')

    def contacto_ya_existe(self,contacto):
        print('El contacto', contacto.id_contacto, 'ya existe en la base de datos')

    def contacto_no_existe(self,id_contacto):
        print(id_contacto,'Contacto no existe en la base de datos')

    def mostrar_cita(self, cita):
        print('**************** Datos de la cita **************** ')
        print('ID', cita.id_cita)
        print('Contacto', cita.id_contacto)
        print('Lugar', cita.lugar)
        print('Fecha', cita.fecha)
        print('Hora', cita.hora)
        print('Asunto', cita.asunto)
        print('******************************** ')

    def mostrar_citas(self, citas):
        print('**************** Citas **************** ')
        for c in citas:
            print(c.lugar, c.fecha, c.hora, c.asunto)
        print('******************************** ')

    def crear_cita(self, cita):
        print(cita.asunto, 'Se ha agregado a la base de datos!')
    
    def agregar_cita(self, cita):
        print('Se ha agregado cita de: ', cita.asunto)

    def borrar_cita(self, cita):
        print(cita.asunto, 'Se ha borrado de la base de datos!')
        
    def modificar_cita(self, cita_o, cita_n):
        print(cita_o, 'Se ha modificado')

    def cita_ya_existe(self,cita):
        print(cita.id_asunto, 'Cita ya existe en la base de datos')

    def cita_no_existe(self,id_cita):
        print(id_cita,'Cita no existe en la base de datos')

    def start(Self):
        print("esto es un ejemplo sencillo de mvc")

    def end(self):
        print("Hata la vista!")
    
    def opcion_no_valida(self):
        print("Opcion incorrecta intenta de nuevo")

    def menu(Self):
        print('1 Agregar contactos')
        print('2 Mostrar contactos')
        print('3 Leer contacto')
        print('4 Editar contacto')
        print('5 Borrar contacto')
        print('6 Buscar contacto por letra')
        print('7 Agregar cita')
        print('8 Mostrar citas')
        print('9 Mostrar cita')
        print('10 Editar cita')
        print('11 Borrar cita')
        print('12 Buscar cita por letra')
        print('13 salir')