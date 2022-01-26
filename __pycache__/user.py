class user:

  """
  Generates new instance of use
  """

user_list=[]

def __init__(self,user_name,password):
  self.username=user_name
  self.password=password

  def storeuser(self):
    """
    stores new users to the user list
    """
    user.user_list.append(self)