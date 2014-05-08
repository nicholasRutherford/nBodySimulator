from nBody.src.body import Body
from nBody.src.nBodySimulator import NBodySimulator

accuarcy = 0.01
time_step = 1
frame_step = 60*60

length = 20
plot_size = 400000000 # size of the background for the animation (in meters)
file_name = 'earth_moon.mp4'

moon = Body(384400000, # x-position (distance from the earth)
         0.0, # y-position
         0.0, # x-velocity
         1000.0, # y-velocity (tangential velocity) in m/s
         7.347*(10**22)) # mass in Kg

earth = Body(0.0, # centered at the origin
        0.0, 
        0.0, # no velocity
        0.0, 
        5.97*(10**24)) # mass in Kg

planets = [moon, earth]
sim = NBodySimulator(planets)
sim.run(planets, time_step=time_step, frame_step=frame_step, 
    length=length, plot_size=plot_size, file_name=file_name)
