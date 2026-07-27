# =========================
# ENTITY CLASSES
# =========================

class User:
    def __init__(self, user_id):
        self.user_id = user_id


class Message:
    def __init__(self, message_id, sender_id, message_type, mention_user=None):
        self.message_id = message_id
        self.sender_id = sender_id
        self.message_type = message_type  # Text / Mention
        self.mention_user = mention_user


class ChatUserStatus:
    def __init__(self, user):
        self.user = user
        self.unread_count = 0
        self.mention_count = 0


class Chat:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []              # list of User
        self.messages = []           # list of Message
        self.user_status_list = []   # list of ChatUserStatus

    # Add user to chat
    def add_user(self, user):
        self.users.append(user)
        self.user_status_list.append(ChatUserStatus(user))


# =========================
# SERVICE CLASS
# =========================

class ChatService:

    def __init__(self):
        self.users = []
        self.chats = []

    def add_user(self, user_id):
        self.users.append(User(user_id))

    def add_chat(self, chat_id):
        self.chats.append(Chat(chat_id))

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_chat(self, chat_id):
        for chat in self.chats:
            if chat.chat_id == chat_id:
                return chat
        return None

    # =========================
    # 1️⃣ SEND MESSAGE
    # =========================
    def send_message(self, user_id, chat_id, message_id, message_type, mention_user=None):

        chat = self.get_chat(chat_id)
        sender = self.get_user(user_id)

        if not chat or not sender:
            print("Invalid user or chat")
            return

        message = Message(message_id, user_id, message_type, mention_user)
        chat.messages.append(message)

        for status in chat.user_status_list:
            if status.user.user_id != user_id:
                status.unread_count += 1

            # Handle mention
            if message_type == "Mention" and status.user.user_id == mention_user:
                status.mention_count += 1

        print("Message Sent")

    # =========================
    # 2️⃣ OPEN CHAT
    # =========================
    def open_chat(self, user_id, chat_id):
        chat = self.get_chat(chat_id)

        if not chat:
            print("Chat not found")
            return

        for status in chat.user_status_list:
            if status.user.user_id == user_id:
                status.unread_count = 0
                print("Chat Opened")
                return

    # =========================
    # 3️⃣ DISPLAY CHAT ACTIVITY
    # =========================
    def display_status(self, user_id, chat_id):
        chat = self.get_chat(chat_id)

        if not chat:
            print("Chat not found")
            return

        for status in chat.user_status_list:
            if status.user.user_id == user_id:

                priority = False
                if status.unread_count > 5 or status.mention_count > 0:
                    priority = True

                print("Unread Messages :", status.unread_count)
                print("Mention Count :", status.mention_count)
                print("Priority Chat :", "Yes" if priority else "No")
                return


# =========================
# MAIN DRIVER (Console)
# =========================

service = ChatService()

n_users = int(input("Enter number of users: "))
for i in range(n_users):
    uid = input("Enter User ID: ")
    service.add_user(uid)

n_chats = int(input("Enter number of chats: "))
for i in range(n_chats):
    cid = input("Enter Chat ID: ")
    service.add_chat(cid)

# Add users to chats manually (for simplicity)
for chat in service.chats:
    count = int(input(f"How many users in {chat.chat_id}? "))
    for _ in range(count):
        uid = input("Enter User ID to add: ")
        user = service.get_user(uid)
        if user:
            chat.add_user(user)

# Sample operations loop
while True:
    print("\n1. Send Message")
    print("2. Open Chat")
    print("3. Display Chat Status")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        uid = input("Sender ID: ")
        cid = input("Chat ID: ")
        mid = input("Message ID: ")
        mtype = input("Message Type (Text/Mention): ")

        mention_user = None
        if mtype == "Mention":
            mention_user = input("Mention User ID: ")

        service.send_message(uid, cid, mid, mtype, mention_user)

    elif choice == 2:
        uid = input("User ID: ")
        cid = input("Chat ID: ")
        service.open_chat(uid, cid)

    elif choice == 3:
        uid = input("User ID: ")
        cid = input("Chat ID: ")
        service.display_status(uid, cid)

    elif choice == 4:
        break
