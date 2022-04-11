import random
import time
import webbrowser

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "`~!@#$%^&*()_-+=[{]}\|;:,<.>/?"

Use_for = lower_case + upper_case + number + symbols

def repeat():
    input_var2 = input("Would you like to generate another password? (Y for Yes, Any Other Key for No): ")
    if input_var2.lower() == "y":
      while True:
         try:
           input_var = int(input("How many characters would you like your password to be? Enter amount of characters: ")) 
         except ValueError:
                print("Invalid Value! Please try again!")
                time.sleep(2)
                continue
         else:
                if input_var > 0 and input_var <= 90:
                     print("Characters selected: " + str(input_var))
                     time.sleep(3)
                     print("Generating password...")
                     time.sleep(3)

                     password = "".join(random.sample(Use_for, input_var))

                     print("Your New Generated Password is: " + password)
                     time.sleep(3)
                     input_var3 = input("Would you like to save this password to a file? (Y for Yes, Any Other Key for No): ")
                     if input_var3.lower() == "y":
                          try: 
                               f = open("Passwords.txt", "w")
                               f.write("Password Generated: " + password)
                               f.close()
                               time.sleep(3)
                               print("Passwords File has been modified!")
                               time.sleep(3)
                               repeat()
                               break  
                          except IOError: 
                               print("Failed to modify file!")
                               print("Error Code: " + str(IOError))
                               time.sleep(3)
                               repeat()
                               break         
                     else: 
                          repeat()    
                          break
                else:
                     print("Invalid Amount of Digits! Please try again!")
                     time.sleep(2)
                     continue  
    else:
     print("Thank you for using Password Generator! Exiting now...")
     time.sleep(4)
     webbrowser.open("https://www.google.com/search?q=Thank+you+for+using+Password+Generator%21&rlz=1C1VDKB_enUS969US969&sxsrf=APq-WBvfz46EX8Pbvu_fdZI3GFuS_7vTRA%3A1648343853459&ei=Lbs_YvHZG9CckPIPxqmGyAM&ved=0ahUKEwixpOmuj-X2AhVQDkQIHcaUATkQ4dUDCA4&uact=5&oq=Thank+you+for+using+Password+Generator%21&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BwgjELACECdKBAhBGABKBAhGGABQnAlYlRFgtBZoAXABeACAAc0BiAH9CZIBBTAuNS4ymAEAoAEByAEIwAEB&sclient=gws-wiz")
     quit() 

print("Welcome to Password Generator! Initializing program...")
time.sleep(5)
while True:
    try:
     input_var = int(input("How many characters would you like your password to be? Enter amount of characters: ")) 
    except ValueError:
           print("Invalid Value! Please try again!")
           time.sleep(2)
           continue
    else:
           if input_var > 0 and input_var <= 90:
                print("Characters selected: " + str(input_var))
                time.sleep(3)
                print("Generating password...")
                time.sleep(3)

                password = "".join(random.sample(Use_for, input_var))

                print("Your New Generated Password is: " + password)
                time.sleep(3)
                input_var3 = input("Would you like to save this password to a file? (Y for Yes, Any Other Key for No): ")
                if input_var3.lower() == "y":
                     try: 
                          f = open("Passwords.txt", "w")
                          f.write("Password Generated: " + password)
                          f.close()
                          time.sleep(3)
                          print("Passwords File has been modified!")
                          time.sleep(3)
                          repeat()
                          break 
                     except IOError:
                      print("Failed to modify file!")
                      print("Error Code: " + str(IOError))
                      time.sleep(3)
                      repeat()
                      break        
                else:    
                     repeat()
                     break    
           else:
                print("Invalid Amount of Digits! Please try again!")
                time.sleep(2)
                continue        




