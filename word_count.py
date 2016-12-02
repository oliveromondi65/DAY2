def words(arg): #creating the function
  counts = dict() #creating the dictionery to hold the counts
  words_in = arg.split()   #getting the words

  #getting the occurences
  for word in words_in:   
    if word in counts:  
      counts[word] += 1  
    else:  
      counts[word] = 1  
  
  return counts