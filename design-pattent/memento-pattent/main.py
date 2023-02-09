
from editor import Editor
from history import History
if __name__ == '__main__':
    editor = Editor()
    history = History()

    editor.set_content("a")
    history.push(editor.create_state())

    editor.set_content("b")
    history.push(editor.create_state())

    editor.set_content("c")
    editor.restore(history.pop())

    print(editor.get_content())