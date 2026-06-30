class Solution {
    public int search(int[] nums, int target) {
        int left=0;
        int right=nums.length-1;
        int mid;
        int smallestInd=0;
        while(left<=right){
            mid=(right+left)/2;
            if(nums[mid]<nums[smallestInd]) smallestInd=mid;
            else if(nums[mid]>nums[right]) left=mid+1;
            else right=mid-1;
        }
        left = (smallestInd==0||target>=nums[0])?0:smallestInd;
        right = (smallestInd==0||target<nums[0])?nums.length-1:smallestInd;
        while(left<=right){
            mid=(right+left)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]<=target) left=mid+1;
            else right = mid-1;
        }
        return -1;
    }
}
