public String stringX(String str) {
    String newstr = "";
    if(str.length()<2){
        return str;
    }
    newstr+=str.charAt(0);
    for(int i=1;i<str.length()-1;i++){
        if(str.charAt(i)!='x'){
        newstr+=str.charAt(i);
        }
    }
    newstr+=str.charAt(str.length()-1);
    return newstr;
}