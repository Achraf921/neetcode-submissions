class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> solution = new ArrayList<>();
        /*
        First idea, would run in O(n^2) time, O(n) space, put all numbers
        in a hashmap with (number, index) format, pick a number as base pointer,
        pick a 2nd number as iterating base pointer, query the hashmap for target
        - base - 2nd base, and then increment the 2nd base till end is reached,
        then increment based, watch out for dupes
        */

        /* it should run in O(n^2) time, O(1) space, doing a regular two pointers
        with two bases would just be brute-force and run in O(n^3) */

        /*since output should be in O(n^2), it means we can afford to quick
        sort the array */
        quicksort(nums,0,nums.length-1);
        for(int i=0;i<nums.length;i++){
            /*
            once sorted we get [-4,-1,-1,0,1,2] (ex)
            setting base pointer at i, 2nd at j, 3rd at k, we get 

            nums[j]+nums[k] = -nums[i]

            can't we now just do the regular twosum II, two-pointer approach
            since target is now set ? what would be the time complexity ?
            */
        int base = nums[i];
        if(i-1>-1&&nums[i-1]==nums[i]) continue;//gets rid of duplicates
        else{
            int target = -nums[i];
            int j = i+1;
            int right = nums.length-1;
            while(j<right){
                if(nums[j]+nums[right]==target){
                    solution.add(Arrays.asList(nums[i],nums[j],nums[right]));
                    while(right-1>0&&nums[right-1]==nums[right]) right--;
                    right--;
                }
                else if(nums[j]+nums[right]<target) j++;
                else right--;
                
            }
        }
        } 
        return solution;   
    }

    public void quicksort(int[] nums,int l,int r){// r is last element, not size
        if (r<=l) return;
        int pivot = nums[r];
        int left = l-1;
        for(int i=l;i<r;i++){
            if(nums[i]<pivot){
                left++;
                int temp = nums[left];
                nums[left]=nums[i];
                nums[i]=temp;
            }
        }
        left++;
        int temp =nums[left];
        nums[left]=pivot;
        nums[r]=temp;
        quicksort(nums,l,left-1);
        quicksort(nums,left+1,r);

    }
}
