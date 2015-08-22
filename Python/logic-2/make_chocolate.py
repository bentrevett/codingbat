def make_chocolate(small, big, goal): #6,2,7
    if(goal>big*5+small) or (goal%5>small):
        return -1
    small_needed=goal-big*5
    if(small_needed>0):
        return small_needed
    else:
        return small_needed%5
