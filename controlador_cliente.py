import cliente_socket
import peticion
import logs


log = logs.get_logger('Cliente-Ctrl')


class ControladorCliente:
    def __init__(self):
        self.cliente = client.Cliente()
    
    def retiro(self,cuenta,valor):
        pet = peticion.Peticion('retiro',{'cuenta':cuenta,'valor':valor})
        resp = self.cliente.enviar_peticion(pet)
        return resp

    def abono(self,cuenta,valor):
        pet = peticion.Peticion('abono',{'cuenta':cuenta,'valor':valor})
        resp = self.cliente.enviar_peticion(pet)
        return resp

    def consulta(self,cuenta):
        pet = peticion.Peticion('consulta',{'cuenta':cuenta})
        resp = self.cliente.enviar_peticion(pet)
        return resp
    
    def consulta_cliente(self,cuenta,contrasena):
        pet = peticion.Peticion('consulta_cliente',{'cuenta':cuenta,'contrasena':contrasena})
        resp = self.cliente.enviar_peticion(pet)
        return resp


if __name__=='__main__':
    ctrl = ControladorCliente()
