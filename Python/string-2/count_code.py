def end_other(a, b): #return true if a ends in b
    if(len(a)>len(b)):
        longer=a
        shorter=b
    else:
        longer=b
        shorter=a
    print(longer[len(longer)-len(shorter):])
    if longer[len(longer)-len(shorter):]==shorter:
        return True
    return False
  


end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc') 
end_other('abc', 'abXabc') 
