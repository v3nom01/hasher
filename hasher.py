# Text To Different Hash Converting Script By v3nom01

import time
import colorama
import hashlib

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

time.sleep(2)

print(Fore.LIGHTBLUE_EX + """
██╗   ██╗██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ ██████╗  ██╗    
██║   ██║╚════██╗████╗  ██║██╔═══██╗████╗ ████║██╔═████╗███║    
██║   ██║ █████╔╝██╔██╗ ██║██║   ██║██╔████╔██║██║██╔██║╚██║    
╚██╗ ██╔╝ ╚═══██╗██║╚██╗██║██║   ██║██║╚██╔╝██║████╔╝██║ ██║    
 ╚████╔╝ ██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝ ██║    
  ╚═══╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝  ╚═╝   
-------------------------------------------------------------
                    Script by v3nom01
------------------------------------------------------------- 
""")
time.sleep(1)

def main():

    input_hash = input(Fore.LIGHTYELLOW_EX + "Enter The Text Which You Want To Convert To Hash : ")

    hashtype1 = hashlib.md5()
    hashtype1.update(input_hash.encode())
    print_md5 = hashtype1.hexdigest()

    hashtype2 = hashlib.sha256()
    hashtype2.update(input_hash.encode())
    print_sha256 = hashtype2.hexdigest()

    hashtype3 = hashlib.sha1()
    hashtype3.update(input_hash.encode())
    print_sha1 = hashtype3.hexdigest()

    hashtype4 = hashlib.sha224()
    hashtype4.update(input_hash.encode())
    print_sha224 = hashtype4.hexdigest()

    hashtype5 = hashlib.sha384()
    hashtype5.update(input_hash.encode())
    print_sha384 = hashtype5.hexdigest()

    hashtype6 = hashlib.sha3_224()
    hashtype6.update(input_hash.encode())
    print_sha3_224 = hashtype6.hexdigest()

    hashtype7 = hashlib.sha3_256()
    hashtype7.update(input_hash.encode())
    print_sha3_256 = hashtype7.hexdigest()

    hashtype8 = hashlib.sha3_384()
    hashtype8.update(input_hash.encode())
    print_sha3_384 = hashtype8.hexdigest()

    hashtype9 = hashlib.sha3_512()
    hashtype9.update(input_hash.encode())
    print_sha3_512 = hashtype9.hexdigest()


    print(Fore.WHITE + """
    md5 = '1'
    sha256 = '2'
    sha1 = '3'
    sha224 = '4'
    sha384 = '5'
    sha3_224 = '6'
    sha3_256 = '7'
    sha3_384 = '8'
    sha3_512 = '9'
    All = '10'
     """)

    method = int(input(Fore.LIGHTYELLOW_EX + "Which Encryption Method Do You Want To Use ? : "))

    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + "================= 25%")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + "============================ 50%")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + "======================================= 75%")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + "================================================== 100%")

    if method == 1:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted String (md5) : " + print_md5)

    elif method == 2:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted string (sha256) : " + print_sha256)

    elif method == 3:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted String (sha1) : " + print_sha1)

    elif method == 4:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted String (sha224) : " + print_sha224)

    elif method == 5:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted String (sha384) : " + print_sha384)

    elif method == 6:
     print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
     print(Fore.LIGHTBLUE_EX + "Converted String (sha3_224) : " + print_sha3_224)

    elif method == 7:
        print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_256) : " + print_sha3_256)

    elif method == 8:
        print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_384) : " + print_sha3_384)

    elif method == 9:
        print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_512) : " + print_sha3_512)

    elif method == 10:
        print(Fore.LIGHTBLUE_EX + "Input String : " + input_hash)
        print(Fore.LIGHTBLUE_EX + "Converted String (md5) : " + print_md5)
        print(Fore.LIGHTBLUE_EX + "Converted string (sha256) : " + print_sha256)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha1) : " + print_sha1)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha224) : " + print_sha224)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha384) : " + print_sha384)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_224) : " + print_sha3_224)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_256) : " + print_sha3_256)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_384) : " + print_sha3_384)
        print(Fore.LIGHTBLUE_EX + "Converted String (sha3_512) : " + print_sha3_512)


    else:
     print(Fore.RED + "Invalid Option Specified")

    process_terminate = str(input(Fore.LIGHTYELLOW_EX + "Do You Want To Close The Script ? (Y/n) : "))

    if process_terminate == str("n" or "N"):
         main()

    elif process_terminate == str("y" or "Y"):
        print(Fore.CYAN + "Closing The Script...")
        time.sleep(2)
        exit()
main()
