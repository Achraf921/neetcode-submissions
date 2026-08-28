/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* accumulator = head;
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        while(p1!=nullptr||p2!=nullptr){
            bool wasNextCreated = false;
            if(p1!=nullptr){
                if(accumulator->val+p1->val>9){
                    accumulator->next = new ListNode(1);
                    wasNextCreated=true;
                    accumulator->val+=(p1->val)-10;
                }
                else{
                accumulator->val+=(p1->val);
                }
                //moving down the llist here to avoid calling on nullptr
                p1=p1->next;
            }

            if(p2!=nullptr){
                if(accumulator->val+p2->val>9){
                    //can never get created twice so ok to let here ungated
                    accumulator->next = new ListNode(1);
                    wasNextCreated=true;
                    accumulator->val+=(p2->val)-10;
                }
                else{
                    accumulator->val+=(p2->val);
                }
                //moving down the llist here to avoid calling on nullptr
                p2=p2->next;
            }

            if(!wasNextCreated && (p1!=nullptr||
                p2!=nullptr)) accumulator->next = new ListNode(0);

            //move down the linked list
            if(p1!=nullptr||
                p2!=nullptr){accumulator=accumulator->next;
            }
        }
        return head;
    }
};
