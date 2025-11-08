from manim import *
from manim.utils.space_ops import rotate_vector
import numpy as np

class SolarSystemEraclide(Scene):
    def fade_out_continuous(self, mobjects, duration):
        start_time = self.time
        def fade_updater(mobj):
            t = self.time - start_time
            alpha = min(t / duration, 1.0)
            mobj.set_opacity(1 - alpha)
            if alpha >= 1.0:
                mobj.remove_updater(fade_updater)
                self.remove(mobj)
        for m in mobjects:
            m.add_updater(fade_updater)

    def construct(self):
        distance = 0.45
        T = 5

        # === Celestial bodies ===
        earth = Dot((0, -3.5, 0), radius=0.2, color=GREEN)
        moon = Dot((0, -3.5 - distance, 0), radius=0.1, color=GREY)
        sun = Dot((0, -3.5 + distance, 0), radius=0.3, color=YELLOW)
        mercury = Dot(sun.get_center() + RIGHT * distance, radius=0.08, color=WHITE)
        venus = Dot(sun.get_center() + RIGHT * distance * 1.7, radius=0.1, color=ORANGE)
        mars = Dot(earth.get_center() + LEFT * distance * 1.6, radius=0.12, color=RED)
        jupiter = Dot(earth.get_center() + RIGHT * distance * 2.2, radius=0.18, color=BROWN)
        saturn = Dot(earth.get_center() + RIGHT * distance * 3.0, radius=0.16, color=BEIGE)

        planets = [earth, moon, sun, mercury, venus, mars, jupiter, saturn]
        self.add(*planets)

        # === Speeds (radians per second) ===
        T_mercury = T * 0.5
        T_venus = T * 0.8
        sun_speeds = [TAU / T_mercury, TAU / T_venus]
        mercury_speed, venus_speed = sun_speeds

        earth_orbiting_planets = [moon, mars, jupiter, saturn]
        distances = {p: np.linalg.norm(p.get_center() - earth.get_center()) for p in earth_orbiting_planets}
        base_period = T * 1.2
        earth_speeds = {
            p: TAU / (base_period * (distances[p] / min(distances.values())))
            for p in earth_orbiting_planets
        }
        sun_speed = TAU / (T * 2.0)

        # === Motion updaters ===
        moon.add_updater(lambda m, dt: m.move_to(
            rotate_vector(m.get_center() - earth.get_center(), earth_speeds[moon] * dt, axis=OUT) + earth.get_center()
        ))
        sun.add_updater(lambda s, dt: s.move_to(
            rotate_vector(s.get_center() - earth.get_center(), sun_speed * dt, axis=OUT) + earth.get_center()
        ))
        mercury.add_updater(lambda m, dt: m.move_to(
            rotate_vector(m.get_center() - sun.get_center(), mercury_speed * dt, axis=OUT) + sun.get_center()
        ))
        venus.add_updater(lambda v, dt: v.move_to(
            rotate_vector(v.get_center() - sun.get_center(), venus_speed * dt, axis=OUT) + sun.get_center()
        ))
        for p in [mars, jupiter, saturn]:
            p.add_updater(lambda obj, dt, p=p: obj.move_to(
                rotate_vector(obj.get_center() - earth.get_center(), earth_speeds[p] * dt, axis=OUT) + earth.get_center()
            ))

        # Let them move and fade out smoothly
        self.wait(5)  # let motion stabilize
        self.fade_out_continuous(planets, duration=10)
        self.wait(10)