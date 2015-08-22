def round_sum(a, b, c):
  def round10(num):
    if num%10>=5:
      num=num+(10-(num%10))
    if num%10<5:
      num=num-(num%10)
    return num
  return round10(a)+round10(b)+round10(c)
