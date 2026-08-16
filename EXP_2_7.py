# 7. Food Delivery Order Queue
# Scenario:
# Food orders are prepared in the order they are received.
# Conditions:
# Maximum queue capacity is 100 orders.
# Duplicate Order IDs are not allowed.
# Only confirmed orders are accepted.
# Queue overflow should be handled.
# Operations:
# Place Order (Enqueue)
# Prepare Order (Dequeue)
# View Next Order
# Display Order Queue

class FoodDeliveryQueue:
    def __init__(self):
        self.queue = []
        # Maximum queue capacity is 100 orders
        self.max_capacity = 100

    def enqueue(self, order_id, is_confirmed):
        # Queue overflow should be handled
        if len(self.queue) >= self.max_capacity:
            print("Queue is full. Cannot accept more orders.")
            return

        # Only confirmed orders are accepted
        if not is_confirmed:
            print(f"Order {order_id} is not confirmed yet.")
            return

        # Duplicate Order IDs are not allowed
        if order_id in self.queue:
            print(f"Order {order_id} is already in the queue.")
            return

        # Place Order (Enqueue)
        self.queue.append(order_id)
        print(f"Order {order_id} placed successfully.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("No orders to prepare.")
            return
            
        # Prepare Order (Dequeue)
        # pop(0) removes the first element to follow FIFO
        prepared_order = self.queue.pop(0)
        print(f"Preparing order: {prepared_order}")

    def view_next(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            # View Next Order
            print(f"Next order to prepare: {self.queue[0]}")

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            # Display Order Queue
            print("Current Order Queue:", self.queue)


# --- Testing ---
orders = FoodDeliveryQueue()

orders.enqueue("ORD001", True)
orders.enqueue("ORD002", False) 
orders.enqueue("ORD003", True)
orders.enqueue("ORD001", True) 

orders.view_next()
orders.display()
orders.dequeue()
orders.display()