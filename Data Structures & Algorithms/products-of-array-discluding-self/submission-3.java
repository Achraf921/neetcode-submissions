class Solution {
    public int[] productExceptSelf(int[] nums) {
        //brute-force/naive solution
        /*
        int[] sol = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int accumulator = 1;
            for(int k=0;k<nums.length;k++)
                if(k!=i)
                    accumulator*=nums[k];
            sol[i]=accumulator;
        }
        return sol;
        */

        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];

        //filling the prefix array
        for(int i=0;i<nums.length;i++){
            prefix[i]=1;
            if(i==0)
                prefix[i]=nums[i];
            else
                for(int k=i;k>-1;k--)
                    prefix[i]*=nums[k]; 
        }
        //filling the suffix array
        for(int i=nums.length-1;i>=0;i--){
            suffix[i]=1;
            if(i==nums.length-1)
                suffix[i]=nums[i];
            else
                for(int k=i;k<nums.length;k++)
                    suffix[i]*=nums[k]; 
        }
        int[] sol = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(i==0)
                sol[i]=1*suffix[i+1];
            else if(i==nums.length-1)
                sol[i]=prefix[i-1]*1;
            else
                sol[i]=prefix[i-1]*suffix[i+1];
        }
        //O(3n) <=> O(n)
        return sol;
        
    }
}  
