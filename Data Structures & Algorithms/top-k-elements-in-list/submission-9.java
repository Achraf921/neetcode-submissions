class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i : nums){
            if(map.containsKey(i)){
                map.put(i,map.get(i)+1);
            }
            else{
                map.put(i,1);
            }
        }
        
        List<Integer> values = new ArrayList<>(map.values());
        List<Integer> keys = new ArrayList<>(map.keySet());
        System.out.println(keys);
        Collections.sort(values, Collections.reverseOrder());
        values = new ArrayList<>(values.subList(0,k));

        List<Integer> sol = new ArrayList<>(k);
        for (int i : keys){
            System.out.println(i);
            if(values.contains(map.get(i))&&!sol.contains(i))
                sol.add(i);
        }
        int[] solarr = new int[k];
        for(int i =0;i<k;i++)
            solarr[i]=sol.get(i);
        return solarr; 
    }
}
