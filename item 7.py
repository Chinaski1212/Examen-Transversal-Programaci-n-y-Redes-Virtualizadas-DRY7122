#.Item 7. Ej N°1
#Configurar EIGRP Nombrado a nivel IPv4/IPv6 con AS a elección. Debe configurar interfaces pasivas respectivas y debe
#mostrar el resultado con el comando show running-config | section eigrp

from netmiko import ConnectHandler
import time

print("Configuracion EIGRP IPv4/IPv6 en CSR1000v cisco")
time.sleep(1)
ipp = input("Ingresar IP del Router CSR1000v a configurar:")
time.sleep(0.5)
name = input("Definir nombre del proceso EIGRP a crear:")
ip_wild = input("Agregar IPv4/IPv6 con su Wildcard para EIGRP:")
conexion = ConnectHandler( 
    device_type="cisco_ios",
    host = ipp, 
    port=22, username="cisco", 
    password="cisco123!")


crear=["router eigrp "+name,
 "address-family ipv4 unicast autonomous-system 1",
  "af-interface default",
   "passive-interface",
  "exit-af-interface",
  "af-interface GigabitEthernet2",
   "no passive-interface",
  "exit-af-interface",
  "network "+ip_wild,
 "exit-address-family"]

salida_comando = conexion.send_config_set(crear)
salida=conexion.send_command("show running-config | section eigrp")
print("\n{}n".format(salida))
