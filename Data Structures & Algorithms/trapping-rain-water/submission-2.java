class Solution {
    public int trap(int[] height) {
        int maxL = 0;
        int maxR = 0;
        int sum = 0;
        int left = 0;
        int right = height.length-1;
        while(left<right){
            /*naturally skips 1st and last blocks as they can hold 0 since 
            they are on the border*/
            if(height[left]<=height[right]){
                if(height[left]>maxL) maxL=height[left];
                left++;
                int water = maxL-height[left];
                if(water>0) sum+=water;
            }
            else{
                if(height[right]>maxR) maxR=height[right];
                right--;
                int water = maxR-height[right];
                if(water>0) sum+=water;
            }
        }
        return sum;
        }
        
    }
