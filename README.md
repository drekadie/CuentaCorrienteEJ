# CuentaCorrienteEJ
Ej en python de codigo de cuenta corriente:

equerimientos:

REQ01: En un proyecto crea una clase y nómbrala CuentaCorriente, que tendrá los siguientes atributos: titular (cadena de texto), saldo (numérico con decimales) y número (numérico).
REQ02: El titular y el número serán obligatorios, el saldo es opcional. Crea los constructores que cumplan lo anterior.
REQ03: Crea métodos get/set para los atributos, y uno toString que muestre los atributos de la clase en una cadena de texto con formato.
REQ04: Tendrá dos métodos extra:
●        abonar: recibe por parámetro la cantidad que se debe abonar al saldo de la cuenta. Si la cantidad es un número negativo, no se debe alterar el saldo.

●        cargar: recibe por parámetro la cantidad que se debe cargar al sado de la cuenta. Si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.

REQ05: Instancie la clase y consuma los métodos para probar los siguientes casos:
Cargo y Abono positivo.
Cargo y Abono negativo.
Cargo y Abono null.
Instanciación de clase CuentaCorriente solo con parámetros obligatorios.
Instanciación de clase CuentaCorriente con todos los parámetros.
Utilización de métodos get/set.
