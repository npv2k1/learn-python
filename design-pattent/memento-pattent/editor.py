from  editorstate import EditorState 
class Editor:
    content: str
    def __init__(self) -> None:
        self.content = ""

    def get_content(self) -> str:
        return self.content
    
    def set_content(self, content: str) -> None:

        self.content = content

    def create_state(self) -> EditorState:
        return EditorState(self.content)

    def restore(self, state: EditorState) -> None:
        self.content = state.getContent()