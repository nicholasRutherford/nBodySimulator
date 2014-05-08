"""
An N-Body simulator which outputs an mp4 file of the simulation. 
Requires ffmpeg.
Author: Nicholas Rutherford
"""

import numpy as np 
from math import sqrt
from matplotlib import pyplot as plt 
from matplotlib import animation

from body import Body

class NBodySimulator(object):
    """Run an N-body and save it to a file or run realtime"""

    def __init__(self, bodies):
        """Create a new simulation

        bodies - list of bodies that are to be simulated
        """

        self.G =  6.67384*(10**(-11))
        self.bodies = bodies
        self.minDist = 0.01

    def setG(self, i):
        """Change the value of the gravitational constant

        i - new value for G
        """
        self.G = i

    def calcAcc(self, m1, m2):
        """Calculate the acceleration on m1 from m2

        m1 - body being accelerated
        m2 - body that exerts it's gravitational pull on the other
        """

        # Fx = (G * m1 * m2)(x1 - x2)/(total_distance)
        term1 = self.G * m1.mass * m2.mass 
        distance = sqrt((m1.xPos-m2.xPos)**2 + (m1.yPos-m2.yPos)**2)
        total_force = term1/(distance**2)

        forceX = (abs(m1.xPos - m2.xPos))*total_force/distance
        forceY = (abs(m1.yPos - m2.yPos))*total_force/distance

        # Prevent unreasonably large accelerations 
        # by limiting the minimum distance.
        if -self.minDist < m2.xPos - m1.xPos < self.minDist:
            forceX = 0.0

        if -self.minDist < m2.yPos - m1.yPos < self.minDist: 
            forceY = 0.0  

        if (m1.xPos - m2.xPos) > 0.0:
            forceX = forceX * -1
        
        if (m1.yPos - m2.yPos) > 0.0:
            forceY = forceY * -1

        # Acceleration = Force/mass
        xAcl = forceX/m1.mass
        yAcl= forceY/m1.mass

        return xAcl, yAcl

    def step(self, dt):
        """Do one step of the simulation with time step dt

        dt - time to jump between simulations"""

        # Calculate the new acceleration for each body by iterating through each
        # body and calculating the force excreted by it
        for b1 in self.bodies:

            #reset acceleration for the new step
            b1.xAcl = 0.0
            b1.yAcl = 0.0

            for b2 in self.bodies:
                if b2 != b1:
                    xAcl, yAcl = self.calcAcc(b1, b2)

                    #update acceleration total so far
                    b1.xAcl += xAcl
                    b1.yAcl += yAcl

        # Update velocities and positions
        for body in self.bodies:
            body.xVel += body.xAcl * dt
            body.yVel += body.yAcl * dt
            body.xPos += body.xVel * dt
            body.yPos += body.yVel * dt
        
    def run(self, bodies, **kwargs):
        """Run the simulation.

        bodies - List of bodies to simulate

        Keyword Arguments:
        time_step - how much to jump in time per step
        frame_step - create a new animation frame every x steps
        length - length of the animation in seconds
        plot_size - size of the background of the animation
        file_name - name to save the animation as
        real_time - whether or not to show the animation as the simulation
                        runs instead of saving it to a file
        """

        defaults = {
            'time_step':0.1,
            'frame_step':10,
            'length':10,
            'plot_size':100,
            'file_name':'simulation.mp4',
            'real_time':False
        }

        defaults.update(kwargs)
        time_step = defaults['time_step']
        frame_step = defaults['frame_step']
        length = defaults['length']
        plot_size = defaults['plot_size']
        file_name = defaults['file_name']
        real_time = defaults['real_time']

         # frames per second for the video to be saved in
        fps = 60

        # total number of frames in the video
        total_frames= fps * length

 
        fig = plt.figure()
        sub_plot = fig.add_subplot(111, aspect='equal', autoscale_on=False,
        xlim=(-plot_size, plot_size), ylim=(-plot_size, plot_size))

        # The positions of the bodies will be marked by blue circles of size 6
        positions, = sub_plot.plot([], [], 'bo', ms=6)

        # Trails will add red points at all the previous locations of the bodies
        trails, = sub_plot.plot([], [], 'r.', ms=2, alpha=0.20)

        # Store the history of the bodies
        x_history = []
        y_history = []

        if real_time:
            fig.show()

        def animate(i):
            """Animate function required by matplotlib.

            i - does nothing, but required by matplotlib"""

            for x in xrange(frame_step):
                self.step(time_step)

            xPosition = []
            yPosition = []
            for body in bodies:
                x_history.append(body.xPos)
                y_history.append(body.yPos)
                xPosition.append(body.xPos)
                yPosition.append(body.yPos)

            trails.set_data(x_history, y_history)
            positions.set_data(xPosition, yPosition)
            
            if real_time:
                fig.canvas.draw()

            return positions, trails

        if real_time:
            for x in xrange(total_frames):
                animate(1)
        else:
            anim = animation.FuncAnimation(fig, animate, frames=total_frames)
            anim.save(file_name, fps=fps, extra_args=['-vcodec', 'libx264'])
