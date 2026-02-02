class Media:
    def __init__(self, title):
        self.title = title


class Book(Media):
    def read(self):
        return f"📖 {self.title} o‘qilmoqda"


class Video(Media):
    def play(self):
        return f"🎬 {self.title} ijro etilmoqda"


print(Book("Python").read())
print(Video("Django darsi").play())
