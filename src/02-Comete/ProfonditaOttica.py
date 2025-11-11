from manim import *
import random

class ProfonditaOttica(MovingCameraScene):
    def construct(self):
        def show_rays_trying_to_pass(light_rays, light_rays_lengths):
            arrow_bases = [arrow.get_start() for arrow in light_rays]
            x_arrows = [base[0] for base in arrow_bases]
            y_base = arrow_bases[0][1]  
            
            rock_positions = []
            for orbit_rocks in rocks:
                for rock in orbit_rocks:
                    rock_positions.append(rock.get_center())
                    
            distances = []
            for x_arrow in x_arrows:
                above_rocks = [(pos, abs(pos[0] - x_arrow)) for pos in rock_positions if pos[1] > y_base]
                if above_rocks:
                    closest_rock = min(above_rocks, key=lambda item: item[1])[0]
                    dist = closest_rock[1] - y_base
                    distances.append(dist)
                else:
                    distances.append(0)
                    
            animations = []
            for ray_index in range(0, len(light_rays)):
                animations.append(light_rays_lengths[ray_index].animate.set_value(distances[ray_index]))
                animations.append(FadeOut(light_rays[ray_index]))
                
            ray_animations = AnimationGroup(*animations)
            return ray_animations



        ########################
        ### SATURN AND ROCKS ###
        ########################
        
        # SATURN
        saturn = Circle(2, color=YELLOW_E)\
            .set_fill(opacity=1)\
            .to_edge(LEFT)\
            .shift(LEFT*2.5)\
            .rotate(90 * DEGREES)\
            .set_z_index(1)
            
        # ORBITS FOR THE ROCKS
        rocks_orbits = VGroup(
            ImplicitFunction(lambda x, y: -y**2 - 0.5*x + 1),
            ImplicitFunction(lambda x, y: -y**2 - x + 4),
            ImplicitFunction(lambda x, y: -y**2 - 0.5*x + 3.5)
        ).shift(DOWN).set_z_index(0)
        
        # ROCKS
        rocks = VGroup(
            VGroup(),
            VGroup(),
            VGroup(),
        )
        for orbit in rocks:
            for i in range(0, 70):
                length = random.uniform(0.1, 0.8)
                orbit.add(Ellipse(length, length/4, color=GRAY))
        for orbit in range(3):
            for rock in rocks[orbit]:
                orbit_points = rocks_orbits[orbit].get_all_points()
                rock_position = random.choice(orbit_points)
                rock.move_to(rock_position)
                
                
                
        ############################
        ### SONDA AND TRAJECTORY ###
        ############################
        
        line = Line([0, 0, 0], [0, 1, 0])
        rectangle = Rectangle(height=0.5, width=1.3, color=YELLOW)\
            .set_fill(opacity=0.5)\
            .move_to(line.get_center())\
            .shift(RIGHT*0.65)
            
        sonda = VGroup(line, rectangle).to_edge(UL)
        sonda_trajectory = Line(sonda.get_center(),
                                sonda.get_center() + [12, 0, 0])
        
        
        
        ##################
        ### LIGHT RAYS ###
        ##################
        
        light_rays = VGroup()
        light_rays_lengths = []
        
        for i in range(10):
            length = ValueTracker(3)
            light_rays_lengths.append(length)
            
            distance = random.uniform(0.1, 3)
            arrow = always_redraw(lambda: Arrow(start=DOWN, end=UP*length.get_value(), color=RED))

            light_rays.add(arrow)
            
        for j in range(10):
            if j == 0:
                light_rays[j].to_edge(LEFT).shift(RIGHT*3)
                light_rays[j+1].next_to(light_rays[j], RIGHT*distance)
            elif j != 9:
                light_rays[j+1].next_to(light_rays[j], RIGHT*distance)
                
        light_rays.shift(DOWN*7.5)
        
        
        
        ##################
        ### ANIMATIONS ###
        ##################
        
        self.play(DrawBorderThenFill(saturn, reverse=True))
        #self.play(Create(rocks_orbits[0]), Create(rocks_orbits[1]), Create(rocks_orbits[2]))
        for orbit in range(3):
            self.play(ShowIncreasingSubsets(rocks[orbit], run_time=0.5))
        self.play(Create(sonda))

        self.play(
            LaggedStart(
                self.camera.frame.animate.move_to(light_rays.get_top()),
                show_rays_trying_to_pass(light_rays, light_rays_lengths),
                lag_ratio=0.8,
            )
        )
        self.play(Create(sonda_trajectory))
        self.play(MoveAlongPath(sonda, sonda_trajectory, run_time=4, func_rate=linear))
        self.wait(2)