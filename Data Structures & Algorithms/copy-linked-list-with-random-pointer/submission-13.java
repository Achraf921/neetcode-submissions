/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {

    public Node copyRandomList(Node head){
        return copyRandomListHelper(head,null);
    }
    public Node copyRandomListHelper(Node head, HashMap<Node,Node> cache) {
        if(head==null) return null;
        HashMap<Node,Node> newCache;
        if(cache==null) newCache = new HashMap<Node,Node>();
        else newCache=cache;
        Node cur = new Node(head.val);
        newCache.put(head,cur);
        cur.next=copyRandomListHelper(head.next,newCache);
        cur.random=newCache.get(head.random);
        return cur;
    }
}
