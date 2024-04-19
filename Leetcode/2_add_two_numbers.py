# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(num: int, r: int) -> int:
    if num == 0:
        return r
    return reverse(num // 10, r * 10 + num % 10)

'''
# In this solution, I couldn't figure out a way to get the numbers saved when it "starts" with a zero.
# This has to do with the way I put the number back together. 0 * 10 would still = 0, meaning it'd 
# not get added and the sum at the end would be completely thrown off.
# It'd also use the reverse recursion function that I made for the other leetcode.
# Time complexity: O(n)(?) While it goes through the list a few times, they'd be constants.
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num_one = 0
    num_two = 0
    dummy_head = ListNode(0)
    l3 = dummy_head
    while l1 != None:
        num_one = num_one * 10 + l1.val
        l1 = l1.next
    while l2 != None:
        num_two = num_two * 10 + l2.val
        l2 = l2.next
    num_one = reverse(num_one, 0)
    num_two = reverse(num_two, 0)
    sum = num_one + num_two
    size = len(str(sum))
    for i in range(size):
        new_node = ListNode(sum % 10)
        l3.next = new_node
        l3 = l3.next
        sum //= 10
    l3 = dummy_head.next
    dummy_head.next = None
    return l3
'''
# Things that I had to look up for the solution is how a linked list in Python works.

# In my next solution, I had thought about making num_one and num_two into strings and concatenating the values into them.
# I ran into the same problem with the leading 0.
# So instead, I turned them into a list, go through them in reverse order, and add them, similar to the first solution.
# Time Complexity: Again, I believe this to be O(n) as the rest are constants. I wouldn't consider any of the solutions
# optimized, though. I can't say I like the solution as it currently stands.
'''
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Since the linked list is in reverse order, when starting with a 0, that means
    # it would actually have value. For example, if the linked list was 0 -> 1, the number
    # should actually be 10 when in correct order.
    # That means that the leading 0 is an important value and should not be ignored.
    # Thus, we add each individual number to a set of arrays and then reverse them to preserve the 0.
    num_one_list = []
    num_two_list = []
    num_one = 0
    num_two = 0
    dummy_head = ListNode(0)
    l3 = dummy_head
    while l1 != None:
        num_one_list.append(l1.val)
        l1 = l1.next
    while l2 != None:
        num_two_list.append(l2.val)
        l2 = l2.next
    for num in reversed(num_one_list):
        num_one = num_one * 10 + num
    for num in reversed(num_two_list):
        num_two = num_two * 10 + num
    sum = num_one + num_two
    # We use the len of the sum as the sum could be greater than the length of the other two
    # numbers due to carry-over.
    # Since the return value needs to be in reverse order similar to the input,
    # we take just the ones digit and place it into the linked list one by one.
    for i in range(len(str(sum))):
        new_node = ListNode(sum % 10)
        l3.next = new_node
        l3 = l3.next
        sum //= 10
    l3 = dummy_head.next
    dummy_head.next = None
    return l3
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    # Intialize a node with the number 0 and set it to l3.
    # Without doing this, there would be nothing to point to.
    # If we added a 1 to end of l3, it should be 0 -> 1
    dummy_head = ListNode(0)
    l3 = dummy_head
    # Carry is included as the last digit added can have a carry.
    # Example 99 + 1
    # But the lists could have reached the end already,
    # but we'd still want to take care of the carry.
    while l1 != None or l2 != None or carry != 0:
        # Doing this allows for one while loop. Sets the value
        # to 0 if the node is None.
        d1 = l1.val if l1 != None else 0
        d2 = l2.val if l2 != None else 0
        sum = d1 + d2 + carry
        # chops off the ones digit for the tens. Results in either a 0 or 1 depending on the tens digit.
        carry = sum // 10
        new_node = ListNode(sum % 10)
        l3.next = new_node
        l3 = l3.next

        # Move the list forward until we reach the end of the list.
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    
    # Now sets l3 to dummy_node, but skip the first item
    # since the first item is the throwaway 0 that wasn't actually needed.
    l3 = dummy_head.next
    dummy_head.next = None
    return l3