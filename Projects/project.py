import os
import hashlib

def cryptPassword(password):
  return hashlib.sha256(password.encode()).hexdigest()

def readLineFunction(f):
    id_line = f.readline()
    if not id_line:
        return None

    name_line = f.readline()
    gender_line = f.readline()
    balance_line = f.readline()
    password_line = f.readline()

    if not (name_line and gender_line and balance_line and password_line):
        return None

    return {
        "id": id_line.strip(),
        "name": name_line.strip(),
        "gender": gender_line.strip(),
        "balance": balance_line.strip(),
        "password": password_line.strip()
    }

def writeRecord(file, account):
  file.write(account["id"] + "\n")
  file.write(account["name"] + "\n")
  file.write(account["gender"]  + "\n")
  file.write(account["balance"] + "\n")
  file.write(account["password"] + "\n")

# def loadAccounts(): 
#   accounts = []
#   if not os.path.exists("client.txt"):
#     return accounts
#   with open("client.txt", "r") as f:
#     while True:
#       account = readLineFunction(f)
#       if account is None:
#         break
#       accounts.append(account)
#   return accounts

# def saveAccounts(accounts):
#   with open("client.txt", "w") as f:
#     for account in accounts:
#       writeRecord(f, account)

def createAccount(id, name, gender, balance, password):
  try:
    f = open("client.txt", "a")
    f.write(str(id)+"\n")
    f.write(name+"\n")
    f.write(gender+"\n")
    f.write(str(balance)+"\n")
    f.write(cryptPassword(password)+"\n")
    f.close()
    print(f"\n{'SAVED SUCCESSFULLY :)':>35}")
  except Exception as e:
    print(f"{'NOT SAVED :(':>25}", e)

def showAccountDetails():
  if not os.path.exists("client.txt"):
    print("No accounts found :(")
    return
  
  f = open("client.txt", "r")
  while True:
    account = readLineFunction(f)
    if account is None:
      break
    print(f"\n{'='*39:>46}")
    print(f"{'ID':>16}: {account['id']}")
    print(f"{'Name':>18}: {account['name']}")
    print(f"{'Gender':>20}: {account['gender']}")
    print(f"{'Balance':>21}: {account['balance']}")
    print(f"{'Password':>22}: {account['password']}")

  f.close()

def updateAccount(id, password):
  if not os.path.exists("client.txt"):
    print("No accounts found :(")
    return
  
  try:
    f = open("client.txt", "r")
    temp = open("temp.txt", "w")
    updated = False
    while True:
      account = readLineFunction(f)
      if account is None:
        break

      if account["id"] == str(id):
        if account["password"] == cryptPassword(password):
          updated = True
          ID = int(input(f"\n{'Enter your new ID:':>32} "))
          Name = input(f"{'Enter your new Name:':>34} ")
          Gender = input(f"{'Enter your new Gender:':>36} ")
          Balance = float(input(f"{'Enter your new Balance:':>37} "))
          Password = input(f"{'Set your new password:':>36} ")
          new_account = {
            "id": str(ID),
            "name": Name,
            "gender": Gender,
            "balance": str(Balance),
            "password": cryptPassword(Password)
          }
          writeRecord(temp, new_account)
        else:
          writeRecord(temp, account)
          print(f"{'Password Incorrect :(':>35}")
      else:
          writeRecord(temp, account)

    f.close()
    temp.close()

    os.remove("client.txt")
    os.rename("temp.txt", "client.txt")

    if updated:
      print(f"{'Account Updated Successfully :)':>45}")
    else:
      print(f"{'Account Not Updated :(':>36}")
  except Exception as e:
    print(f"{'Update Unsuccessful :(':>36}", e)

def deposit(id, password, amount):
  if not os.path.exists("client.txt"):
    print("No accounts found :(")
    return
  
  try:
    f = open("client.txt", "r")
    temp = open("temp.txt", "w")
    found = False
    while True:
      account = readLineFunction(f)
      if account is None:
        break

      if account["id"] == str(id):
        found = True
        if account["password"] == cryptPassword(password):
          new_balance = float(account["balance"]) + amount
          account["balance"] = str(new_balance)
          writeRecord(temp, account)
          print(f"{'Deposit successful :) ! New balance':>49}: {new_balance}")
        else:
          writeRecord(temp, account)
          print(f"{'Password Incorrect :(':>35}")
      else:
          writeRecord(temp, account)


    f.close()
    temp.close()

    os.remove("client.txt")
    os.rename("temp.txt", "client.txt")

    if not found:
      print(f"{'Account not found :(':>34}")

  except Exception as e:
    print(f"{'Deposit Unsuccessful :(':>38}", e)

def withdrawal(id, password, amount):
    if not os.path.exists("client.txt"):
      print("No accounts found :(")
      return

    try:
      f = open("client.txt", "r")
      temp = open("temp.txt", "w")
      found = False
      while True:
        account = readLineFunction(f)
        if account is None:
          break

        if account["id"] == str(id):
          found = True
          if account["password"] == cryptPassword(password):
            if float (account["balance"]) >= amount:
              new_balance = float(account["balance"]) - amount
              account["balance"] = str(new_balance)
              writeRecord(temp, account)
              print(f"{'Withdrawal successful :) ! New balance':>49}: {new_balance}")
            else:
              writeRecord(temp, account)
              print(f"{'Insufficient balance :(':>35}")
            
          else:
            writeRecord(temp, account)
            print(f"{'Password Incorrect :(':>35}")
        else:
          writeRecord(temp, account)


      f.close()
      temp.close()

      os.remove("client.txt")
      os.rename("temp.txt", "client.txt")

      if not found:
        print(f"{'Account not found :(':>34}")

    except Exception as e:
      print(f"{'Withdrawal Unsuccessful :(':>35}", e)

def searchForAccount(id, password):
  if not os.path.exists("client.txt"):
    print("No accounts found :(")
    return
  
  try:
    f = open("client.txt", "r")
    found = False
    while True:
      account = readLineFunction(f)
      if account is None:
        break

      if account["id"] == str(id):
        found = True
        if account["password"] == cryptPassword(password):
          print(f"{'Account found successfully :)':>43}")
          print(f"{'Name':>18} : {account['name']}")
          print(f"{'Gender':>20} : {account['gender']}")
          print(f"{'Balance':>21} : {account['balance']}")
        else:
          print(f"{'Password Incorrect :(':>35}")
          break
        

    f.close()

    if not found:
      print(f"{'Account not found':>31}")

  except Exception as e:
    print(f"{'Search Unsuccessful :(':>35}", e)

def deleteAccount(id, password):
  if not os.path.exists("client.txt"):
    print("No accounts found :(")
    return
  
  try:
    f = open("client.txt", "r")
    temp = open("temp.txt", "w")
    found = False
    deleted = False
    while True:
      account = readLineFunction(f)
      if account is None:
        break

      if account["id"] == str(id):
        found = True
        if account["password"] == cryptPassword(password):
          deleted = True
          print(f"{'Account deleted successfully :)':>45}")
        else:
          writeRecord(temp, account)
          print(f"{'Password Incorrect :(':>35}")
      else:
          writeRecord(temp, account)
      
    f.close()
    temp.close()
    os.remove("client.txt")
    os.rename("temp.txt", "client.txt")

    if deleted == True:
      print(f"{'Account deleted successfully :)':>45}")

  except Exception as e:
    print(f"{'Deletion Unsuccessful :(':>35}", e)

while(True):
  choice = int(input('''
       =======================================           
              1) Create an Account            
              2) Show Account Details
              3) Update              
              4) Deposit 
              5) Withdraw     
              6) Search for an Account          
              7) Delete an Account
              8) Exit                             
       =======================================
              Enter your choice: '''))
  
  match choice:
    case 1:
      print(f"{'='*39:>46}")

      while True:
        try:
            print(f"\n{'='*39:>46}")
            ID = int(input(f"{'Enter your ID:':>28} "))

            duplicate = False
            if os.path.exists("client.txt"):
              f = open("client.txt", "r")
              while True:
                account = readLineFunction(f)
                if account is None:
                  break
                if account["id"] == str(ID):
                  duplicate = True
                  break
              f.close()

            if duplicate == True:
              print(f"{'Error: Account with this ID already exists :)':>59}")
            else:
              break

        except Exception as e:
            print(f"{'Invalid ID! Please enter numbers only :(':>54}", e)

      while True:
        Name = input(f"{'Enter your Name:':>30} ")
        if Name == "":
          print(f"{'Invalid Name! Please enter a valid name :(':>55}")
          print(f"\n{'='*39:>46}")
        else:
          break

      while True:
        Gender = input(f"{'Enter your Gender:':>32} ")
        if Gender.lower() in ["male", "female", "m", "f"]:
          break
        else:
          print(f"{'Invalid Gender! Please enter Male or Female only :(':>65}")
          print(f"\n{'='*39:>46}")

      while True:
        try:
          Balance = float(input(f"{'How much money you want to save?':>46} "))
          if Balance <=0:
            print(f"{'Invalid Amount :(':>35}")
            print(f"\n{'='*39:>46}")
          else:
            break
        except Exception as e:
          print(f"{'Invalid Amount! Please enter numbers only :(':>58}", e)
        
      Password = input(f"{'Set your account password:':>40} ")
      createAccount(ID, Name, Gender, Balance, Password)
      print(f"\n{'='*39:>46}")
    case 2:
      print(f"{'='*39:>46}")
      showAccountDetails()
      print(f"{'='*39:>46}")
    case 3:
      print(f"{'='*39:>46}")
      ID = int(input(f"\n{'Enter your ID:':>28} "))
      Password = input(f"{'Enter your account password:':>42} ")
      updateAccount(ID, Password)
      print(f"{'='*39:>46}")
    case 4:
      print(f"{'='*39:>46}")
      ID = int(input(f"\n{'Enter your ID:':>28} "))
      Password = input(f"{'Enter your account password:':>42} ")
      while True:
        try:
          Amount = float(input(f"{'Enter the amount you want to deposit:':>51} "))
          if Amount <= 0:
            print(f"{'Invalid Amount :(':>35}")
            print(f"{'='*39:>46}")
            break
          else:
            deposit(ID, Password, Amount)
            print(f"{'='*39:>46}")
        except Exception as e:
          print(f"{'Invalid Amount! Please enter numbers only :(':>58}", e)
          print(f"{'='*39:>46}")
    case 5:
      print(f"{'='*39:>46}")
      ID = int(input(f"\n{'Enter your ID:':>28} "))
      Password = input(f"{'Enter your account password:':>42} ")
      while True:
        try:
          Amount = float(input(f"{'Enter the amount you want to withdraw:':>52} "))
          if Amount <= 0:
            print(f"{'Invalid Amount :(':>35}")
            print(f"{'='*39:>46}")
          else:
            withdrawal(ID, Password, Amount)
            print(f"{'='*39:>46}")
            break
        except Exception as e:
          print(f"{'Invalid Amount! Please enter numbers only :(':>58}", e)
          print(f"{'='*39:>46}")      
    case 6:
      print(f"{'='*39:>46}")
      ID = int(input(f"\n{'Enter your ID:':>28} "))
      Password = input(f"{'Enter your account password:':>42} ")
      searchForAccount(ID, Password)
      print(f"{'='*39:>46}")
    case 7:
      print(f"{'='*39:>46}")
      ID = int(input(f"\n{'Enter your ID:':>28} "))
      Password = input(f"{'Enter your account password:':>42} ")
      deleteAccount(ID, Password)
      print(f"{'='*39:>46}")
    case 8:
      print(f"{'='*39:>46}")
      print(f"{'Program Terminated! Goodbye :)':>44}")
      break
    case _:
      print(f"{'='*39:>46}")
      print(f"{'Error! Try Again':>30}")
      print(f"{'='*39:>46}")