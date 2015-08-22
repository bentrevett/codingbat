def near_ten(num):
  remainder=num%10
  if (remainder-2)<=0 or (remainder+2)>=10:
    return True
  else:
    return False
