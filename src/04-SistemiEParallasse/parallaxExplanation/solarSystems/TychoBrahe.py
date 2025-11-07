from manim import *

class SolarSystemGeocentric(Scene):
    def construct(self):
        distance = 0.45
        
        # --- Planet definitions ---
        earth = Dot((0, -3.5, 0), 0.2, color=GREEN)
        moon = Dot((0, 0, 0), 0.09, color=GREY)
        mercury = Dot((0, 0, 0), 0.1, color=YELLOW)
        venus = Dot((0, 0, 0), 0.2, color=ORANGE)
        sun = Dot((0, 0, 0), 0.9, color=YELLOW)
        mars = Dot((0, 0, 0), 0.1, color=RED)
        jupiter = Dot((0, 0, 0), 0.4, color=DARK_BROWN)
        saturn = Dot((0, 0, 0), 0.4, color=YELLOW_E)
        
        planets = [
            venus, mercury, sun, moon, earth, mars, jupiter, saturn
        ]
        planets_names = VGroup(
            Tex("Venere"), Tex("Mercurio"), Tex("Sole"),
            Tex("Luna"), Tex("Terra"), Tex("Marte"),
            Tex("Giove"), Tex("Saturno")
        )

        # --- Arrange planet positions ---
        for i in range(len(planets)):
            if i == 0:
                # Start with Venus (index 0)
                planets[i].move_to((0, -4 + planets[i].radius + 0.1, 0))
                continue

            ignored_distance = planets[i].radius + planets[i - 1].radius

            # Inner system (Venus → Earth)
            if i <= 4:
                if planets[i].radius == 0.09:
                    # Moon closer to Earth
                    planets[i].move_to(
                        (0, planets[i - 1].get_center()[1] + distance / 2 + ignored_distance, 0)
                    )
                else:
                    planets[i].move_to(
                        (0, planets[i - 1].get_center()[1] + distance + ignored_distance, 0)
                    )
            else:
                # Outer system (Mars, Jupiter, Saturn)
                # Compute base spacing equal to Venus–Earth distance
                earth_y = planets[4].get_center()[1]
                venus_y = planets[0].get_center()[1]
                base_spacing = abs(earth_y - venus_y)
                planets[i].move_to(
                    (0, planets[i - 1].get_center()[1] + base_spacing + ignored_distance, 0)
                )

        # --- Label positioning ---
        for i in range(len(planets_names)):
            planets_names[i]\
                .move_to(planets[i].get_center())\
                .shift(RIGHT * planets[i].radius)\
                .shift(RIGHT * (planets_names[i].length_over_dim(0) / 2))\
                .shift(RIGHT * 0.5)

        # --- Orbits for Mercury and Venus (around the Sun) ---
        mercury_orbit = Circle(planets[2].get_center()[1] - planets[1].get_center()[1], color=BLACK)\
            .rotate(-90*DEGREES)\
            .add_updater(lambda x: x.move_to(planets[0].get_center())) 
        venus_orbit = Circle(planets[2].get_center()[1] - planets[0].get_center()[1], color=BLACK)\
            .rotate(-90*DEGREES)\
            .add_updater(lambda x: x.move_to(planets[0].get_center()))

        # --- Show all planets ---
        for i in range(len(planets)):
            self.play(FadeIn(planets[i]), Write(planets_names[i]), run_time=0.5)

        self.play(FadeOut(planets_names))

        # --- Add orbits ---
        self.add(mercury_orbit, venus_orbit)

        # --- Animate motion ---
        planets_rotating = AnimationGroup(
            Rotate(planets[3], TAU * 3, about_point=planets[4].get_center(), rate_func=linear, run_time=5),  # Moon
            AnimationGroup(
                Rotate(planets[2], TAU * 3, about_point=planets[4].get_center(), rate_func=linear, run_time=5),  # Sun
                MoveAlongPath(planets[0], venus_orbit, rate_func=linear, run_time=5),  # Venus
                MoveAlongPath(planets[1], mercury_orbit, rate_func=linear, run_time=5),  # Mercury
                lag_ratio=0.1
            ),
            Rotate(planets[5], TAU * 3, about_point=planets[4].get_center(), rate_func=linear, run_time=5),  # Mars
            Rotate(planets[6], TAU * 2, about_point=planets[4].get_center(), rate_func=linear, run_time=5),  # Jupiter
            Rotate(planets[7], TAU * 1, about_point=planets[4].get_center(), rate_func=linear, run_time=5),  # Saturn
            lag_ratio=0.1
        )

        self.play(planets_rotating)
        self.wait(2)
