class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        /*
        Monotonic decreasing stack, whenever a value is bigger than the previous ones,
        we remove the smaller ones before for it to remain monotonic, and we increment 
        the counter at the index of the removed values as well as the existing values
        */

        ArrayDeque<int[]> stack = new ArrayDeque<>();
        int[] solution = new int[temperatures.length];
        for(int i=0;i<temperatures.length;i++){
            if(stack.isEmpty()||temperatures[i]<=stack.peek()[1]) stack.push(new int[]{i,temperatures[i]});
            //simply pushing to the stack if <= or empty to remain monotonic (meaning a lower temp hasn't been reached)
            else{
                int curTemp = temperatures[i];
                while(!stack.isEmpty()&&curTemp>stack.peek()[1]){
                    solution[stack.peek()[0]]+=i-stack.peek()[0];//adding the accurate number of days delta
                    stack.pop();
                }
                /*once all non-inferior temps have been removed and updated acordingly to sol we add
                the now inferior new value to the stack.*/
                stack.push(new int[]{i,curTemp});
            }
        }
        return solution;
    }

    //stack[40,28]
    //sol[1,4,1,2,1,0,0]

    //after manually running it, it does seem to work, let's try to submit
}
