from manim import *

# class Scene(Scene):
#     def construct(self):
#         frase = Tex("")
#         self.play(Write(frase))

class Shakespeare(Scene):
    def construct(self):
        frase = Tex("When beggars die, there are no comets seen\\\\the heavens themselves blaze forth the death of princes")
        self.play(Write(frase))
        
class Vendetta(Scene):
    def construct(self):
        frase = Tex("Dal movimento de l’humor collerico\\\\gli animi de gli huomini sono incitati alla vendetta")
        self.play(Write(frase))
        
class Rammarichi(Scene):
    def construct(self):
        frase = Tex("Gli huomini fuggivano per i boschi, lasciando le case loro,\\\\sì come usciti fuori di senno, non si trovava chi avesse cura de gli animali,\\\\né chi lavorasse le terre, solo morti si vedevano,\\\\solo ramarichi, stridi e pianti s’udivano")
        self.play(Write(frase))
        
class Paternoster(Scene):
    def construct(self):
        frase = Tex("Venne un certo liquore nell’aere come fuoco,\\\\e parea che la terra ardesse, e stette così per lo spazio del dire di due Paternoster;\\\\dietro a questo venne un tempo molto scuro e tenebroso con un tuono grandissimo,\\\\il quale durò fermamente per dire di tre Paternoster")
        self.play(Write(frase))