from manim import *
import random

class ProfonditaOttica(MovingCameraScene):
    def show_random_objects_creation(collection_of_mobjects):
        
        random_creation = AnimationGroup(
            
        )
    
    def construct(self):
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
        distance = 4
        
        for i in range(10):
            light_rays.add(Arrow(start= DOWN, end=UP*3, color=RED))
        for j in range(10):
            if j == 0:
                light_rays[j].to_edge(LEFT).shift(RIGHT*0.5)
                light_rays[j+1].next_to(light_rays[j], RIGHT*distance)
            elif j != 9:
                light_rays[j+1].next_to(light_rays[j], RIGHT*distance)
                
        light_rays.shift(DOWN*7.5)



        ##################
        ### ANIMATIONS ###
        ##################
        
        self.add(light_rays)
        
        self.play(DrawBorderThenFill(saturn, reverse=True))
        #self.play(Create(rocks_orbits[0]), Create(rocks_orbits[1]), Create(rocks_orbits[2]))

        for orbit in range(3):
            self.play(ShowIncreasingSubsets(rocks[orbit], run_time=0.5))    
                
        self.play(Create(sonda))
        
        light_moving = DrawBorderThenFill(light_rays, run_time=0.5)
        light_moving_slow = DrawBorderThenFill(light_rays, run_time=1)
        self.play(AnimationGroup(self.camera.frame.animate.move_to(light_rays), light_moving_slow))
        self.play(light_moving)
        self.play(light_moving)
        self.play(light_moving)
        self.play(light_moving)
        self.play(light_moving)
        self.play(AnimationGroup(light_moving_slow, self.camera.frame.animate.shift(UP*6.5)))
        
        self.play(Create(sonda_trajectory))
        self.play(MoveAlongPath(sonda, sonda_trajectory, run_time=4, func_rate=linear))


        self.wait(2)