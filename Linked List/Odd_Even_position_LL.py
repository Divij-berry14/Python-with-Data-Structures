class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def rearrange_Even_Odd(self,head):
    if head==None:
        return None
    odd=head
    even=head.next
    firstEven=even

    while(1==1):
        if odd==None or even==None or even.next==None:
            odd.next=firstEven
            break

        odd.next=even.next
        odd=even.next

        if odd.next==None:
            even.next=None
            odd.next=firstEven
            break
        even.next=odd.next
        even=odd.next