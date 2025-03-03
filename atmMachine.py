print("WELCOME 🙏💳")
print("Please Insert The Card")
confirm = input("Type 'OK' (if inserted):")
import time
print('Wait a moment...')
print("===================================")
time.sleep(3)


total_cash = 500000
atm_pin = 8008


def engTerm(atm,atm_pin,total_cash):
    if (atm == atm_pin):
        print("Choose what to do?")
        print("1. Check Balance")
        print("2. Cash Withdraw")
        print("3. Cash Deposit")
        print("4. Exit")
        i = int(input("Please choose from above: ")) 
        
        match (i):
            case 1:
                print(f"Your balance is {total_cash}")
                time.sleep(1)
                engTerm(atm,atm_pin,total_cash)
            case 2:
                wa = int(input("Enter the amount: "))
                if(wa< total_cash):
                    print("Withdraw Successful")
                    total_cash = total_cash - wa
                    print(f"Your new balance is {total_cash}")
                    time.sleep(1)
                    engTerm(atm,atm_pin,total_cash)
                else:
                    print("Amount insufficient.")
                    engTerm(atm,atm_pin,total_cash)
            case 3:
                da = int(input("Enter Amount to Deposit: "))
                total_cash = total_cash+da
                print(f"Done...New balance is {total_cash}")
                engTerm(atm,atm_pin,total_cash)
            case 4:
                end()
            case _:
                engTerm(atm,atm_pin,total_cash)
            
        
    else:
        print("wrong PIN.. Start Over")
        time.sleep(2)
        atmTerm()
    
    

def nepTerm(atm,atm_pin,total_cash):
     if (atm == atm_pin):
        print("के गर्न चहानु हुन्छ?")
        print("१. रकम हेर्न")
        print("२. रकम निकालन")
        print("३. रकम जम्मा गर्न")
        print("४. बाहिर जान??")

        i = int(input("के गर्नुहुन्छ : ")) 
        
        match (i):
            case 1:
                print(f"तपाईको रकमः {total_cash}")
                time.sleep(1)
                nepTerm(atm,atm_pin,total_cash)
            case 2:
                wa = int(input("कति निकालने: "))
                if(wa< total_cash):
                    print("Withdraw Successful")
                    total_cash = total_cash - wa
                    print(f"तपाईको नँया रकमः {total_cash}")
                    time.sleep(1)
                    nepTerm(atm,atm_pin,total_cash)
                else:
                    print("रकम पुगेन।।।")
                    nepTerm(atm,atm_pin,total_cash)
            case 3:
                da = int(input("कति हालने : "))
                total_cash = total_cash+da
                print(f"भयो।।। हजुरको नँया रकम ः{total_cash}")
                nepTerm(atm,atm_pin,total_cash)
            case 4:
                end()
            case _:
                nepTerm(atm,atm_pin,total_cash)
            
        
     else:
        print("गलत पिन।।। सुरुबाट गर्नुहोस।।।")
        time.sleep(2)
        atmTerm()
    
def end():
    print("Saving progress.... please wait")
    time.sleep(5)
    print("Thank you For Being patient. Please take your card with you")


def atmTerm():
    print("Welcome to Wellsfargo Bank Terminal")
    print("Select your preferred Language")
    print("1. English")
    print("2. Nepali")
    print("3. Exit")
    ch = input("Enter your choice: ")
    if(ch =='1'):
        atm = int(input("Please Enter Your PIN :"))
        engTerm(atm,atm_pin,total_cash)
    elif(ch == '2'):
        atm = int(input("PIN हाल्नुहोस :"))
        nepTerm(atm,atm_pin,total_cash)
    else:
        end()



if(confirm.lower().strip() == 'ok'):
    atmTerm()

else:
    print("OOps Something Went Wrong! Try again Later!!")








