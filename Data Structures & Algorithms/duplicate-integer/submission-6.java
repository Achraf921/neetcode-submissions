class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> hset = new HashSet<>();
        
        for(int num:nums)
            hset.add(num);

        if(hset.size()==nums.length)
            return false;
        return true;

    }
}