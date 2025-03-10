from manim import *
import numpy as np
from scipy.spatial import distance

class KNNAnimation(Scene):
    def construct(self):
        # Define cluster points
        zeroth_column = np.array([1,1,0])
        cluster1 = (np.random.rand(3,3)*-1 + 1) * zeroth_column
        cluster2 = (np.random.rand(3,3) + 1) * zeroth_column
        cluster3 = ((np.random.rand(3,3) - 1
                     ) * zeroth_column) *np.array([-1, 1, 0])

        # Define new point
        new_point = np.array([0, 0, 0])


        # Convert 2d coords to flat 3d coords
        def to_manim_coords(point):
            new_coords = np.array([point[0], point[1], 0])
#            print(new_coords)
            return new_coords

        # All points in a single cluster
        all_clusters = np.concatenate((cluster1, cluster2, cluster3))


        # Cluster lists with each point in a single color
        cluster1_dots = [Dot(point=p, color=BLUE) for p in cluster1]
        cluster2_dots = [Dot(point=p, color=GREEN) for p in cluster2]
        cluster3_dots = [Dot(point=p, color=RED) for p in cluster3]


        # List with all np.array points
        all_points = np.concatenate([cluster1, cluster2, cluster3])

        # List with all manim dots
        all_dots = cluster1_dots + cluster2_dots + cluster3_dots

        # Centers the camera to the new_point
        self.camera.frame_center = new_point

        # Adjust camera
        self.camera.frame_height= 7
        self.camera.frame_width = 6

        # Create all dots simultaneaously
        self.play(*[Create(dot) for dot in all_dots])

        # Creates the new dot
        new_dot = Dot(to_manim_coords(new_point), color=WHITE).scale(1.2)
        self.play(Create(new_dot))

        # Order dots in order of distance
        dist_dot_color_list = []

        i=0
        for p in all_points:
            dist_from_new_point = distance.euclidean(new_point, p)
            color = all_dots[i].color
            dist_dot_color_list.append([dist_from_new_point, all_dots[i], color])
            i +=1

        sorted_list = sorted(dist_dot_color_list, key=lambda x: x[0])

        # Draw all connections
        i=0

        line_list = []
        for list in sorted_list:
            line = Line(new_dot.get_center(), # Create a line from new_point
                        list[1].get_center(), # to the dot
                        color=list[1].color) # with the dot color

            i+=1
            self.play(Create(line), run_time=0.1)#np.pi/10) # Plays in 0.314 seconds

            line_list.append(line)




        # Remove all points
        self.play(*[Uncreate(p) for p in all_dots])


        # Organize all lines on the side
        line_group = VGroup(line_list)
        self.play(line_group.animate.arrange_in_grid(rows=3, columns=3,
                                                     buff=0.1,
                                                     row_alignments='uuu',
                                                     col_alignments='lll')) # First item is the center


        # Animates them being arranged
#        animation_1 = line_group.animate.align_on_border(UP + RIGHT)#[-1,1,0])
#        animation_2 = line_group.animate.arrange(DOWN, buff=0.1, center=False)
#        animation_list = [animation_2, animation_1]
#        self.play(AnimationGroup(animation_list, lag_ratio=0))

        #self.play(line_list[0].animate.align_on_border([-1,1,0])) # Align to top_right border
        # This way, when center=False, it is used as the start of the alignment
        #self.play(line_group.animate.set_angle(0))
        #self.play(line_group.animate.arrange(DOWN, buff=0.1,
         #                                    center=False)) # First item is the center

        # Move new_dot to below the columns


        # Set center of camera to center of grid


        # Add text above grid

        # Iterate through values of k = [0,5]
        ## For each value of k, highlight the lines used, and change new_dot color.



        ignore_below = '''
        # Compute distances and select nearest neighbors
        all_points = np.vstack([cluster1, cluster2, cluster3])
        colors = [BLUE] * len(cluster1) + [GREEN] * len(cluster2) + [RED] * len(cluster3)
        distances = [distance.euclidean(new_point, p) for p in all_points]
        nearest_indices = np.argsort(distances)[:3]  # K = 3

        # Draw connections to nearest neighbors
        lines = []
        for i in nearest_indices:
            neighbor = all_points[i]
            neighbor_dot = Dot(to_manim_coords(neighbor), color=colors[i])
            line = Line(new_dot.get_center(), neighbor_dot.get_center(), color=colors[i])
            lines.append(line)

        self.play(*[Create(line) for line in lines])

        # Determine majority class
        neighbor_colors = [colors[i] for i in nearest_indices]
        majority_color = max(set(neighbor_colors), key=neighbor_colors.count)

        # Assign new color to new point
        self.play(new_dot.animate.set_color(majority_color))

        # Hold final frame
        self.wait(2)
        '''
        self.wait(3)
