public int max1020(int a, int b) {
    int bigger, smaller;
    if(a>=b){
        bigger = a;
        smaller=b;
    }
    else{
        bigger=b;
        smaller=a;
    }
    if(bigger>=10 && bigger<=20){
        return bigger;
    }
    else if(smaller>=10 && smaller<=20){
        return smaller;
    }
    else{
        return 0;
    }
}