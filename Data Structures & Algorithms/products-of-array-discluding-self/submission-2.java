class Solution {
    public int[] productExceptSelf(int[] nums) {
        //brute-force/naive solution
        int[] sol = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int accumulator = 1;
            for(int k=0;k<nums.length;k++)
                if(k!=i)
                    accumulator*=nums[k];
            sol[i]=accumulator;
        }
        return sol;
        
        
    }
}  
