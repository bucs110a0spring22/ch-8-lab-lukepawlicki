class StringUtility:
  def __init__(self, string):
    '''
    Sets the string parameter for the class
    Args: self- str, object created by the class
          string- str, word plugged into the class
    Return: None
    '''
    self.string = string

  def __str__(self):
    '''
    Returns the string
    Args: self- str, instance of the class object
    Return: self.string- str, returns the object
    '''
    return self.string

  def vowels(self):
    '''
    Counts the number of vowels in the string
    Args: self- str, the word being plugged in
    Return: count- str, number of vowels in the word
    '''
    count = 0
    for i in self.string:
      if i == 'a'or i =='e'or i =='i'or i =='o'or i =='u':
        count += 1
      if count >= 5: 
        return 'many'
    return str(count)
        

  def bothEnds(self):
    '''
    Returns the first and last two characters in the string
    Args: self- str, word being plugged in
    Return: modified version of the string, or an empty string
    '''
    return (self.string[0]+self.string[1]+self.string[-2]+self.string[-1] if len(self.string) >2 else '')
  
  def fixStart(self):
    '''
    Changes all instances of the first letter to a '*,' except for the first letter itself
    Args: self- word being plugged in
    Return: newNewString- str, new string with the above changes
    '''
    if len(self.string) <= 1:
      return self.string
    else:
      newString = self.string.replace(self.string[0],'*')
      newNewString = self.string[0] + newString[1:]
    return newNewString
          
  def asciiSum(self):
    '''
    Adds the ord values for all letters in the string
    Args: self- word being plugged in
    Return: sum- int, sum of the ords of the letters in the string
    '''
    sum = 0
    for i in range(len(self.string)):
      sum += ord(self.string[i])
    return sum
    
  def cipher(self):
    '''
    Changes all letters by the length of the string, down the alphabet
    Args: self- word being plugged in
    Return: cipher- str, new string with incremented letters
    '''
    cipher = ""
    for i in self.string:
      if i.isalpha():
        if i.isupper():
            ordVal = ord(i) + len(self.string)
            if ordVal > ord('Z'):
              ordVal = ordVal - 26
            letter = chr(ordVal)
        if i.islower():
            ordVal = ord(i) + len(self.string)
            if ordVal > ord('z'):
              ordVal = ordVal - 26
              if ordVal > ord('z'):
                ordVal = ordVal - 26
            letter = chr(ordVal)
      else:
        letter = i
      cipher += letter
    return cipher
  