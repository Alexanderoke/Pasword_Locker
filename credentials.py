from sre_parse import REPEAT_CHARS
from keyring import get_password
import pyperclip

user_passwords={'twitter':'01234r',
                'instagram':'124p'
                }

repeat_condition= True

def retrieve_password():
  for site in user_passwords:
    print('-'+site)

    try:
      site_chosen=input("choose the site to retrieve your password")
      