class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charS = s.toCharArray();//[r,a,c,e,c,a,r]
        char[] charT = t.toCharArray();//[c,a,r,r,a,c,e]

        Arrays.sort(charS);//[a,a,c,c,e,r,r]
        Arrays.sort(charT);//[a,a,c,c,e,r,r]

        if(s.length()!=t.length())
            return false;
        boolean test = true;
        for(int i=0;i<s.length();i++)
            if(charS[i]!=charT[i])
                test=false;
        return test;


        

    }
}
