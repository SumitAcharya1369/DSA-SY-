# Case Study 8: Playlist Manager
# Songs are stored as:
# Song1 → Song2 → Song3
# Tasks:
# Insert Song4.
# Display the playlist.
# Delete Song2.
# Display the updated playlist.

# Playlist Manager using Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --- Execution of Tasks ---

music_playlist = Playlist()

# Initial state
music_playlist.insert("Song1")
music_playlist.insert("Song2")
music_playlist.insert("Song3")

print("Task 1: Insert Song4.")
music_playlist.insert("Song4")

print("\nTask 2: Display the playlist.")
music_playlist.display()

print("\nTask 3: Delete Song2.")
music_playlist.delete("Song2")

print("\nTask 4: Display the updated playlist.")
music_playlist.display()