import random
from credentials import credentials;
from user import user


def main():
  while True:
    print("Password manager")
    print('\n')
    print("write 'y'to create a new user account: write 'N' to login to your account type 'exit' to exit the system ")
    access_code=input().lower()
    print('\n')

    if access_code =='y':
      print("enter username")
      new_user_name=input()
      print("Welcome"+' '+new_user_name+' '+"Please enter your password")
      new_user_password=input()
      print("Welcome"+' ' + new_user_name+' '+"account succesfully created." )
    else:
      access_code='N'
      print("please login")
      print("Enter username")
      entered_username=input()
      print("enter password")
      entered_password=input()

      while entered_username==new_user_name and entered_password==new_user_password:
        print("login succesfull")
      else:
         access_code=='exit'
         break

  if__name__='__main__'
  main()