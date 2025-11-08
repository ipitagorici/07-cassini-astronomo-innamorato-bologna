from manim import *
from manim.utils.space_ops import rotate_vector
import numpy as np

class SolarSystemTychoBrahe(Scene):
    def construct(self):
        distance = 0.45
        T = 5  # base rotation duration in seconds

        # === Celestial bodies ===
        earth = Dot((0, -3.5, 0), radius=0.2, color=GREEN)
        moon = Dot((0, 0, 0), radius=0.09, color=GREY)
        sun = Dot((0, 0, 0), radius=0.9, color=YELLOW)
        mercury = Dot((0, 0, 0), radius=0.1, color=YELLOW_E)
        venus = Dot((0, 0, 0), radius=0.15, color=ORANGE)
        mars = Dot((0, 0, 0), radius=0.1, color=RED)
        jupiter = Dot((0, 0, 0), radius=0.35, color=DARK_BROWN)
        saturn = Dot((0, 0, 0), radius=0.4, color=YELLOW_E)

        planets = [earth, moon, sun, mercury, venus, mars, jupiter, saturn]
        planet_names = VGroup(
            Tex("Terra"), Tex("Luna"), Tex("Sole"),
            Tex("Mercurio"), Tex("Venere"), Tex("Marte"), Tex("Giove"), Tex("Saturno")
        )

        # === Position planets vertically ===
        for i, planet in enumerate(planets):
            if i == 0:
                planet.move_to((0, -4 + planet.radius + 0.1, 0))
            else:
                prev = planets[i - 1]
                offset = distance / 2 if planet.radius == 0.09 else distance
                planet.move_to(
                    (0, prev.get_center()[1] + offset + planet.radius + prev.radius, 0)
                )

        # === Position labels ===
        for i, name in enumerate(planet_names):
            name.next_to(planets[i], RIGHT)

        # === Show planets and labels ===
        for i in range(len(planets)):
            self.play(FadeIn(planets[i]), Write(planet_names[i]), run_time=0.4)
        self.play(FadeOut(planet_names))

        # === References ===
        earth_center = earth
        sun_center = sun

        # === Orbit structure ===
        earth_orbiting_bodies = [moon, sun]  # orbit Earth
        sun_orbiting_bodies = [mercury, venus, mars, jupiter, saturn]  # orbit Sun

        # === Define speeds ===
        sun_speed = TAU / (T * 2)      # slow orbit around Earth
        moon_speed = TAU / (T / 2)     # fast orbit around Earth
        sun_speeds = {
            mercury: TAU / (T / 3),
            venus: TAU / (T / 3.5),
            mars: TAU / (T / 4),
            jupiter: TAU / (T / 5),
            saturn: TAU / (T / 6),
        }

        # === Initial offsets ===
        offsets_earth = {p: p.get_center() - earth_center.get_center() for p in earth_orbiting_bodies}
        offsets_sun = {p: p.get_center() - sun_center.get_center() for p in sun_orbiting_bodies}

        # === Time tracker ===
        t = ValueTracker(0)

        def orbit_position(center, offset, speed):
            return lambda: center.get_center() + rotate_vector(offset, speed * t.get_value())

        # === Updaters ===
        for planet in earth_orbiting_bodies:
            offset = offsets_earth[planet]
            speed = sun_speed if planet is sun else moon_speed
            planet.add_updater(lambda m, off=offset, spd=speed: m.move_to(orbit_position(earth_center, off, spd)()))

        for planet in sun_orbiting_bodies:
            offset = offsets_sun[planet]
            speed = sun_speeds[planet]
            planet.add_updater(lambda m, off=offset, spd=speed: m.move_to(orbit_position(sun_center, off, spd)()))

        # === Trails ===
        trails = [
            TracedPath(p.get_center, stroke_color=p.get_color(), stroke_width=2, dissipating_time=1)
            for p in planets if p is not earth
        ]
        self.add(*trails)

        # === Sequential orbit starts ===
        # 1. Only Moon orbits first
        self.play(t.animate.set_value(T / 4), run_time=T / 4, rate_func=linear)
        self.wait(0.5)

        # 2. Sun starts orbiting Earth
        self.play(t.animate.set_value(T / 2), run_time=T / 4, rate_func=linear)
        self.wait(0.5)

        # 3. All planets orbit together
        self.play(t.animate.set_value(T * 2), run_time=T * 1.5, rate_func=linear)

        # === Fade out ===
        self.play(*[FadeOut(p, run_time=10) for p in planets])
        self.wait(2)