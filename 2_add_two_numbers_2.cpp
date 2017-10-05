/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum;
		ListNode* head;
		head = sum;
        int up = 0;
		// Line 15: member access within null pointer of type 'struct ListNode'
        while (l1->val and l2->val) {
            sum->val = (l1->val + l2->val + up) % 10;
            up = (l1->val + l2->val + up) / 10;
            ListNode* follow = new ListNode(0);
			sum->next = follow;
			sum = sum->next;
        }
		while (l1->val) {
			sum->val = (l1->val + up) % 10;
			up = (l1->val + up) / 10;
            ListNode* follow = new ListNode(0);
			sum->next = follow;
			sum = sum->next;
		}
		while (l2->val) {
			sum->val = (l2->val + up) % 10;
			up = (l2->val + up) / 10;
            ListNode* follow = new ListNode(0);
			sum->next = follow;
			sum = sum->next;
		}
		if (up > 0) {
			ListNode* follow = new ListNode(up);
			sum->next = follow;
		}
		return head;
    }
};