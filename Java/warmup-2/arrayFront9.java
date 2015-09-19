public boolean arrayFront9(int[] nums) {
    int length=4;
    if(nums.length<4){
        length=nums.length;
    }
    for(int i=0;i<length;i++){
        if(nums[i]==9){
            return true;
        }
    }
    return false;
}