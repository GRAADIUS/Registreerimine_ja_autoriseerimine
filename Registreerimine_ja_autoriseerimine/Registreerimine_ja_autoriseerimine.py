from MyModule import *
def main():
    while True:    
        print("Programmeerija ei vastuta teie failide eest!")
        read = input("sisestage sisselogimiseks '1'\nregistreerumiseks sisestage '2'\nsisestage '3' parooli ja kasutajanime muutmiseks\nsisestage '4', kui unustasite parooli\nprogrammist väljumiseks sisestage '5'\n")
        if read == "1":
            aut()
        elif read == "2":
            reg()
        elif read == "3":
            update()
        elif read == "4":
            restore_password()
        elif read == "5":
            break
        else:
            print("Vale väärtus.")

main()