public int close10(int a, int b) {
  int abs_a = Math.abs(10-a);
  int abs_b = Math.abs(10-b);
  if(abs_a>abs_b){
    return b;
  }
  else if(abs_b>abs_a){
    return a;
  }
  else{
    return 0;   
  }
}