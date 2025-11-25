stack=[]

# push an item in stack
stack.append(2)
stack.append(3)
stack.append(8)

# stack.top() or stack.peek()
top=stack[-1]

# pop() the topmost element
popped_element=stack.pop()

# check if stack is empty
if not stack:
    print("Empty")
    
# size
size=len(stack)

# pop until stack is empty
while stack:
    stack.pop()
    
print(stack)