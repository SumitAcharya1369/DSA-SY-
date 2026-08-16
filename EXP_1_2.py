# EXPERIMENT 1 (CASE STUDY 1)
# 2. Browser History
# Scenario:
# A web browser stores recently visited web pages in a stack. The latest page visited is the first
# one accessed when the user clicks the Back button.
# Conditions:
# • Store only URLs beginning with https://
# • Maximum browser history size is 15 pages.
# • Visiting the same page consecutively should not create a duplicate entry.
# • If history is full, reject the new page.
# Operations:
# • Visit New Page (Push)
# • Go Back (Pop)
# • Current Page (Peek)
# • Display Browser History2. Browser History

class BrowserHistory:
    def __init__(self):
        self.stack = []
        self.max_size = 15

    def push(self, url):
        # Reject if full
        if len(self.stack) >= self.max_size:
            print("History is full!")
            return

        # Store only https:// URLs
        if not url.startswith("https://"):
            print("Invalid URL. Must start with https://")
            return

        # Prevent consecutive duplicates
        if len(self.stack) > 0 and self.stack[-1] == url:
            print("Duplicate entry ignored.")
            return

        self.stack.append(url)
        print(f"Visited: {url}")

    def pop(self):
        if len(self.stack) == 0:
            print("History empty.")
            return
        
        popped_url = self.stack.pop()
        print(f"Going back from: {popped_url}")

    def peek(self):
        if len(self.stack) == 0:
            print("Browser history is empty.")
        else:
            print(f"Current Page: {self.stack[-1]}")

    def display(self):
        if len(self.stack) == 0:
            print("History is empty.")
        else:
            # Reversing the list to show newest pages first
            print("Browser History:", self.stack[::-1])


# --- Testing ---
browser = BrowserHistory()

browser.push("https://google.com")
browser.push("http://insecure-site.com") 
browser.push("https://github.com")
browser.push("https://github.com") 

browser.peek()
browser.display()
browser.pop()
