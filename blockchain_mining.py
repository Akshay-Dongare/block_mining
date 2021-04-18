from hashlib import sha256
import time

def menu():
    print("1. DEFAULT MODE")
    print("2. CUSTOM MODE")
    print("3. QUIT PROGRAM")

    try:
        SELECTION=int(input("Choose a mode: "))
        if SELECTION==1:
            TRANSACTIONS="akshay->nikita -> 20 BTC nikita-> ashutosh -> 5 BTC vrunda -> akshay -> 10 BTC"
            DIFFICULTY=5
            MAX_NONCE = 1000 ** 1000
            BLOCK_NUMBER = 5
            PREVIOUS_HASH = 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
            NEW_HASH = mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY, MAX_NONCE)
            print(NEW_HASH)

        elif SELECTION==2:
            #take user inputs for custom mode 
            TRANSACTIONS= input("Enter transactions: ")
            DIFFICULTY=int(input("Enter difficulty(prefix zeros): "))
            MAX_NONCE = int(input("Enter max nounce: "))
            BLOCK_NUMBER = int(input("Enter block number: "))
            PREVIOUS_HASH = input("Enter previous hash: ")
            NEW_HASH = mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY, MAX_NONCE)
            print(NEW_HASH)
    
        elif SELECTION==3:
            pass   
        else:
            print("INVALID CHOICE. ENTER 1-3")
            menu()
                    
    except ValueError:
        print("INVALID CHOICE. ENTER 1-3")
        menu()
 

def SHA256(TEXT):
    return sha256(TEXT.encode("ascii")).hexdigest()

def mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY,MAX_NONCE):
    mineSTART=time.time()
    print("MINING HAS STARTED")
    for NONCE in range(MAX_NONCE):
        TEXT=str(BLOCK_NUMBER)+ TRANSACTIONS + PREVIOUS_HASH + str(NONCE)
        NEW_HASH=SHA256(TEXT)
        if NEW_HASH.startswith('0'* DIFFICULTY):
            print(f"SUCCESSFULLY MINED CRYPTOCURRENCY WITH NONCE VALUE: {NONCE}")
            TOTAL_TIME=(time.time()-mineSTART)
            print(f"MINING COMPLETE! MINING TOOK: {TOTAL_TIME} SECONDS")
            return NEW_HASH
    raise BaseException(f"COULD NOT FIND CORRECT HASH AFTER TRYING {MAX_NONCE} TIMES")

if __name__=='__main__':
    menu()