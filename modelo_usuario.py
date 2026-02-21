class Usuario:
    def __init__(self, nombre, ID):
        self.nombre=nombre
        self.ID=ID

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre=nuevo_nombre

    def mostar_info(self):
        print(f"ID: {self.ID}")
        print(f"nombre: {self.nombre}")

