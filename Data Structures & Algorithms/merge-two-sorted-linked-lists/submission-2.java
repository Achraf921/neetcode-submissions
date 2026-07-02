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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null&&list2==null) return null;
        if(list1==null||list2==null) return (list1==null)?list2:list1;

        ListNode head = (list1.val<=list2.val)?list1:list2;
        ListNode headNode = head;
        ListNode node1 = (list1.val<=list2.val)?list2:list1;
        ListNode node2 = (list1.val<=list2.val)?list1.next:list2.next;

        while(node1!=null&&node2!=null){
            if(node1.val<=node2.val){
                headNode.next=node1;
                headNode=headNode.next;
                node1=node1.next;
            }
            else{
                headNode.next=node2;
                headNode=headNode.next;
                node2=node2.next;
            }
        }
        if(node1!=null) headNode.next=node1;
        if(node2!=null) headNode.next=node2;
        return head;
    }
}