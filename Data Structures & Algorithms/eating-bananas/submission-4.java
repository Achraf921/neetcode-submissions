class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right =0;
        for(int i=0;i<piles.length;i++) right=(piles[i]>right)?piles[i]:right;
        int left=1;
        int mid;
        while(left<=right){
            mid=(right+left)/2;
            int hoursMid = h;
            int hoursBelowMid = h;
            for(int i=0;i<piles.length;i++){
                hoursMid-=(piles[i]+mid-1)/mid;
                hoursBelowMid=((mid-1)<=0)?-1:hoursBelowMid-(piles[i]+mid-2)/(mid-1);
            }
            if(hoursMid>=0&&hoursBelowMid<0) return mid;
            else if(hoursMid>=0&&hoursBelowMid>=0)right=mid-1;
            else left = mid+1;
        }
        return -1;
    }
}
