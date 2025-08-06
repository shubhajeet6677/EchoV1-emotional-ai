class MemoryManager:
    def __init__(self):
        self.history = []

    def add_memory(self, user ,echo):
        self.history.append({"user" : user , "echo" : echo})

    def get_context_text(self):
        return "\n".join(
            [f"User: {msg['user']}\nEcho: {msg['echo']}" for msg in self.history]
            
            )


        if len(self.history) > 5 :
            self.history.pop(0)

    # Inside MemoryManager class
    def clear_memory(self):
        self.memory_data = []


    def get_content(self):
        return self.history