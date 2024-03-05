class Todo:

    def __init__ (self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list = []

    def mark_completed(self):
        self.completed = True

    def add_tag (self, tag:str):
        if tag not in self.tags:
            self.tags.append (tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:

    def __init__(self):
        self.todos: dict [str, Todo]= {}

    def add_todo (self, title:str, description:str) -> int:
        id = len(self.todos) + 1
        nuevo_objeto = Todo (title, description)
        self.todos [id] = nuevo_objeto
        return id

    def pending_todos (self):
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos (self):
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count (self):
        tags_counter = {}
        for todo in self.todos:
            for tag in todo.tags:
                if tag in tags_counter:
                    tags_counter[tag] = tags_counter[tag] + 1
                else:
                    tags_counter[tag] = 1
        return tags_counter