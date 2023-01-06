import pyfiglet as pf 
import os
os.system("cls")
print(pf.figlet_format("Logo maker" ))
name  = input("Enter name for Logo : ")
a = (pf.figlet_format(f"{name}" ))
print(a)
with open ("LOGO.txt" , "a") as f:
    f.write("================================\n")
    f.write(a)
print("[+] Your logo saved in : "+os.getcwd()+"\\"+"LOGO.txt")