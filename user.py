


class user:

  """
  generates new user
  """
  new_user=[]

  def __init__(self,username,password):
    self.username=username
    self.password=password
    
    def store_user(self):
      """
      stores new user tonew_user list
      """
      user.new_user.append(self)

      def delete_user(self):
        
        '''
        delete_user method deletes a saved user from the new_user
        '''
        user.new_user.remove(self)