public String altPairs(String str) {
    String newstr="";
    int end;
    for(int i=0;i<str.length();i+=4){
        end=i+2;
        if(i+2>str.length()){
            end=str.length();
        }
        newstr+=str.substring(i,end);
    }
    return newstr;
}