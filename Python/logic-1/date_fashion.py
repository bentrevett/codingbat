def date_fashion(you, date):
  if you>7 or date>7:
    if you<3 or date<3:
      return 0
    return 2
  elif you<3 or date<3:
    return 0
  return 1
