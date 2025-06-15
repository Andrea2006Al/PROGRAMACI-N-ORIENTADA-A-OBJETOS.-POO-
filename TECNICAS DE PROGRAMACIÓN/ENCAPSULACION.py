class CuentaBancaria:
    def __init__(self, saldo_inicial):
        # Atributo privado
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        """Aumenta el saldo de la cuenta"""
        if monto > 0:
            self.__saldo += monto
            print(f"Se depositaron ${monto}.")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        """Disminuye el saldo si hay fondos suficientes"""
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se retiraron ${monto}.")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        """Devuelve el saldo disponible"""
        return self.__saldo

# Prueba del programa
if __name__ == "__main__":
    cuenta = CuentaBancaria(100)
    cuenta.depositar(50)
    cuenta.retirar(30)
    print(f"Saldo actual: ${cuenta.mostrar_saldo()}")
