# Case Study 14: Food Delivery Orders
# Orders:
# 1001 → 1002 → 1003 → 1004
# Tasks:
# Display all orders.
# Delete Order 1002.
# Insert Order 1005.
# Display the updated orders.

# Food Delivery Orders using Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OrderList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        # If list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node and add the new node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        
        # If head node holds the key to be deleted
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key, keep track of the previous node
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # If key was not present in the list
        if temp is None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --- Execution of Tasks ---

orders = OrderList()

# Initial state
orders.insert(1001)
orders.insert(1002)
orders.insert(1003)
orders.insert(1004)

print("Task 1: Display all orders.")
orders.display()

print("\nTask 2: Delete Order 1002.")
orders.delete(1002)

print("\nTask 3: Insert Order 1005.")
orders.insert(1005)

print("\nTask 4: Display the updated orders.")
orders.display()