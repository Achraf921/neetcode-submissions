class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		count = {}
		max_element = float('-inf')
		for n in nums[0:k]:
			if n>max_element:
				max_element = n
			val = count.get(n)
			if val is None:
				count[n] = 1
			else:
				count[n]+=1
	
		output_array = [max_element]
		left = 0
		right = k-1
		while True: # sliding window loop
			left+=1
			right+=1
			if right>len(nums)-1: break
			removed = nums[left-1]
			added = nums[right]
			val = count.get(added)
			if val is None:
				count[added]=1
			else:
				count[added]+=1
			count[removed]-=1
			if removed == max_element and added<max_element and count[removed]==0:
			# worst case, runs O(k)
				max_element = float('-inf') # to re-compute from scratch rather than on the 
			# deceased previous max_ele
				for n in nums[left:right+1]:
					if n>max_element:
						max_element = n
			else: #scenario where either we have not removed the max element,
				# a new max_element took over, or we had other instances of max
				# element in the window
				if added>max_element:
					max_element = added

			output_array.append(max_element) # indent whatever max_element survived

		return output_array