class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> hmap=new HashMap<>();
        for(int i=0;i<strs.length;i++){
            int[] key = new int[26];
            String str=strs[i];
            for(int k=0;k<str.length();k++){
                key[str.charAt(k)-'a']=key[str.charAt(k)-'a']+1;
            }
            String key2 = Arrays.toString(key);
            if(hmap.containsKey(key2)){
                hmap.get(key2).add(str);
            }
            else{
               List<String> temp = new ArrayList<>();
               temp.add(str);
               hmap.put(key2,temp);
            }

        }
        return new ArrayList<>(hmap.values());
    }
}
