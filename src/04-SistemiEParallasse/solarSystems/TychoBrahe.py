from manim import *
from manim.utils.space_ops import rotate_vector
import numpy as np
from math import floor

class SolarSystemTychoBrahe(Scene):
    def construct(self):
        distance = 0.45
        T = 5  # base rotation duration in seconds
        speed_factor = 3.0  # Set to three as requested

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

        # === Initial offsets ===
        offsets_earth = {p: p.get_center() - earth_center.get_center() for p in earth_orbiting_bodies}
        offsets_sun = {p: p.get_center() - sun_center.get_center() for p in sun_orbiting_bodies}

        # === Compute distances and Keplerian scaling ===
        dist_earth = {p: np.linalg.norm(offset) for p, offset in offsets_earth.items()}
        dist_sun = {p: np.linalg.norm(offset) for p, offset in offsets_sun.items()}

        # Earth system: base period for Moon = T/2
        a_inner_earth = dist_earth[moon]
        k_earth = speed_factor * (TAU / (T / 2)) * (a_inner_earth ** 1.5)

        # Sun system: base period for Mercury = T/3
        a_inner_sun = dist_sun[mercury]
        k_sun = speed_factor * (TAU / (T / 3)) * (a_inner_sun ** 1.5)

        # === Speeds ===
        speeds = {}
        for planet in earth_orbiting_bodies:
            offset = offsets_earth[planet]
            a = np.linalg.norm(offset)
            speed = k_earth / (a ** 1.5)
            speeds[planet] = speed

        for planet in sun_orbiting_bodies:
            offset = offsets_sun[planet]
            a = np.linalg.norm(offset)
            speed = k_sun / (a ** 1.5)
            speeds[planet] = speed

        # === Staggered start times ===
        order = [moon, sun, mercury, venus, mars, jupiter, saturn]
        start_times = {}
        st = 0.0
        for p in order:
            start_times[p] = st
            st += 0.5

        # === Compute align times with staggered starts ===
        align_t = {}
        TAU_EPS = 1e-8
        align_t[moon] = 5.0
        speed_sun_obj = speeds[sun]
        effective_dt_at_moon_stop_for_sun = 5.0 - start_times[sun]
        orbits = speed_sun_obj * effective_dt_at_moon_stop_for_sun / TAU
        num = floor(orbits + TAU_EPS)
        next_o = num + 1
        align_effective_dt_sun = next_o * TAU / speed_sun_obj
        align_t[sun] = start_times[sun] + align_effective_dt_sun
        for p in sun_orbiting_bodies:
            speed = speeds[p]
            effective_dt_at_sun_stop = align_t[sun] - start_times[p]
            orbits = speed * effective_dt_at_sun_stop / TAU
            num = floor(orbits + TAU_EPS)
            next_o = num + 1
            align_effective_dt = next_o * TAU / speed
            align_t[p] = start_times[p] + align_effective_dt

        max_align_t = max(align_t.values())

        # === Time tracker ===
        t = ValueTracker(0)

        # === Updaters with staggered starts and alignment stops ===
        def add_orbital_updater(planet, center, offset, speed, start_t, align_time):
            def updater(m):
                dt = t.get_value()
                effective_dt = max(0, dt - start_t)
                total_angle = speed * effective_dt
                angle = total_angle % TAU
                m.move_to(center.get_center() + rotate_vector(offset, total_angle))
                if dt >= align_time:
                    m.clear_updaters()
            planet.add_updater(updater)

        for planet in earth_orbiting_bodies:
            offset = offsets_earth[planet]
            speed = speeds[planet]
            start_t = start_times[planet]
            align_time = align_t[planet]
            add_orbital_updater(planet, earth_center, offset, speed, start_t, align_time)

        for planet in sun_orbiting_bodies:
            offset = offsets_sun[planet]
            speed = speeds[planet]
            start_t = start_times[planet]
            align_time = align_t[planet]
            add_orbital_updater(planet, sun_center, offset, speed, start_t, align_time)

        # === Trails ===
        trails = [
            TracedPath(p.get_center, stroke_color=p.get_color(), stroke_width=2, dissipating_time=0.5)
            for p in planets if p is not earth
        ]
        self.add(*trails)

        # === Sequential orbit starts with delays ===
        # Planets kick off one by one over ~3.5s, then continue to alignments (~10s total motion)
        self.play(t.animate.set_value(max_align_t + 0.1), run_time=max_align_t + 0.1, rate_func=linear)

        self.wait(2)