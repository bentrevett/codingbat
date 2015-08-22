def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed<=61:
      return 0
    if speed>60 and speed<81:
      return 1
    if speed>80:
      return 2  
  else:
    if speed<=66:
      return 0
    if speed>65 and speed<86:
      return 1
    if speed>85:
      return 2
