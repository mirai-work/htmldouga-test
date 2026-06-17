import pyxel
import js
from pyodide.ffi import create_proxy # ← これが必要です！

class App:

    def __init__(self):
        pyxel.init(160, 120)
        self.state = "TITLE"
        pyxel.run(
            self.update,
            self.draw
        )

    def play_movie(self, filename):
        self.state = "MOVIE"
        
        # JavaScriptに安全にPythonの関数を渡すための「プロキシ」を作成
        # これによりJavaScript側から実行されても self を見失わなくなります
        js_callback = create_proxy(self.movie_finished)

        # 文字列ではなく、作成したプロキシを直接渡す
        js.playMovie(filename, js_callback)

    def movie_finished(self):
        print("動画終了")
        self.state = "TITLE"

    def update(self):
        if self.state == "TITLE":
            if pyxel.btnp(pyxel.KEY_1):
                self.play_movie("opening.mp4")

            if pyxel.btnp(pyxel.KEY_2):
                self.play_movie("ending.mp4")

            if pyxel.btnp(pyxel.KEY_3):
                self.play_movie("sonota.mp4")

    def draw(self):
        pyxel.cls(0)

        if self.state == "TITLE":
            pyxel.text(20, 20, "1 : OPENING", 7)
            pyxel.text(20, 40, "2 : ENDING", 7)
            pyxel.text(20, 60, "3 : SONOTA MOVIE", 7)

        elif self.state == "MOVIE":
            pyxel.text(
                35,
                60,
                "MOVIE PLAYING...",
                8
            )

App()
