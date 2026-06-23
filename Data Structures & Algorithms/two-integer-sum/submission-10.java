class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hmap = new HashMap<>();
        int t=target;

        for(int i=0;i<nums.length;i++)
                hmap.put(nums[i],i);
        for(int i=0;i<nums.length;i++){
            int nx = t-nums[i];
            if(hmap.get(nx)!=null&&hmap.get(nx)!=i){
                int[] sol = {i,hmap.get(nx)};
                Arrays.sort(sol);
                return sol;
            }

        }
        return new int[2];  
    }
}
