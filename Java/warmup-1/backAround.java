public String backAround(String str) 
    {
        char first = str.charAt(str.length()-1);
        return first+str+first;
    }