import socket

# Creazione di un oggetto socket
ScK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associazione del socket all'indirizzo IP e alla porta desiderati
ScK.bind(("192.168.1.152", 80))

# Impostazione del socket in modalità di ascolto, consentendo al server di accettare connessioni in entrata
ScK.listen(1)

try:
    # Accettazione di una connessione in entrata
    conn, addr = ScK.accept()
    print(f"Connessione da {addr}")

    # Inizializzazione di una variabile per memorizzare il messaggio in arrivo
    MessaggioInArrivo = ""

    # Ricezione dei dati fino a quando il messaggio in arrivo non è "You There?"
    while(MessaggioInArrivo != "You There?"):
        MessaggioInArrivo = conn.recv(2048).decode()

    # Stampare il messaggio ricevuto
    print(f"Ricevuto: {MessaggioInArrivo}")

    # Preparazione di una risposta
    MessaggioDiRisposta = "Yes"

    # Invio della risposta al client
    conn.send(MessaggioDiRisposta.encode())

except Exception as e:
    # Gestione degli errori durante la connessione
    print(f"Errore durante la connessione: {e}")

finally:
    # Chiusura del socket dopo l'uso
    ScK.close()
    print("Socket chiuso")
