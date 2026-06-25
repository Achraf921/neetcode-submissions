class Solution {
    public boolean isValid(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for(int i = 0;i<s.length();i++){
            if(stack.peek()==null) stack.push(s.charAt(i));
            else if(s.charAt(i)==')'){
                if(stack.peek().equals(new Character('('))) stack.pop();
                else stack.push(')');
            }
            else if(s.charAt(i)==']'){
                if(stack.peek().equals(new Character('['))) stack.pop();
                else stack.push(']');
            }
            else if(s.charAt(i)=='}'){
                if(stack.peek().equals(new Character('{'))) stack.pop();
                else stack.push('}');
            }
            else stack.push(s.charAt(i));
        }
        return stack.peek()==null;
    }
}
