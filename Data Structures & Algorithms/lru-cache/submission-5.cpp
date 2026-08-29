class LRUCache {
private: 
    struct Node{ //will use to have doubly linked list
        int key;
        Node* next;
        Node* prev; 
        Node(int k){
            key=k;
            next=nullptr;
            prev=nullptr;
        }
    };

    unordered_map<int, pair<int,Node*>> cache;//O(1) hashmap
    int capacity;
    Node* head; //we want to store the lru element at the head
    Node* tail; //we also need to keep a ref to tail

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head=nullptr;
        tail=nullptr;
    }
    
    int get(int key) {
        if(cache.size()==0||!cache.contains(key)) return -1;
        auto& cur = cache[key]; //passed by reference
        Node* afterVal = cur.second->next;
        Node* beforeVal = cur.second->prev;
        //remove the cur node from its current position
        if(beforeVal==nullptr){
            return cur.first; //if already MRU, don't change anything
            //also handles the cap=1 edge case without segfaulting later
        }
        if(afterVal==nullptr){
            head = cur.second->prev;
        }
        else{
          afterVal->prev=beforeVal;  
        }
        //finicky linked list re-arangement that is common to all scenarios
        //(tail, middle and head scenarios)
        beforeVal->next=afterVal;
        cur.second->prev=nullptr;
        tail->prev=cur.second;
        cur.second->next=tail;
        tail=cur.second;
        return cur.first;
    }
    
    void put(int key, int value) {
        //dangerous edge case where we overwrite a key-value tuple,
        //we should be able to overwrite even if the cache is full
        //and without evicting the lru but just replacing the overwritee
        //WITHOUT creating a new Node
        if(cache.contains(key)){
            //first we need to grab that key, get its Node,
            //make it the tail, change its value, then overwrite in cache
            Node* cur = cache[key].second;
            if(cur!=tail&&(tail!=head)){
                //two scenarios where we actually need to shuffle the dll
                Node* afterVal=cur->next;
                Node* prevVal=cur->prev;
                prevVal->next=afterVal;
                if(afterVal!=nullptr){
                    afterVal->prev=prevVal;
                }
                else{
                    //head scenario
                    head=prevVal;
                }
                cur->next=tail;
                cur->prev=nullptr;
                tail->prev=cur;
                tail=cur;
            }
            cache[key] = {value,cur};//finally inserting
        }
        else if(cache.size()>capacity-1){
            //pop out lru element
            cache.erase(head->key);
            //unlinking the new removed head lru-element
            if(head!=tail){
            head->prev->next=nullptr;
            }
            Node*temp = head;
            head=head->prev; //setting it to nullptr at cap = 1
            temp->prev=nullptr;
            if(temp==tail) tail=nullptr; //edge case guard for cap = 1
            delete temp;
            //link new tail (new mru)
            if(tail==nullptr){
                //if tail is null, then head is null too, thats the only 
                //scenario we end up with a null tail
                head= new Node(key);
                tail=head;
            }
            else{
                //regular case
                tail->prev= new Node(key);
                tail->prev->next=tail;
                tail = tail->prev; 
            }
            //finally putting into the cache
            cache[key]={value,tail};
        }
        //we also need to handle the case where we overwrite a key
        else{
            if(head==nullptr&&tail==nullptr){
                head = new Node(key);
                tail=head;
            }
            else{
                //regular case
                tail->prev= new Node(key);
                tail->prev->next=tail;
                tail = tail->prev; 
            }
            cache[key]={value,tail}; 
        }
    }
};
