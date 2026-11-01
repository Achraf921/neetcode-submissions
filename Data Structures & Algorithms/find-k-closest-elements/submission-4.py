class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [1, 2, 3, 4, 5, 6, 7, 8]
        # x = 5, k= 7
        # l_arr = [4, 3, 2, 1]
        # r_arr = [6, 7, 8]
        # return l_arr[::-1]+r_arr -> [1,2,3,4,6,7,8] 
        # we want to stall pointer exploration, whenever a boundary is hit
        # otherwise, we move both pointers at the same pace once at a time
        # here, worst case scenario woudl run in O(n) space and time I belive
        # a way to keep the array sorted
        # is to use two sub-arrays to store the elements (in insertion order)
        # from respectively the left and right explorere to keep the sorted structure of the arr
        # and then at the very end merge the two.
        # [1, 1, 4, 5 ,9, 19, 20, 98] # we actually mean by distance the value distance
        # rather than the index, in case of equality, we systematically go for the smallerst
        # x = 5, k = 4
        # l_arr = [4, 1, 1]
        # r_arr =[9], result l_arr[::-1] + r_arr = [1,1,4,9]

        l_arr = []
        r_arr = []
        pointer=-1
        # we first want to find x's index
        left, right, med = 0, 1, abs(x-((arr[0]+arr[1])/2))
        for i in range(1, len(arr)-1):
            new_med = abs(x-((arr[i]+arr[i+1])/2))
            if new_med<med:
                left = i
                right = i+1
                med = new_med
        count = 0
        while (left>=0 or right<len(arr)) and count<k:
            if left>=0 and right<len(arr): # if both are still in grame we compare
                dist_l = abs(x-arr[left])
                dist_r = abs(x-arr[right])
                if dist_l<dist_r:
                    l_arr.append(arr[left])
                    left-=1
                elif dist_r<dist_l:
                    r_arr.append(arr[right])
                    right+=1
                else: # equal
                    l_arr.append(arr[left])
                    left-=1
            elif left<0: # the boolan survided on right
                r_arr.append(arr[right])
                right+=1
            else: # the boolean survided on left
                l_arr.append(arr[left])
                left-=1
            count+=1
        return l_arr[::-1] + r_arr






        