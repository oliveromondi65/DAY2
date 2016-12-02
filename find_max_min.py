def find_max_min(arg): #creating the function
  
  minimum = min(arg) #finding the minimum value
  maximum = max(arg) #finding the maximum value

  if minimum == maximum: #testing if the minimum and maximum are equal
    number_of_elements = len(arg)
    new_list = [number_of_elements]
    return new_list
  
  else: return [minimum, maximum] #returning the minimum and maximum in an array
  