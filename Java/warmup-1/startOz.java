public String startOz(String str) {
  String oz="";
  if(str.length()>0&&str.charAt(0)=='o')
    oz+="o";
  if(str.length()>1&&str.charAt(1)=='z')
    oz+="z";
  return oz;
}