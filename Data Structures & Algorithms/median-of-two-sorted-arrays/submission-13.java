class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] min = (nums1.length <= nums2.length) ? nums1 : nums2;
        int[] max = (nums1.length <= nums2.length) ? nums2 : nums1;
        int m = min.length, n = max.length;
        int half = (m + n + 1) / 2;      // size of the combined left partition
        int lo = 0, hi = m;              // i = how many we take from min, in [0, m]
        while (lo <= hi) {
            int i = (lo + hi) / 2;
            int j = half - i;
            int left1  = (i == 0) ? Integer.MIN_VALUE : min[i - 1];
            int right1 = (i == m) ? Integer.MAX_VALUE : min[i];
            int left2  = (j == 0) ? Integer.MIN_VALUE : max[j - 1];
            int right2 = (j == n) ? Integer.MAX_VALUE : max[j];
            if (left1 <= right2 && left2 <= right1) {
                int maxLeft = Math.max(left1, left2);
                if ((m + n) % 2 == 1) return maxLeft;
                return (maxLeft + Math.min(right1, right2)) / 2.0;
            } else if (left1 > right2) hi = i - 1;
            else lo = i + 1;
        }
        return 0.0;
    }
}
