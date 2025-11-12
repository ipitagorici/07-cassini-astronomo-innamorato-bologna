from manim import *
from PIL import Image

class SeIlSarsi(Scene):
    def construct(self):
        frase = Tex("Se il Sarsi vuole ch’io creda che i Babilonii\\\\"+
                    "cocesser l’uova col girarle velocemente nella fionda, io lo crederò;\\\\"+
                    "ma dirò bene, la cagione di tal effetto esser lontanissima da quella che gli viene attribuita,\\\\"+
                    "e per trovar la vera io discorrerò così:\\\\"+
                    "\"Se a noi non succede un effetto che ad altri altra volta è riuscito,\\\\"+
                    "è necessario che noi nel nostro operare manchiamo di quello che fu causa della riuscita d’esso effetto,\\\\"+
                    "e che non mancando a noi altro che una cosa sola, questa sola cosa sia la vera causa:\\\\"+
                    "ora, a noi non mancano uova, né fionde, né uomini robusti che le girino,\\\\"+
                    "e pur non si cuocono, anzi, se fusser calde, si raffreddano più presto;\\\\"+
                    "e perché non ci manca altro che l’esser di Babilonia,\\\\"+
                    "adunque l’esser Babilonie è la causa dell’indurirsi l’uova, e non l’attrizion dell’aria\"",
                    color=YELLOW,
                    font_size=35)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        self.play(Write(frase))

class HaecInsomni(Scene):
    def construct(self):
        fraseLatino = Tex("\"Haec insomni studio\\\\per gelidas noctes Coelitus deducta\" \\\\",
                    color=YELLOW,
                    font_size=60).shift(UP*1.5)
        fraseItaliano = Tex("Queste cose tratte dal cielo\\\\con studio insonne nel gelo delle notti\\\\"+
                            "(Cassini)",
                    color=YELLOW,
                    font_size=60).shift(DOWN*2)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        self.play(Write(fraseLatino), Write(fraseItaliano))