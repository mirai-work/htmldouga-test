import pyxel
import js

class App:

    def __init__(self):
        pyxel.init(160, 120)
        self.state = "TITLE"
        
        # JavaScript側からPythonのメソッドを呼べるように登録
        js.window.pyxel_app = self

        pyxel.run(self.update, self.draw)

    def show_photo(self):
        self.state = "PHOTO"
        # 画像ファイル名だけを渡してJSの関数を呼び出す
        js.showImage("photo.PNG")

    def photo_finished(self):
        # JS側から画像が閉じられたら、ステートをTITLEに戻す
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

App()
