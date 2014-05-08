from nBody.src.body import Body
from nBody.src.nBodySimulator import NBodySimulator


time_step = 0.01
frame_step = 10
length = 10
plot_size = 20
file_name = 'twelve_bodies.mp4'

vMult1 = 1
vMult2 = -1.5
vMult3 = 1
massScale = 0.5
massScale2 = 0.25

#           X     Y     Xv               Yv    Mass
b1 = Body( 0.0,  3.0,  1.0*vMult1,  0.0*vMult1, 4.0)
b2 = Body( 3.0,  0.0,  0.0*vMult1, -1.0*vMult1, 4.0)
b3 = Body( 0.0, -3.0, -1.0*vMult1,  0.0*vMult1, 4.0)
b4 = Body(-3.0,  0.0,  0.0*vMult1,  1.0*vMult1, 4.0)

b5 = Body( 0.0,  9.0,  1.0*vMult2,  0.0*vMult2, 4.0*massScale)
b6 = Body( 9.0,  0.0,  0.0*vMult2, -1.0*vMult2, 4.0*massScale)
b7 = Body( 0.0, -9.0, -1.0*vMult2,  0.0*vMult2, 4.0*massScale)
b8 = Body(-9.0,  0.0,  0.0*vMult2,  1.0*vMult2, 4.0*massScale)

b9  = Body( 0.0,  15.0,  1.0*vMult3,  0.0*vMult3, 4.0*massScale2)
b10 = Body( 15.0,  0.0,  0.0*vMult3, -1.0*vMult3, 4.0*massScale2)
b11 = Body( 0.0, -15.0, -1.0*vMult3,  0.0*vMult3, 4.0*massScale2)
b12 = Body(-15.0,  0.0,  0.0*vMult3,  1.0*vMult3, 4.0*massScale2)


bodies = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]

sim = NBodySimulator(bodies)
sim.setG(1)
sim.run(bodies, time_step=time_step, frame_step=frame_step,
         length=length, plot_size=plot_size, file_name=file_name)
