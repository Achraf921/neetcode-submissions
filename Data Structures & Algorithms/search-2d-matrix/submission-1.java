class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //we just need to map the matrix into a regylar array
        int m = matrix.length;
        int n = matrix[0].length;
        /*we need to craft a new indexing system to conver the 2nd matrix
        into a 1d array, working with modulo*/
        /*
        to do the computation, we might want to have a helper method
        */
        int left = 0;
        int right = m*n-1;
        int mid;
        while(left<=right){
            mid = (right+left)/2;
            if(matrix[mid/n][(mid%n)]==target) return true;
            else if(matrix[mid/n][(mid%n)]<target) left=mid+1;
            else right = mid-1;
        }
        return false;
    }
}
