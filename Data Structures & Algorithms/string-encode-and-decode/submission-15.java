class Solution {

    public String encode(List<String> strs) {
        String sol="";
        for(String str : strs){
            String delimitor = str.length()+"#";
            sol+=delimitor+str;
        }
         return sol;   

    }

    public List<String> decode(String str) {
        System.out.println(str);
        List<String> sol = new ArrayList<>();
        int pointerRight = 0;
        int pointerLeft = 0;
        int length=0;
        while (pointerRight<str.length()){
            if(str.charAt(pointerRight) != '#')
                pointerRight++;
            else{
                length = Integer.parseInt(str.substring(pointerLeft,pointerRight));
                System.out.println(pointerRight);
                sol.add(str.substring(pointerRight+1,pointerRight+1+length));
                pointerLeft=pointerRight+length+1;
                pointerRight=pointerLeft;
            }
        }
        return sol;

    }
}
