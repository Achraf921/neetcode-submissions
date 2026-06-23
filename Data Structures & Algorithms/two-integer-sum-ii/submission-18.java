class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
        Use a hashmap to try to access (target - pointer) in O(1) for each
        one of the elements of the array, will run in O(n) space, O(n) time.

        Not optimal, O(n) time but O(n) space
        */
        
        /* we should rather use a two pointer approach/binary. search like approach */

        int left=0;
        int right = numbers.length-1;
        
        while(true){
            int sum = numbers[left]+numbers[right];
            if(sum==target) return new int[]{left+1,right+1};
            else if(sum<target) left++;
            else right --;
        }


    }
}
