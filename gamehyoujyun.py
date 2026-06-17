import pyxel
import js

class App:

    def __init__(self):
        pyxel.init(160, 120)
        self.state = "TITLE"
        js.window.pyxel_app = self
        pyxel.run(self.update, self.draw)

    def show_photo(self):
        self.state = "PHOTO"
        js.showImage("photo.PNG")

    def photo_finished(self):
        self.state = "TITLE"

    def update(self):
        if self.state == "TITLE":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.show_photo()

    def draw(self):
        pyxel.cls(0)
        if self.state == "TITLE":
            pyxel.text(20, 50, "SPACE : PHOTO", 7)
        elif self.state == "PHOTO":
            pyxel.text(35, 50, "SHOWING PHOTO...", 8)

# 【注意】App() は class の外側（左端に寄せる）で呼び出します
App()
