from body import body
from nBodySimulator import nBodySimulator

time_step = 0.01
frame_step = 1
length = 20
plot_size = 1.5
file_name = 'figure_eight.mp4'


#              X               Y             Xv                 Yv     Mass
b1 = body(  0.9700436,   -0.24308753,    0.4666203685,     0.43236573, 1.0)
b2 = body( -0.9700436,    0.24308753,    0.4666203685,     0.43236573, 1.0)
b3 = body(        0.0,           0.0, -2*0.4666203685,  -2*0.43236573, 1.0)


bodies = [b1, b2, b3]
sim = nBodySimulator(bodies)
sim.setG(1)
sim.run(bodies, time_step, frame_step, length, plot_size, file_name)
