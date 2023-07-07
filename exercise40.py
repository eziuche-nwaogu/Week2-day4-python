class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_birthday = ["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"]
happy_bday = Song(happy_birthday)
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])
another_essay = Song(["You can think about a module as a specialized dictionary", "that can store Python code so you can access it with the .operator"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
another_essay.sing_me_a_song()