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
    public void reorderList(ListNode head) {
        //let's first figure out the length
        int len=0;
        ListNode p=head;
        while(p!=null){
            p=p.next;
            len++;
        }
        if(len<=2) return;
        ListNode left = head;
        p=head;
        int counter=0;
        while(counter<len/2){
            p=p.next;
            counter++;
        }
        ListNode right = p.next;
        p.next=null;
        right = reverseLinkedList(right);
        ListNode store;
        while(left!=null&&right!=null){
            store=left.next;
            left.next=right;
            left=store;
            store=right;
            right=right.next;
            store.next=left;
        }
    }

    public static ListNode reverseLinkedList(ListNode head){
        if(head==null||head.next==null) return head;
        ListNode back = null;
        ListNode cur = head;
        ListNode forward = head.next;

        while(cur!=null){
            cur.next=back;
            back=cur;
            cur=forward;
            if(forward!=null) forward=forward.next;
        }
        return back;
    }
}
