class Solution {
public:
    bool isPerfectSquare(int num) {
        int count=0;
        if(num==1){
            return true;
        }
        for(long long i=1;i<num;i++){

            if((i*i)==num){
                count++;
            }
        }
        if(count==1){
            return true;
        }
        else{
            return false;
        }
    }
};