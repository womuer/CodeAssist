void findDuplicates(int arr[], int n) {
    int i, j;
    printf(
);
    
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                printf(
, arr[i]);
            }
        }
    }
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *removeNthFromEnd(struct ListNode *head, int n) {
    struct ListNode entry, *p_free, *p = head;
    int i, sz = 0;
    entry.next = head;
    while (p != NULL) {
        p = p->next;
        sz++;
    }
    for (i = 0, p = &entry; i < sz - n; i++, p = p -> next)
    ;
    p_free = p->next;
    if (n != 1) {
        p->next = p->next->next;
    } else {
        p->next = NULL;
    }
    free(p_free);
    return entry.next;
}