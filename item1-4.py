opcionesmenu = 0
while opcionesmenu != 1:
    print("-----Detector rango VLANs-----")
    print("\n")
    vlan_usuario = int(input("Ingrese el numero de VLAN en formato numerico: "))
    print("\n")
    if vlan_usuario >= 1 and vlan_usuario <= 1005:
        print(f"{vlan_usuario} es una VLAN de rango normal.")

    elif vlan_usuario >= 1006 and vlan_usuario <= 4094:
        print(f"{vlan_usuario} es una vlan de rango extendido.")
        
    entradausuario = input("Presione Enter para volver a ingresar una VLAN o 'S' para salir: ")
    if entradausuario.upper() == "S":
        opcionesmenu = 1