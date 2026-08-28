class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        //here, all sort and multiset based solutions imply either using 
        //more than O(1) space or editing the nums array which is not 
        //allowed, hence we'll implement floyd's hare and tortoise 
        //which runs in
        //O(1) space O(n) time
        //here seeing this array as a linked list where the value is the 
        //pointer to which its pointing, the duplicate will hence 
        //have two pointers pointing at it which creates a cycle


        //starting at 0+step size since 0 is certain to not be the start
        // of the cycle

        int slow = nums[0]; //single step
        int fast = nums[nums[0]]; //double step
        while(slow!=fast){
            slow=nums[slow];
            fast=nums[nums[fast]];
            //we keep cycling until we are not pointing to the same val
        }
        int newslow = 0 ;
        while(nums[newslow]!=nums[slow]){
            newslow=nums[newslow];
            slow=nums[slow]; //advancing both at single step speed
        }
        return nums[newslow];

    }
};
