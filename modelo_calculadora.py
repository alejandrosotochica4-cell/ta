class Calculadora:
    def __init__(self, fecha):
        self.fecha = fecha 
        self.resultado = ""
        self.tipo_operacion = ""
    def get_numero_1(self):
        return self.numero_1
    
    def set_numero_1(self, nuevo_numero1):
        self.numero_1=nuevo_numero1

    def get_numero_2(self):
        return self.numero_2
    
    def set_numero_2(self, nuevo_numero_2):
        self.numero_2=nuevo_numero_2

    def get_resultado(self):
        return self.resultado 
    
    def set_resultado(self, nuevo_resultado):
        self.resultado=nuevo_resultado
        
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self,nueva_fecha):
        self.fecha= nueva_fecha

    def get_tipo_operacion(self):
        return self.tipo_operacion

    def set_tipo_operacion(self, tipo_operacion):
        self.get_tipo_operacion = tipo_operacion

    def sumar_numeros(self, numero_1,numero_2):
        resultado = (numero_1 + numero_2)
        return resultado
    
    def restar_numeros(self, numero_1,numero_2):
        resultado = (numero_1 - numero_2)

    def multiplicar_numeros(self, numero_1,numero_2):
        resultado = (numero_1*numero_2)
        return resultado
    
    def dividr_numeros(self, numero_1,numero_2):
        resultado = (numero_1/numero_2)
        #return resultado
        print (resultado)
    
    def hacer_operacion(self, numero_1,numero_2,tipo_operacion):
        if self.tipo_operacion == "suma":
            self.resultado = self.sumar_numeros(numero_1.get_numero(),numero_2.get_numero())
        elif self.tipo_operacion == "resta" :
            self.resultado = self.restar_numeros(numero_1.get_numero(),numero_2.get_numero())

    def mostrar_resultado():
        pass 

    def mostrar_tabla():
        pass 

    

    