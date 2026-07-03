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
    ListNode dummy = new ListNode(0, head);
    ListNode first = head, second = dummy;
    for (int i = 0; i < n; i++) first = first.next;  // gap of n
    while (first != null) {                           // walk both to the end
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;                   // second is right before target
    return dummy.next;
}
}
