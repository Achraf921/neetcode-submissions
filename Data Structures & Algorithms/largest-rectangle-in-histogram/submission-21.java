class Solution {
    public int largestRectangleArea(int[] heights) {
        int[][] couples = new int[heights.length][];
        for(int i=0;i<couples.length;i++) couples[i] = new int[]{heights[i],i};
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        int maxArea = 0;
        //implementing monotonic stack filling and logic
        //we need to watch out for left index computation
        for(int i=0;i<couples.length;i++){
            if(stack.isEmpty()||stack.peek()[0]<=couples[i][0]) stack.push(couples[i]);
            else{

                int rightMost = i-1;
                while(!stack.isEmpty()&&stack.peek()[0]>couples[i][0]){
                    int[] current = stack.pop();
                    int leftMost=(stack.isEmpty())?0:stack.peek()[1]+1;
                    int width=rightMost-leftMost+1;
                    maxArea=(current[0]*width>maxArea)?current[0]*width:maxArea;
                }
                stack.push(couples[i]);
            }
        }

        //emptying the stack (i.e the remaining monotonicaly ordered part of the histogram)
        int rightMost = stack.peek()[1];
        while(!stack.isEmpty()){
            int[] current = stack.pop();
            int leftMost=(stack.isEmpty())?0:stack.peek()[1]+1;
            int width=rightMost-leftMost+1;
            maxArea=(current[0]*width>maxArea)?current[0]*width:maxArea;
        }
        return maxArea; 
    }
}
