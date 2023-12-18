import socket

ScK = socket.socket()

try:
    ScK.connect(("192.168.1.152", 80))

    print(ScK)

    richiesta = "You There?"
    ScK.send(richiesta.encode())

    risposta = ScK.recv(2048).decode()
    
    # Ricevi ulteriori dati solo se la risposta non è "Yes"
    while risposta != "Yes":
        risposta = ScK.recv(2048).decode()

    print(risposta)

except Exception as e:
    print(f"Errore durante la connessione: {e}")

finally:
    ScK.close()
    print("Socket chiuso")
