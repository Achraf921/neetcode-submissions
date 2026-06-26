class MinStack {

    private ArrayDeque<Integer> mainStack;
    private ArrayDeque<Integer> minStack;


    public MinStack() {
        this.mainStack = new ArrayDeque<>();
        this.minStack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        mainStack.push(val);
        if(minStack.isEmpty())
            minStack.push(val);
        else
            minStack.push((val<minStack.peek())?val:minStack.peek());
        
    }
    
    public void pop() throws NoSuchElementException{
        mainStack.pop();
        minStack.pop();      
    }
    
    public int top() {
        return mainStack.peek();
        
    }
    
    public int getMin() {
        return minStack.peek();
        
    }
}
