class TimeMap {
    HashMap<String, ArrayList<String[]>> hmap;

    /*since timestamps are strictly increasing, we are good
    to use index as timestamp and then could either get in O(1) or
    search for the nearest if the get timestamp doesn't exist*/

    /*since timestamps are strictly increasing but not explicitley
    a Un+1 = Un + 1 series, we might want to store the timestamp 
    value rather than using index to not end up with 
    empty/null memory slots and un-necessarly consume memory addresses
    , we do so in the following format : 
     { {timeStamp1, Value1} , {timeStamp2, Value2}, ...} in increasing order
     and we can hence apply bin search if looking for a specific time stamp to
     allow O(log(n)) lookup*/

    public TimeMap() {
        this.hmap = new HashMap<String, ArrayList<String[]>>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!hmap.containsKey(key)){
            hmap.put(key, new ArrayList<String[]>());
        }
        hmap.get(key).add(new String[]{Integer.toString(timestamp), value});
    }
    
    public String get(String key, int timestamp) {
        if(!hmap.containsKey(key)||Integer.parseInt(hmap.get(key).get(0)[0])>timestamp) return "";
        else if(Integer.parseInt(hmap.get(key).get(hmap.get(key).size()-1)[0])<timestamp) return hmap.get(key).get(hmap.get(key).size()-1)[1];
        else{
            int left = 0;
            int right = hmap.get(key).size()-1;
            int mid;
            int closest=0; // {distance, index}
            while(left<=right){
                mid=(right+left)/2;
                if(Integer.parseInt(hmap.get(key).get(mid)[0])==(timestamp)) return hmap.get(key).get(mid)[1];
                else if(Integer.parseInt(hmap.get(key).get(mid)[0])<timestamp){
                    left=mid+1;
                    closest=(Math.abs(closest-timestamp)>Math.abs(closest-Integer.parseInt(hmap.get(key).get(mid)[0])))?mid:closest;
                }
                else right = mid-1;          
            }
            return hmap.get(key).get(closest)[1];
        }
    }      
    }
