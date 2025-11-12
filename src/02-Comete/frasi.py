from manim import *
from PIL import Image


class StellaRossa(Scene):
    def construct(self):
        frase_sinistra = Tex("Come la stella rossa\\\\" +
                            "fiammeggiante fa\\\\"+
                            "pestilenza",
                            tex_environment="flushright",
                            font_size=60,
                            color=YELLOW)
        frase_sinistra.to_edge(LEFT).shift(UR).shift(LEFT).shift(UP*0.75)
        frase_destra = Tex("che dalla sua chioma\\\\"+ 
                            "calare malattie\\\\"+
                            "e guerra\\\\" +
                            "(Omero)",
                            tex_environment="flushleft",
                            font_size=60,
                            color=YELLOW)
        frase_destra.to_edge(RIGHT).shift(UL).shift(RIGHT).shift(UP*0.5)
        
        elmo = ImageMobject("src/assets/elmoPiumaRossa.png")\
            .scale(1.3)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(elmo))
        self.play(Write(frase_sinistra), Write(frase_destra))

class Shakespeare(Scene):
    def construct(self):
        fraseEnglish = Tex("When beggars die, there are no comets seen;\\\\the heavens themselves blaze forth the death of princes",
                    font_size=50,
                    color=YELLOW).shift(UP*1.5)
        fraseItalian = Tex("Quando muoiono i pezzenti, non si vedono comete;\\\\i cieli stessi fiammeggiano annunziando la morte dei Principi",
                    font_size=50,
                    color=YELLOW).next_to(fraseEnglish, DOWN*4)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(fraseEnglish), Write(fraseItalian))
        
class Vendetta(Scene):
    def construct(self):
        frase = Tex("Dal movimento de l’humor collerico\\\\gli animi de gli huomini sono incitati alla vendetta",
                    font_size=60,
                    color=YELLOW)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(frase))
        
class Rammarichi(Scene):
    def construct(self):
        frase = Tex("Gli huomini fuggivano per i boschi,\\\\lasciando le case loro,\\\\" +
                    "sì come usciti fuori di senno,\\\\non si trovava chi avesse cura de gli animali,\\\\" +
                    "né chi lavorasse le terre, solo morti si vedevano,\\\\" +
                    "solo ramarichi, stridi e pianti s’udivano",
                    font_size=60,
                    color=YELLOW)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(frase))
        
class Paternoster(Scene):
    def construct(self):
        frase = Tex("Venne un certo liquore nell’aere come fuoco,\\\\" +
                    "e parea che la terra ardesse,\\\\e stette così per lo spazio del dire di due Paternoster;\\\\" +
                    "dietro a questo venne un tempo\\\\molto scuro e tenebroso con un tuono grandissimo,\\\\" +
                    "il quale durò fermamente\\\\per il dire di tre Paternoster",
                    font_size=58,
                    color=YELLOW)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(frase))
        
class StragiAllaCristianita(Scene):
    def construct(self):
        frase = Tex("Gran stragi alla Cristianità,\\\\onde papa Callisto III ordinò,\\\\"+
                    "ch’in tutte le città nel mezzo giorni\\\\si suonassero le campane,\\\\"+
                    "acciò in quel tempo i fedeli\\\\facessero orazioni per placare l’ira del cielo",
                    font_size=65,
                    color=YELLOW)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        self.play(Write(frase))



