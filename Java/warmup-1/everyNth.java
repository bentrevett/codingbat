public String everyNth(String str, int n) {
  String new_string="";
  for(int i=0;i<str.length();i+=n){
    new_string+=str.charAt(i);
    }
    return new_string;
}