class EditorState :
    content: str
    def __init__(self, content: str) -> None:
        self.content = content
    def getContent(self) -> str:
        return self.content


