def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n>=13 and n<=19:
      if n==15 or n==16:
        return n
      else:
        return 0
    else:
      return n
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
