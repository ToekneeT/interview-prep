# https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    list3 = dummy_head
    # Loops until one of the values in the linked list doesn't exist.
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next
    
    # If there's a linked list that is larger than another, it'll add
    # the extra one to the end of the new linked list.
    if list1 == None:
        list3.next = list2
    elif list2 == None:
        list3.next = list1

    return dummy_head.next