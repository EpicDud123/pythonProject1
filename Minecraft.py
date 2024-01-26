from ursina import *

app = Ursina()
entity = Entity(model='cube', color=color.cyan)
camera = EditorCamera()
floor_texture = load_texture(r'C:\Users\WinstonBai\Downloads\Among Us Logo - Download Free Vector PNG.png')
floor = Entity(
    model='plane',
    texture=floor_texture,
    texture_scale=(20, 20),  # Increase the texture scale to make the floor larger
    scale=(20, 1, 20),  # Adjust the scale of the plane to make it larger
    collider='box',
)
floor.y=-entity.scale_y/2

def update():
    movement()
    camera_move()
    # Get the change in mouse position since the last frame
    dx, dy = held_keys['mouse_x'], held_keys['mouse_y']
    #camera.rotation_y -= 0.5 #dx * 100  # Rotate the camera left/right
    #camera.rotation_x += 0.5 #dy * 100  # Rotate the camera up/down
def movement():
    entity.position += entity.left * time.dt*2 * held_keys['a']
    entity.position += entity.right * time.dt*2 * held_keys['d']
    entity.position += entity.forward * time.dt*2 * held_keys['w']
    entity.position += entity.back * time.dt*2 * held_keys['s']
    entity.position += entity.up * time.dt*2 * held_keys['q']
    entity.position += entity.down * time.dt*2 * held_keys['e']
def camera_move():
    camera.z += held_keys["u"]*time.dt*3
    camera.z -= held_keys["o"]*time.dt*3
    camera.x += held_keys["l"]*time.dt*3
    camera.x -= held_keys["j"]*time.dt*3
    camera.y += held_keys["i"]*time.dt*3
    camera.y -= held_keys["k"]*time.dt*3
app.run()       # opens a window and starts the game.