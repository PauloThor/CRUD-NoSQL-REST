class Post:
    id = 1

    def __init__(self, created_at, updated_at, title: str, author: str,
    tags: list, content: str):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content