class CuentaCorriente():
    titular = ""
    saldo = 0.0
    cuenta = 0

    def __init__(self, titular, cuenta, saldo=None):
        self.titular = titular
        self.saldo = saldo
        self.cuenta = cuenta

    def getTitular(self):
        return self.titular
    def getCuenta(self):
        return self.cuenta
    def getSaldo(self):
        return self.saldo

    def setTitular(self, titular):
        self.titular = titular
    def setCuenta(self,cuenta):
        self.cuenta = cuenta
    def setSaldo(self,saldo):
        self.saldo = saldo

    def conFormato(self):
        print("Titular:",self.titular,"-","Cuenta:", self.cuenta, "-", "Saldo:",self.saldo)

    def abonar(self, saldo):
        self.saldo += saldo

    def cargar(self, saldo):
        self.saldo -= saldo
print("Cargo y Abono positivo")    
cuenta1 = CuentaCorriente('Diego Sepulveda',str("12323435"), 25.000)
cuenta1.conFormato()
print("abono $10.000")
cuenta1.abonar(10.000)
cuenta1.conFormato()
print("cargo -$20.000")
cuenta1.cargar(20.000)
cuenta1.conFormato()
print("El titular de la cuenta es:",cuenta1.getTitular(),"-","La cuenta es:",cuenta1.getCuenta(),"-","El saldo es:",cuenta1.getSaldo())

print("Cargo y Abono negativo")
cuenta2 = CuentaCorriente('Diego Sepulveda',str("12323435"), 25.000)
cuenta2.conFormato()
cuenta2.abonar(-10.000)
cuenta2.conFormato()
cuenta2.cargar(-20.000)
cuenta2.conFormato()
print("El titular de la cuenta es:",cuenta2.getTitular(),"-","La cuenta es:",cuenta2.getCuenta(),"-","El saldo es:",cuenta2.getSaldo())

print("Cargo y Abono null")
cuenta3 = CuentaCorriente('Diego Sepulveda',str("12323435"), 25.000)
cuenta3.conFormato()
cuenta3.abonar(0000)
cuenta3.conFormato()
cuenta3.cargar(0000)
cuenta3.conFormato()
print("El titular de la cuenta es:",cuenta3.getTitular(),"-","La cuenta es:",cuenta3.getCuenta(),"-","El saldo es:",cuenta3.getSaldo())



