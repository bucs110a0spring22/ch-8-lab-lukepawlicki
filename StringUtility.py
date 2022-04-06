class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    for i in self.string:
      if i == 'a'or i =='e'or i =='i'or i =='o'or i =='u':
        count += 1
      if count >= 5: 
        return 'many'
    return str(count)
        

  def bothEnds(self):
    return (self.string[0,1,-2,-1] if len(self.string[0,1,-2,-1])>2 else '')
  
  # def fixStart(self):
  #   l 
  
  # def asciiSum(self):
  #   l 
  
  # def cipher(self):