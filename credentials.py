import pyperclip

user_passwords={'twitter':'01234r',
                'instagram':'124p'
                }

repeat_condition= True

def retrieve_password():
  for site in user_passwords:
    print('-'+site)
    
    
  site_chosen=input("choose the site to retrieve your password").lower()
  password_chosen=user_passwords[site_chosen]
  pyperclip.copy(password_chosen)
  print("############################################################")
  print(site_chosen+" pasword copied")
  print("############################################################")
  print("please enter site from the list")
  


retrieve_password()
while repeat_condition:
  get_another_pasword= input("get aanother password? y/N ")

  if get_another_pasword=='y':
      retrieve_password()
  else:
      retrieve_password=False
      print("Thank you see you next time")
