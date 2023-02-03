from ursina import *

path = (Vec3(0,0,0), Vec3(0,1,0), Vec3(0,3,0), Vec3(0,4,0), Vec3(2,5,0))
thicknesses = ((1,1), (.5,.5), (.75,.75), (.5,.5), (1,1))
e = Entity(model=Pipe(path=path, thicknesses=thicknesses))
e.model.colorize()

EditorCamera()
origin = Entity(model='cube', color=color.magenta)
origin.scale *= .25
