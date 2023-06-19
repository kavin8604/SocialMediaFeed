import heapq
from datetime import datetime

class ListNode:
    def __init__(self, post):
        self.post = post
        self.next = None

class Post:
    def __init__(self, content, timestamp, image=None):
        self.content = content
        self.timestamp = timestamp
        self.image = image

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

class User:
    def __init__(self, username):
        self.username = username
        self.feed = Feed()

class Feed:
    def __init__(self):
        self.head = None
        self.priority_queue = []
    
    def add_post(self, post):
        new_node = ListNode(post)
        
        heapq.heappush(self.priority_queue, post.timestamp)
        
        new_node.next = self.head
        self.head = new_node
    
    def remove_post(self, post_content):
        current = self.head
        prev = None

        while current:
            if current.post.content == post_content:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                self.priority_queue.remove(current.post.timestamp)
                heapq.heapify(self.priority_queue)

                return True
            
            prev = current
            current = current.next

        return False
    
    def display_feed(self):
        current = self.head
        while current:
            print(f"Content: {current.post.content}")
            if current.post.image:
                print(f"Image: {current.post.image}")
            current = current.next

user_feeds = {}

def print_all_posts():
    for username, feed in user_feeds.items():
        print()
        print(f"{username}'s Feed:")
        feed.display_feed()
        print()

def main():
    while True:
        print("1. Add a user")
        print("2. Add a post for a user")
        print("3. Delete a post for a user")
        print("4. Print all posts by all users")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter the username: ")
            if username not in user_feeds:
                user = User(username)
                user_feeds[username] = user.feed
                print("User added.")
            else:
                print(f"Error: User '{username}' already exists.")

        elif choice == "2":
            username = input("Enter the username who posts: ")
            if username in user_feeds:
                content = input("Enter the content of the post: ")
                image = input("Enter the image URL (optional, press Enter to skip): ")
                timestamp = datetime.now()
                post = Post(content, timestamp, image)
                user_feeds[username].add_post(post)
                print("Post added.")
            else:
                print(f"Error: User '{username}' does not exist.")

        elif choice == "3":
            username = input("Enter the username: ")
            if username in user_feeds:
                content = input("Enter the content of the post to delete: ")
                if user_feeds[username].remove_post(content):
                    print("Post deleted.")
                else:
                    print("Post not found.")
            else:
                print(f"Error: User '{username}' does not exist.")

        elif choice == "4":
            print_all_posts()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == "__main__":
    main()
