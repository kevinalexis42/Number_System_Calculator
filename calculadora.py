import re

def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
CALCULADURA DE SISTEMAS NUMERICOS\n
MENU DE OPCIONES\n
2 - Binario\n
8 - Octal\n
10 - Decimal\n
16 - Hexadecimal\n
Por favor selecciona en que sistema deseas trabajar: """   )
    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return
    numero1 = input(
        f"Ok, vas a trabajar con la base " + base_origen + " \nIngresa el primer numero: ")
    numero2 = input(
        f"\nIngresa el segundo numero: ")
    
    opciones = ["1", "2", "3", "4", ]
    operaciones = input("""
OPERACIONES SOPORTADAS\n
1-SUMA
2-RESTA
3-MULT
4-DIVISION\n
Por favor selecciona que operacion vas a realizar: """   )
    if operaciones not in opciones:
        print("Opcion erronea")
        return
    return (base_origen, numero1, numero2, operaciones)


def obtener_numero_decimal(base_origen, numero1, numero2, operaciones):
    
    if base_origen == "2" and operaciones == "1":
        return suma_bin(numero1, numero2)
    elif base_origen == "2" and operaciones == "2":
        return rest_bin(numero1, numero2)
    elif base_origen == "2" and operaciones == "3":
        return mult_bin(numero1, numero2)
    elif base_origen == "2" and operaciones == "4":
        return div_bin(numero1, numero2)
    
    elif base_origen == "8" and operaciones == "1":
        return suma_oct(numero1, numero2)
    elif base_origen == "8" and operaciones == "2":
        return rest_oct(numero1, numero2)
    elif base_origen == "8" and operaciones == "3":
        return mult_oct(numero1, numero2)
    elif base_origen == "8" and operaciones == "4":
        return div_oct(numero1, numero2)
    
    
    elif base_origen == "10" and operaciones == "1":
        return suma_dec(numero1, numero2)
    elif base_origen == "10" and operaciones == "2":
        return resta_dec(numero1, numero2)
    elif base_origen == "10" and operaciones == "3":
        return multiplicacion_dec(numero1, numero2)
    elif base_origen == "10" and operaciones == "4":
        return division_dec(numero1, numero2)
    
    
    elif base_origen == "16" and operaciones == "1":
        return sum_hex(numero1, numero2)
    elif base_origen == "16" and operaciones == "2":
        return rest_hex(numero1, numero2)
    elif base_origen == "16" and operaciones == "3":
        return mult_hex(numero1, numero2)
    elif base_origen == "16" and operaciones == "4":
        return div_hex(numero1, numero2)
    
    
def suma_bin(numero1, numero2):
    sum = bin(int(numero1, 2) + int(numero2, 2)) 
    print("\n"+sum[2:]+"\n") 

def suma_oct(numero1, numero2):
    sum = oct(int(numero1, 8) + int(numero2, 8)) 
    print("\n"+sum[2:]+"\n")  
    
def sum_hex(numero1, numero2):
    sum = hex(int(numero1, 16) + int(numero2, 16)) 
    print("\n"+sum[2:]+"\n") 

def rest_bin(numero1, numero2):
    sum = bin(int(numero1, 2) - int(numero2, 2)) 
    print("\n"+sum[2:]+"\n") 

def rest_oct(numero1, numero2):
    sum = oct(int(numero1, 8) - int(numero2, 8)) 
    print("\n"+sum[2:]+"\n")

def rest_hex(numero1, numero2):
    sum = hex(int(numero1, 16) - int(numero2, 16)) 
    print("\n"+sum[2:]+"\n")
    
def mult_bin(numero1, numero2):
    Multiplication = int(numero1, 2) * int(numero2, 2)
    binaryMul = bin(Multiplication)
    binaryMul = str(binaryMul)
    binaryRes = re.sub("0b", "", binaryMul)
    print("\nResult = " + binaryRes + "\n")
    
def mult_oct(numero1, numero2):
    Multiplication = int(numero1, 8) * int(numero2, 8)
    octMul = oct(Multiplication)
    octRes = re.sub("0o", "", octMul)
    print("\nResult = " + octRes + "\n")
    
def mult_hex(numero1, numero2):
    Multiplication = int(numero1, 16) * int(numero2, 16)
    hexMul = hex(Multiplication)
    hexRes = re.sub("0x", "", hexMul)
    print("\nResult = " + hexRes + "\n")

def div_bin(numero1, numero2):
    Division = int(int(numero1, 2) / int(numero2, 2))
    binaryDiv = bin(Division)
    binaryDiv = str(binaryDiv)
    binaryRes = re.sub("0b", "", binaryDiv)
    print("\nResult = " + binaryRes + "\n")
    
def div_oct(numero1, numero2):
    Division = int(int(numero1, 8) / int(numero2, 8))
    octDiv = oct(Division)
    octDiv = str(octDiv)
    octRes = re.sub("0o", "", octDiv)
    print("\nResult = " + octRes + "\n")
    
def div_hex(numero1, numero2):
    Division = int(int(numero1, 16) / int(numero2, 16))
    hexDiv = hex(Division)
    hexDiv = str(hexDiv)
    hexRes = re.sub("0x", "", hexDiv)
    print("\nResult = " + hexRes + "\n")
    
#operaciones decimales
def suma_dec(numero1, numero2):
    sum = int(numero1) + int(numero2)
    print("\n"+str(sum)+"\n")
    
def resta_dec(numero1, numero2):
    res = int(numero1) - int(numero2)
    print("\n"+str(res)+"\n")
    
def multiplicacion_dec(numero1, numero2):
    Multiplicacion = int(numero1) * int(numero2)
    print("\n"+str(Multiplicacion)+"\n")
    
def division_dec(numero1, numero2):
    Division = int(numero1) / int(numero2)
    print("\n"+str(Division)+"\n")


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
    if datos:
        base_origen, numero1, numero2, operaciones = datos
        numero_decimal = obtener_numero_decimal(base_origen, numero1, numero2, operaciones)