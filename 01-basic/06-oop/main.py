class me:
    def __init__(self):
        super().__init__()
        print("start")
    def helo(self):
        print("hello")
    def __del__(self):
        print("end")
if __name__ == "__main__":
    x=me()
    x.helo()
