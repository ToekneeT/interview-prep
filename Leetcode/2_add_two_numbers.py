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
# In my next solution, I had thought about making num_one and num_two into strings and concatenating the values into them.
# I ran into the same problem with the leading 0.
# So instead, I turned them into a list, go through them in reverse order, and add them, similar to the first solution.
# Time Complexity: Again, I believe this to be O(n) as the rest are constants. I wouldn't consider any of the solutions
# optimized, though. I can't say I like the solution as it currently stands.
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
    for i in range(len(str(sum))):
        new_node = ListNode(sum % 10)
        l3.next = new_node
        l3 = l3.next
        sum //= 10
    l3 = dummy_head.next
    dummy_head.next = None
    return l3