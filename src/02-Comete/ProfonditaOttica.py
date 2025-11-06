from manim import *
import random

class ProfonditaOttica(Scene):
    def construct(self):
        ########################
        ### SATURN AND ROCKS ###
        ########################
        
        # SATURN
        
        saturn = Circle(2, color=YELLOW)\
            .to_edge(LEFT)\
            .shift(LEFT*2)\
            .rotate(90 * DEGREES)  # Assuming DEGREES for clarity; adjust if needed

        # ORBITS FOR THE ROCKS
        
        rocks_orbits = VGroup(
            ImplicitFunction(lambda x, y: -y**2 - x + 4),
            ImplicitFunction(lambda x, y: -y**2 - 2*x + 1),
            ImplicitFunction(lambda x, y: -y**2 - 0.5*x + 3.5)
        )

        # ROCKS
        
        rocks = VGroup(
            VGroup(),
            VGroup(),
            VGroup(),
        )
        for orbit in range(0, 3):
            for rock in range(1, 10):
                length = random.uniform(0.5, 1.0)
                rocks[orbit].add(Line([0, 0, 0], [length, 0, 0]))



        ##################
        ### ANIMATIONS ###
        ##################
        
        self.play(DrawBorderThenFill(saturn, reverse=True))
        self.play(Create(rocks_orbits[0]), Create(rocks_orbits[1]), Create(rocks_orbits[2]))

        self.add(rocks)

        forth_anims = []
        for orbit in range(3):
            for rock in rocks[orbit]:
                forth_anims.append(MoveAlongPath(rock, rocks_orbits[orbit], run_time=2))

        self.play(*forth_anims, run_time=2)

        back_anims = []
        for orbit in range(3):
            for rock in rocks[orbit]:
                back_anims.append(MoveAlongPath(rock, rocks_orbits[orbit], run_time=2, reverse=True))

        self.play(*back_anims, run_time=2)

        self.wait(2)