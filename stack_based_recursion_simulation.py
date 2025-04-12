class Stack:
    # Construct new stack:
    def __init__ (self):
        """
        Create a stack with a fixed size of 10
        """
        self.array = [None]*10
        self.size = 0  # Number of elements currently in the stack
    
    # Neccessary functions for Stack:
    def push(self, item):
        """
        Push an item onto the stack (end of array). If the stack is full, double the size of the stack
        """
        if self.size == len(self.array):
            self.array = self.array + [None]*len(self.array)
        self.array[self.size] = item # Add the item to the end of the array
        self.size += 1 #Update the size of the stack
        
    def pop(self):
        """
        Pop the last item from the stack array. If the stack is empty, return None
        """
        if self.size == 0:
            return None
        value = self.array[self.size-1]
        self.array[self.size-1] = None # Set the last elem to None
        self.size -= 1 #Decrease the size of the stack
        return value
    
    def isEmpty(self):
        """
        Return True if the stack is empty, False otherwise
        """
        return self.size == 0    
    
  # Useful functions for a stack:

    def peak(self):
        """
        Return the item at the top of the stack
        """
        if self.size == 0:
            return None
        return self.array[self.size-1]

    def isFull(self):
        """
        Return True if the stack is full, False otherwise
        """
        return self.size == len(self.array)
    
    def __str__(self):
        """
        Return a string representation of the stack.
        """
        return str([self.array[i] for i in range(self.size)])
    
def F_1(n, F_results = None):
    """
    Recursive F(n) from the assignment page, function 1
    """
    if F_results is None: # if the list is not provided, create a new list to store the results of the recursive function
        F_results = []
    # function body as listed in document
    if n > 1:
        if n%2 == 0:
            F_1(n//2, F_results)  # Recursive call, passing the same F_results
        else:
            F_1(3*n+1, F_results)  # Recursive call, passing the same F_results
    F_results.append(n)
    return F_results

def F_2(n, F_results=None):
    """
    Recursive F(n) from the assignment page, function 2
    """
    if F_results is None:
        F_results = []  # Initialize the list only once at the start
    
    if n >= 6:
        F_2(n // 3, F_results)  # Recursive call
        F_2(2 * n // 3, F_results)  # Recursive call
    F_results.append(n)  # Append the value of n to the list
    return F_results  # Return the list of values

def F_3(a, b, F_results=None):
    """
    Recursive F(a,b) from the assignment page, function 3
    """
    if F_results is None:
        F_results = []  # Initialize the list only once at the start
    
    if a <= b:
        m = (a+b)//2
        F_3(a, m-1, F_results)  # Recursive call
        F_results.append(m)
        F_3(m+1, b, F_results)  # Recursive call
    
    return F_results  # Return the list of values

def F_4(a, b, F_results=None):
    """
    Recursive F(a,b) from the assignment page, function 4
    """
    if F_results is None:
        F_results = []
    if a <= b:
        m=(a+b)//2
        F_4(a, m-1, F_results)
        F_4(m+1, b, F_results)
        F_results.append(m)
    return F_results

def function_1(n):
    """
    Performs a non-recursive Collatz sequence on an integer n
    """
    S = Stack()
    S.push(n)
    result = []  # List to store output
    current = n
    #print(current)
    while current > 1:
        if current % 2 == 0:
            current = current//2   
        else:
            current = 3*current + 1
        S.push(current)
    # Pop all elements from stack to reverse the order
    while not S.isEmpty():
        result.append(S.pop())

    return result

def function_2(n):
    S = Stack()
    S.push((n, False)) #(value, completed flag)
    result = []

    while not S.isEmpty():
        current, completed = S.pop()

        if completed:  # If this node's children have been processed, we can now append it
            result.append(current)
        else:
            if current < 6:  # Base case: just append immediately
                result.append(current)
            else:
                S.push((current, True))  # Push current again, but marked as completed
                S.push((2 * current // 3, False))  # Push right child
                S.push((current // 3, False))  # Push left child

    return result 


def function_3(a, b):
    #Think of the problem as a binary tree. Every node may have a left and right child node bacsed on the parent node a, b and m values.
    S = Stack()  
    S.push((a, b, False))  # Push the initial range and the flag to indicate we have not "completed" the node connections to children.
    result = []     # Initialize list to store the value of m from the node traversal in-order

    while not S.isEmpty():     
        a, b, completed = S.pop() #load up the last node from the stac (moving down left nodes and progressing right) 
        
        m = (a+b)//2 #calculate the mid point ("m") value

        if completed: #grab the value of m from the last node we popped off the stack if we have already completed a search for any children
            # Append the popped node's mid point value
            result.append(m)
            continue  # next iteration!

        if a <= b:
            if m+1 <= b: #if right node condition is satisfied:
                S.push((m+1, b, False)) # Push the right side
            #Push the parent node because we popped it off the stack earlier in the loop to organize the list. 
            # Now that we are checking its children, we can say we completed the search of this node.
            S.push((a,b, True)) #set flag to true
            if a <= m-1: #if left node condition is satisfied:
                S.push((a, m-1, False)) # Push the left side
    return result

def function_4(a, b):
    #Think of the problem as a binary tree. Every node may have a left and right child node bacsed on the parent node a, b and m values.
    S = Stack()  
    S.push((a, b, False))  # Push the initial range and the flag to indicate we have not "completed" the node connections to children.
    result = []     # Initialize list to store the value of m from the node traversal in-order

    while not S.isEmpty():     
        a, b, completed = S.pop() #load up the last node from the stac (moving down left nodes and progressing right) 
        
        m = (a+b)//2 #calculate the mid point ("m") value

        if completed: #grab the value of m from the last node we popped off the stack if we have already completed a search for any children
            # Append the popped node's mid point value
            result.append(m)
            continue  # next iteration!
    
        else:
            #Push the parent node because we popped it off the stack earlier 
            S.push((a,b, True)) #set flag to true

            if m+1 <= b: #if right node condition is satisfied:
                S.push((m+1, b, False)) # Push the right side
            # Now that we are checking its children, we can say we completed the search of this node.
            if a <= m-1: #if left node condition is satisfied:
                S.push((a, m-1, False)) # Push the left side

        
    return result


if __name__ == "__main__":
    # Create a new text file (or overwrite if it already exists)
    with open("stack_output.txt", "w") as file:
        file.write("The Magical Mystery Stack spits out thusly:\n")  # Write content to the file

        file.write("Function 1\n")
        for i in {7, 18, 19, 22, 105}: # Testing function_1
            stack = F_1(i) # We ned a list to write output of recursive function F
            #Output Recursive F_1
            file.write("Recursive output for n = "+ str(i) +": "+ str(stack) + "\n")        
            #Output Iterativbe function_1
            file.write("Iterative output for n = "+ str(i) +": "+ str(function_1(i)) + "\n\n")

        file.write("Function 2\n")
        for i in {7, 18, 19, 22, 43}: # Testing function_2 
            stack = F_2(i)  # Again, we ned a list to write output of recursive function F
            #Output Recursive F_2
            file.write("Recursive output for n = "+ str(i) +": "+ str(stack) + "\n")        
            #Output Iterativbe function_2
            file.write("Iterative output for n = "+ str(i) +": "+ str(function_2(i))+"\n\n")

        file.write("Function 3\n")     
        for a, b in {(0,7), (1,18), (4, 19), (-1, 22)}: # Testing function_3 
            stack = F_3(a, b)  
            file.write("Recursive output for (a,b) = "+ str((a, b)) +": "+ str(stack) + "\n")        
            #Output Iterativbe function_3
            file.write("Iterative output for (a,b) = "+ str((a, b)) +": "+ str(function_3(a,b)) + "\n\n")

        file.write("Function 4\n")     
        for a, b in {(0,7), (1,18), (4, 19), (-1, 22)}: # Testing function_4 
            stack = F_4(a, b)  
            file.write("Recursive output for (a,b) = "+ str((a, b)) +": "+ str(stack) + "\n")        
            #Output Iterativbe function_4
            file.write("Iterative output for (a,b) = "+ str((a, b)) +": "+ str(function_4(a,b)) + "\n\n")
