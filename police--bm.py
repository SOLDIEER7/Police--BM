import os
import pyfiglet

os.system("pip install python")
os.system('pip install python2')
os.system('pip install python3')

B = '\033[0;36m'
print()
print()
print(B+'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(B+'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
D = pyfiglet.figlet_format('Police -- BM')
print(B+D) 
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(B+'''
                                                  INSTA:@astra_x7
''')
print()

Z = '\033[1;31m' 
X = '\033[1;33m' 
B = '\033[0;36m'




print()
print(Z+'- - - - - - - - - - - - - - - - - - - - - - - - - -')
print(B+'[+]',X+"Welcome to my tool, share it with your friends")
print(Z+'- - - - - - - - - - - - - - - - - - - - - - - - - -')
print()
print()
import os
import socket
from threading import Timer



def timer():
    t = Timer(10, timer)
    t.start()


user = str(input((B+'[+]' ) + ((((X+' Enter your name: ' ))))))
print()
print(B+'[+]',X+"Welcome", user)
print()
print(Z+"________________________________________________________")
print()
print(B+'[+]',X+'My channal link( https://www.instagram.com/astra_x7/ )')
print(Z+"________________________________________________________")
print()
print()
print (Z+'_ _ _ _ _ _ _ _ _ _ _ _ _')
print()

print(B+'1-',X+"get host of ip :")

print(B+'2-',X+"get port of service :")

print(B+'3-',X+"get service of port :")

print(B+'4-',X+'geolocation ip :')

print()
print (Z+'_ _ _ _ _ _ _ _ _ _ _ _ _')
print()


def menu():
    choise = str(input((B+'[+]' ) + ((((X+' Enter your choise : ' ))))))
    print()
    print()
    print()
    print()
   
    if choise == "1":
        print(Z+'===================================================================')
        print()
        import pyfiglet
        D = pyfiglet.figlet_format('domain ip')
        print(B+D)
        
        import socket
        ip = str(input((B+'[+]')+((((X+" Enter ip :"))))))
        host = socket.gethostbyaddr(str(ip))
        print("############################")
        print(B+'[+]',X+'',host)
        
        print("############################")
        print()
        print(Z+'===================================================================')
        print()
        x = input((B+'[+]')+((((X+" Enter to exit :")))))
    
    elif choise == "2":
        print(Z+'===================================================================')
        print()
        import pyfiglet
        D = pyfiglet.figlet_format('Server port')
        print(B+D)
        import socket
        service = str(input((B+'[+]')+((((X+" Enter service: "))))))
        port = socket.getservbyname(service)
        print(B+'[+]',X+'Server port:',X+'',port)
        print()
        print(Z+'===================================================================')
        print()
        x = input((B+'[+]')+((((X+" Enter to exit :")))))
    elif choise == "3":
        import socket
        print(Z+'===================================================================')
        print()
        import pyfiglet
        D = pyfiglet.figlet_format('Port server')
        print(B+D)
        port = int(input((B+"[+]")+((((X+" Enter port: "))))))
        service_name = socket.getservbyport(port)
        print(B+'[+]',X+'Port server:',X+'',service_name)
        print()
        print(Z+'===================================================================')
        print()
        x = input((B+'[+]')+((((X+" Enter to exit :")))))

        
   
    elif choise == "4":
        import os
        print(Z+'===================================================================')
        print()
        import pyfiglet
        D = pyfiglet.figlet_format('ip locator')
        print(B+D)
        from geoip import geolite2
        ip = str(input((B+'[+]')+((((X+" Enter ip :"))))))
        locator = geolite2.lookup(ip)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>")
        print(B+'[+]',X+'',locator)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>")
        print(Z+'===================================================================')
        print()
        x = input((B+'[+]')+((((X+" Enter to exit :")))))


menu()
