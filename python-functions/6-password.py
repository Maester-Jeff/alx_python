def validate_password(password):
  #First we must check the password length so that if that is not satisfied no need for the check to continue
  if len(password) < 8:
    return False
  #Then we check if atleast an uppercase, lowercase, digit, and no space conditions are satisfied. 
  for characters in password:
    if not any(characters.isupper() for characters in password):
      return False
    if not any(characters.islower() for characters in password):
      return False
    if not any(characters.isdigit() for characters in password):
      return False
    if any(characters.isspace() for characters in password):
      return False
  else:
    return True
