/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        /* a trivial solution is to reverse the link list, remove the 
        start and re-reverse it again, runs in O(n) time, O(1) space, is there
        sumn smarter ?*/
        if(head==null) return null;
        if(head.next==null){
            if(n<=0) return head;
            else return null;
        }
        ListNode newHead = reverseLinkedList(head);
        int counter =0;
        ListNode pointer = newHead;
        ListNode pointerPrev=null;
        while(counter<n-1){
            pointerPrev=pointer;
            pointer=pointer.next;
            counter++;
        }
        if(pointerPrev!=null) pointerPrev.next=pointer.next;
        else newHead= pointer.next;
        pointer.next=null;
        return reverseLinkedList(newHead);
        
    }
    public static ListNode reverseLinkedList(ListNode head){
        if(head==null||head.next==null) return head;
        ListNode prev=null;
        ListNode cur = head;
        ListNode forward = head.next;
        while(cur!=null){
            cur.next=prev;
            prev=cur;
            cur=forward;
            if(forward!=null) forward=forward.next;
        }
        return prev;
    }
}
