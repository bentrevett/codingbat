def close_far(a, b, c):
  if abs(a-b)<=1: #b is close
    if abs(a-c)>=2 and abs(b-c)>=2: #c is far
      return True
  if abs(a-c)<=1: #c is close
    if abs(a-b)>=2 and abs(b-c)>=2: #b is far
      return True
  return False
