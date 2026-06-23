class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0)
            return 0;
        HashSet<Integer> hset = new HashSet<>();
        for(int i=0;i<nums.length;i++)
            hset.add(nums[i]);
        
        int length=1;
        int start=-1;
        for(int i=0;i<nums.length;i++){
            if(hset.contains(nums[i]-1))
                continue;
            else if(hset.contains(nums[i]+1)){
                start=nums[i]+1;
                int tempLength = 1;
                while(hset.contains(start)){
                    tempLength++;
                    start++;
                }
                if(tempLength>length)
                    length=tempLength;

            }
        }
        return length;
        
    }
}
