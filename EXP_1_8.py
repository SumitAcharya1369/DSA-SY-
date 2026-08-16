# 8. Call Stack in Programming
# Scenario:
# A program stores active function calls in a stack. The most recently called function completes
# execution first.
# Conditions:
# • Maximum call stack depth is 15.
# • Function names must start with a letter.
# • Recursive calls are allowed only up to 3 consecutive levels.
# • Reject invalid function names.
# Operations:
# • Call Function (Push)
# • Return from Function (Pop)
# • Current Function (Peek)
# • Display Call Stack

class CallStack:
    def __init__(self):
        self.stack = []
        self.max_depth = 15

    def push(self, func_name):
        # Reject if call stack is full
        if len(self.stack) >= self.max_depth:
            print("Stack Overflow!")
            return

        # Function names must start with a letter
        if not func_name or not func_name[0].isalpha():
            print("Invalid function name.")
            return

        # Check for recursive calls (max 3 consecutive levels)
        consecutive_count = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == func_name:
                consecutive_count += 1
            else:
                break 
                
        if consecutive_count >= 3:
            print("Recursion limit of 3 reached.")
            return

        self.stack.append(func_name)
        print(f"Called: {func_name}()")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow!")
            return
            
        completed_func = self.stack.pop()
        print(f"Returned from: {completed_func}()")

    def peek(self):
        if len(self.stack) == 0:
            print("Call stack is empty.")
        else:
            print(f"Current function: {self.stack[-1]}()")


# --- Testing ---
system_stack = CallStack()

system_stack.push("main")
system_stack.push("1invalid_func") 
system_stack.push("calculate_sum")

system_stack.push("factorial") 
system_stack.push("factorial") 
system_stack.push("factorial") 
system_stack.push("factorial") 

system_stack.peek()
system_stack.pop()