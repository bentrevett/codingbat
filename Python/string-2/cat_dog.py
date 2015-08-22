def cat_dog(str):
    cats=0
    dogs=0
    for x in range(len(str)-2):
        if str[x:x+3]=='cat':
            cats+=1
        if str[x:x+3]=='dog':
            dogs+=1
    return cats==dogs
