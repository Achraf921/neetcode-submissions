class Solution {
    public boolean isPalindrome(String s) {
                    String workingString= s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        // ex : moom
        if(workingString.length()%2==0){
            String first = workingString.substring(0,(workingString.length()/2));
            String last = new StringBuilder(workingString.substring((workingString.length()/2),workingString.length())).reverse().toString();
            if(first.equals(last))
                return true;
            else 
                return false;
        }
        else{ //ex : yeney
            String first = workingString.substring(0,((workingString.length()/2)));
            String last = new StringBuilder(workingString.substring(((workingString.length()/2)+1),workingString.length())).reverse().toString();
            if(first.equals(last))
                return true;
            else 
                return false;

        }
        
    }
}
