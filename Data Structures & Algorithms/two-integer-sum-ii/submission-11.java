class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
        Use a hashmap to try to access (target - pointer) in O(1) for each
        one of the elements of the array, will run in O(n) space, O(n) time.
        */
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i=0;i<numbers.length;i++) map.put(numbers[i],i);
        for(int i=0;i<numbers.length;i++){
            if(map.get(target-numbers[i])!=null)
                return new int[] {i+1,(int)map.get(target-numbers[i])+1};
        }

        return new int[]{-1,-1};
    }
}
