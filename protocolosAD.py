OSPF = 110
EIGRP = 90
BGP = 20
protocolo = input("Ingrese un protocolo ")
if protocolo == "OSPF":
    print(f"La distancia administrativa es {OSPF}")
elif protocolo == "EIGRP":
    print(f"La distancia administrativa es {EIGRP}")
elif protocolo == "BGP":
    print(f"La distancia administrativa es {BGP}")
else:print("Protocolo no valido")
