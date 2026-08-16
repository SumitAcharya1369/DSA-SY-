# 6. Supermarket Billing Queue
# Scenario:
# Customers wait in a queue to pay their bills at the checkout counter.
# Conditions:
# Queue capacity is 40 customers.
# Duplicate Customer IDs are not allowed.
# Only customers with shopping carts can join.
# No new customer can enter when the queue is full.
# Operations:
# Add Customer (Enqueue)
# Bill Customer (Dequeue)
# View Next Customer
# Display Billing Queue

class SupermarketQueue:
    def __init__(self):
        self.queue = []
        # Queue capacity is 40 customers
        self.capacity = 40

    def join_queue(self, customer_id, has_cart):
        # No new customer can enter when the queue is full
        if len(self.queue) >= self.capacity:
            print("Queue is full!")
            return

        # Only customers with shopping carts can join
        if not has_cart:
            print(f"Customer {customer_id} needs a shopping cart to join.")
            return

        # Duplicate Customer IDs are not allowed
        if customer_id in self.queue:
            print(f"Customer {customer_id} is already in line.")
            return

        self.queue.append(customer_id)
        print(f"Customer {customer_id} joined the queue.")

    def checkout(self):
        if len(self.queue) == 0:
            print("No customers in queue.")
            return
            
        served_customer = self.queue.pop(0)
        print(f"Customer {served_customer} has paid the bill.")

    def display_queue(self):
        if len(self.queue) == 0:
            print("The billing queue is empty.")
        else:
            print("Current Billing Queue:", self.queue)


# --- Testing ---
checkout_line = SupermarketQueue()

checkout_line.join_queue("CUST_101", True)
checkout_line.join_queue("CUST_102", False) 
checkout_line.join_queue("CUST_103", True)
checkout_line.join_queue("CUST_101", True) 

checkout_line.display_queue()
checkout_line.checkout()
checkout_line.display_queue()