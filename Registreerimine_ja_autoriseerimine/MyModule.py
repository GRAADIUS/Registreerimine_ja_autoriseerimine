from random import *
def restore_password():
    while True:
        user = input("Parooli taastamiseks sisestage oma nimi: ")
        user_file = open('users.txt', 'r+', encoding='utf8')
        read_user_file = user_file.readlines()
        try:
            ind = read_user_file.index(user + "\n")
            password = input("Sisestage uus parool: ")
            if len(password) >= 6:
                password_check = input("Sisestage uus parool uuesti:")
                if password == password_check:
                    password_file = open('passwords.txt', 'r+', encoding='utf8')
                    read_password_file = password_file.readlines()
                    read_password_file.remove(read_password_file[ind])
                    read_password_file.append(password + "\n")
                    password_file.close()
                    password_file = open('passwords.txt', 'w', encoding='utf8')                                            
                    password_file.writelines(read_password_file) 
                    print("Parool muudetud.")
                    break
                else:
                    print("Parooli mittevastavus.")
            else:
                print("Parool on liiga lühike.")
            break
        except:
            print("Sellist kasutajat pole olemas.")
            break
def reg():
    username = input("Sisestage oma kasutajanimi: ")
    user_file = open('users.txt', 'r+', encoding='utf8')
    password_file = open('passwords.txt', 'a', encoding='utf8')
    read_user_file = user_file.readlines()
    IITF = read_user_file.count(username + "\n")
    if IITF == 0:
        for i in range(len(read_user_file)):
            if read_user_file[i].rstrip() != username:
                or_ = input("kas soovite ise parooli luua?  (jah/ei): ")
                if or_.upper() == "JAH":                    
                    while True:
                        password = input("Sisestage parool: ")
                        if len(password) >= 6:
                            password_check = input("Sisestage parool uuesti: ")
                            if password == password_check:
                                user_file.write(username + "\n")
                                password_file.write(password + "\n")
                                print("Konto loodud.")
                                break
                            else:
                                print("Parooli mittevastavus.")
                        else:
                            print("Parool on liiga lühike.")
                    break
                elif or_.upper() == "EI":
                    str0=".,:;!_*-+()/#¤%&"
                    str1 = '0123456789'
                    str2 = 'qwertyuiopasdfghjklzxcvbnm'
                    str3 = str2.upper()
                    str4 = str0+str1+str2+str3
                    ls = list(str4)
                    shuffle(ls)
                    psword = ''.join([choice(ls) for x in range(12)])
                    print(f"Teie parool:{psword}")
                    user_file.write(username + "\n")
                    password_file.write(psword + "\n")
                    print("Konto loodud.")
                    break
    else:
        print("See kasutaja on juba olemas.")            
def aut():
    username = input("Sisestage oma kasutajanimi: ")
    user_file = open('users.txt', 'r+', encoding='utf8')
    read_user_file = user_file.readlines()
    for i in range(len(read_user_file)):
        if read_user_file[i].rstrip() == username:
            mistakes = 0
            while True:
                password = input("Sisestage parool: ")
                password_file = open('passwords.txt', 'r+', encoding='utf8')
                read_password_file = password_file.readlines()
                if read_password_file[i].rstrip() == password:
                    print("Tere tulemast")
                    while True:
                        exit_ = input("Kui soovite oma kontolt välja logida, kirjutage 'välja':")
                        if exit_.upper() ==  "VÄLJA":
                            break
                        else:
                            pass
                    break
                else:                
                    print("vale salasõna.")
                    if mistakes == 3:
                        restore = input("Kas taastada parool? (jah/ei): ")
                        if restore.upper() == "JAH":
                            restore_password()
                            break
                        elif restore.upper() == "EI":
                            pass
                    else:
                        mistakes += 1
            break
        else:
            pass
def update():
    old_username = input("Sisestage oma kasutajanimi: ")
    user_file = open('users.txt', 'r+', encoding='utf8')
    read_user_file = user_file.readlines()
    for i in range(len(read_user_file)):
        if read_user_file[i].rstrip() == old_username:
            mistakes = 0
            while True:
                old_password = input("Sisestage parool: ")
                password_file = open('passwords.txt', 'r', encoding='utf8')
                read_password_file = password_file.readlines()
                if read_password_file[i].rstrip() == old_password:
                    username = input("sisesta oma uus kasutajanimi: ")
                    for i in range(len(read_user_file)):
                        if read_user_file[i].rstrip() != username:
                            while True:
                                password = input("Sisestage parool: ")
                                if len(password) >= 6:
                                    password_check = input("Sisestage parool uuesti: ")
                                    if password == password_check:
                                        ind =  read_user_file.index(old_username + "\n")
                                        read_user_file.remove(old_username + "\n")
                                        read_password_file.remove(read_password_file[ind])
                                        read_user_file.append(username + "\n")
                                        read_password_file.append(password + "\n")
                                        user_file.close()
                                        password_file.close()
                                        user_file = open('users.txt', 'w', encoding='utf8')
                                        password_file = open('passwords.txt', 'w', encoding='utf8')                                            
                                        password_file.writelines(read_password_file)
                                        user_file.writelines(read_user_file)                                          
                                        print("Konto muudetud.")
                                        break
                                    else:
                                        print("Parooli mittevastavus.")
                                else:
                                    print("Parool on liiga lühike.")
                            break
                    break
                else:                
                    print("vale salasõna.")
                    if mistakes == 3:
                        restore = input("Kas taastada parool? (jah/ei): ")
                        if restore.upper() == "JAH":
                            restore_password()
                            break
                        elif restore.upper() == "EI":
                            pass
                    else:
                        mistakes += 1
            break
        else:
            pass