class CuentaBancaria:

    def __init__(self, titular: str, numero_cuenta: str, saldo: float) -> None:
        self.titular: str = titular
        self.numero_cuenta: str = numero_cuenta
        self.saldo: float = saldo


    def ingresar(self, cantidad: float) -> None:
        if cantidad > 0:
            self.saldo = self.saldo + cantidad


    def retirar(self, cantidad: float) -> bool:
        if self.saldo >= cantidad and cantidad > 0:
            self.saldo = self.saldo - cantidad
            return True
        else:
            print(f"Saldo: {self.saldo} € insuficiente")
            return False

    
    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self.titular}, Cuenta: {self.numero_cuenta}, Saldo: {self.saldo} €")


cuenta_001 = CuentaBancaria("Ana", "ES01-4587-5749", 500)
cuenta_001.mostrar_informacion()
cuenta_001.ingresar(200)
cuenta_001.retirar(800)
cuenta_001.retirar(150)
cuenta_001.mostrar_informacion()