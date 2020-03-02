from model.model import Model
from view.view import View


class Controller:
    #Contrusctor
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    #Contacto controllers
    def agregar_contacto(self,id_contacto, nombre, tel, correo , dir):
        e,c = self.model.agregar_contacto(id_contacto, nombre, tel, correo , dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre='', n_tel='', n_correo='', n_dir=''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e,c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.contactos_letra(letra)
        self.view.mostrar_contactos(c)

    def agregar_cita(self,id_cita,id_contacto, lugar, fecha, hora , asunto):
        e,c = self.model.agregar_cita(id_cita,id_contacto, lugar, fecha, hora , asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)

    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)

    def insertar_contactos(self):
        self.agregar_contacto(1,'Juan Perez', '4641661118', 'jperez@gmail.com','Av siempre viva 113')
        self.agregar_contacto(2,'Carlos Martinez', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')
        self.agregar_contacto(3,'Armando Navarro', '6473350', 'Armando.Navarroz@gmail.com','Piedras negras 234')
        self.agregar_contacto(4,'Adriana Prieto', '64891111', 'zanahoria@gmail.com','Jalisto 032')
    
    def insertar_citas(self):
        self.agregar_cita(1,1, 'Cerveceria Chapultepec', '26/01/2020','14:30','Tomar')
        self.agregar_cita(2,1, 'MCarty´s', '10/09/2020','14:30','Platicar')
        self.agregar_cita(3,2, 'Casa de Levi', '26/05/20','14:30','Tomar mas !')

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e,c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def actualizar_cita(self,id_cita,n_id_contacto='', n_lugar='', n_fecha='', n_hora='' , n_asunto=''):
        e = self.model.actualizar_cita(id_cita,n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas_fecha(self, fecha):
        c = self.model.cita_fecha(fecha)
        self.view.mostrar_citas(c)


    def start(self):
        #Display a welcome mesagge
        self.view.start()
        #insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #show all contacts in DB
        self.leer_todos_contactos()
        self.leer_contactos_letra('a')
        self.leer_todas_citas()

    def menu(self):
        #Display menu
        self.view.menu()
        while True:
            o = input('Seleccion una opcion (1-13):  ')

            if o == '1':
                id_contacto = int(input('ID del contacto:'))
                nombre = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dir = input('Direccion ')
                self.agregar_contacto(id_contacto,nombre,tel,correo,dir)
            if o == '2':
                self.leer_todos_contactos()
            if o == '3':
                id_contacto = int(input('ID del contacto:'))
                self.leer_contacto(id_contacto)
            if o == '4':
                id_contacto = int(input('ID del contacto:'))
                nombre = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dir = input('Direccion ')
                self.actualizar_contacto(id_contacto,nombre,tel,correo,dir)
            if o == '5':
                g = input('Ingrese id de contacto:  ')
                self.borrar_contacto(g)
            if o == '6':
                g = input('Ingrese una letra:  ')
                print(g)
                self.leer_contactos_letra(g)
            if o == '7':
                id_cita = int(input('ID de la cita:'))
                id_contacto = int(input('ID del contacto:'))
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto ')
                self.agregar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
            if o == '8':
                self.leer_todas_citas()
            if o == '9':
                g = input('Ingrese una letra:  ')
                self.leer_cita(g)
            if o == '10':
                id_cita = int(input('ID de la cita:'))
                id_contacto = int(input('ID del contacto:'))
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto ')
                self.actualizar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
            if o == '11':
                self.borrar_cita(1)
            if o == '12':
                fecha = input('Ingrese la fecha (dd-mm-aaaa): ')
                self.leer_citas_fecha(fecha)
            elif o == '13':
                self.view.end()
                break
    

