"""
Sprite Explosion

Simple program to show creating explosions with particles

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_explosion_particles
"""
import random
import math
import arcade
import time
from arcade.application import MOUSE_BUTTON_LEFT, MOUSE_BUTTON_MIDDLE, MOUSE_BUTTON_RIGHT

ENEMY_SPEED=10
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.1
SPRITE_SCALING_LASER = 0.8
ENEMY_COUNT = 1
ENEMY_BULLET_OFFSET = 100

GOOFYAHHCOLORS = lambda: (random.randint(0,255), random.randint(0,255), random.randint(0,255))
GOOFYAHHRAINBOWS=[[255, 0, 0],[	255, 165, 0],[234, 255, 0],[0, 255, 0], [0, 0, 255],[0, 229, 255],[255, 0, 247]]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Explosion Example"

BULLET_SPEED = 5
PLAYER_HEALTH=99999
PLAYUH_BOLLET_BAOH=75


# --- Explosion Particles Related

# How fast the particle will accelerate down. Make 0 if not desired
PARTICLE_GRAVITY = 0.0

# How fast to fade the particle
PARTICLE_FADE_RATE = 8

# How fast the particle moves. Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5

# How many particles per explosion
PARTICLE_COUNT = 20

# How big the particle
PARTICLE_RADIUS = 3

# Possible particle colors
PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
                   arcade.color.COQUELICOT,
                   arcade.color.LAVA,
                   arcade.color.KU_CRIMSON,
                   arcade.color.DARK_TANGERINE]

# Chance we'll flip the texture to white and make it 'sparkle'
PARTICLE_SPARKLE_CHANCE = 0.02

# --- Smoke
# Note: Adding smoke trails makes for a lot of sprites and can slow things
# down. If you want a lot, it will be necessary to move processing to GPU
# using transform feedback. If to slow, just get rid of smoke.

# Start scale of smoke, and how fast is scales up
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03

# Rate smoke fades, and rises
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5

# Chance we leave smoke trail
SMOKE_CHANCE = 0.25


class Bullet(arcade.Sprite):
    def __init__(
            self,
            filename=":resources:images/space_shooter/laserBlue01.png",
            size=1,
            owner="enemy",
            breathing_time=10,
            *args,
            **kwargs,
    ):
        super().__init__(filename, size, *args, **kwargs)
        self.breathing_time=breathing_time
        self.owner = owner

    def update(self):
        self.breathing_time -= 1 / 60
        if self.breathing_time <= 0:
            self.remove_from_sprite_lists()
        self.center_y += self.change_y
        self.center_x += self.change_x
        """ Update this particle """
        # if self.alpha <= PARTICLE_FADE_RATE:
        #     # Remove faded out particles
        #     self.remove_from_sprite_lists()
        # else:
        #     # Update values
        #     self.alpha -= SMOKE_FADE_RATE
        #     self.center_x += self.change_x
        #     self.center_y += self.change_y
        #     self.scale += SMOKE_EXPANSION_RATE



class Smoke(arcade.SpriteCircle):
    """ This represents a puff of smoke """
    def __init__(self, size, color=GOOFYAHHCOLORS()):
        super().__init__(size, color, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def update(self):
        """ Update this particle """
        if self.alpha <= PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += SMOKE_EXPANSION_RATE


class Particle(arcade.SpriteCircle):
    """ Explosion particle """
    def __init__(self, my_list):
        # Choose a random color
        color = random.choice(PARTICLE_COLORS)

        # Make the particle
        super().__init__(PARTICLE_RADIUS, color)

        # Track normal particle texture, so we can 'flip' when we sparkle.
        self.normal_texture = self.texture

        # Keep track of the list we are in, so we can add a smoke trail
        self.my_list = my_list

        # Set direction/speed
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed

        # Track original alpha. Used as part of 'sparkle' where we temp set the
        # alpha back to 255
        self.my_alpha = 255

        # What list do we add smoke particles to?
        self.my_list = my_list

    def update(self):
        """ Update the particle """
        if self.my_alpha <= PARTICLE_FADE_RATE:
            # Faded out, remove
            self.remove_from_sprite_lists()
        else:
            # Update
            self.my_alpha -= PARTICLE_FADE_RATE
            self.alpha = self.my_alpha
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y -= PARTICLE_GRAVITY

            # Should we sparkle this?
            if random.random() <= PARTICLE_SPARKLE_CHANCE:
                self.alpha = 255
                self.texture = arcade.make_circle_texture(int(self.width),
                                                          arcade.color.WHITE)
            else:
                self.texture = self.normal_texture

            # Leave a smoke particle?
            if random.random() <= SMOKE_CHANCE:
                smoke = Smoke(5, color=GOOFYAHHCOLORS())
                smoke.position = self.position
                self.my_list.append(smoke)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.spinnygunangle=0#degrees

        self.player_health=PLAYER_HEALTH

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.explosions_list = None

        # Set up the player info
        self.player = None
        self.score = 0
        self.playerbreathing = True

        self.frame_count = 0
        self.last_enemy_count=0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = [
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\pewpewpowpow.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\pewpewpowpow.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\powpew.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\powpew.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\powpew.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\powpew.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\pewpewpowpow.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\epicpewsound.wav")
        ]
        self.hit_sound = [
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\despacito.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\Emotional Damage.wav"),
            arcade.sound.load_sound(r"C:\Users\WinstonBai\OneDrive\Documents\Audacity\Never Gonna Give You Up Original (1).wav")
        ]
        self.background = arcade.load_texture(r"C:\Users\WinstonBai\Downloads\super-mario-bros-1-1-i20783.jpg")
        self.background_0_x = 0
        self.background_1_x = SCREEN_WIDTH
        self.background_0_y = 0
        self.background_1_y = SCREEN_HEIGHT

        self.t0=time.time()
        self.t1 = time.time()
        self.game_over = False


    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player = arcade.Sprite(r"C:\Users\WinstonBai\Downloads\Whentheimposterissus.png",
                                    SPRITE_SCALING_PLAYER)
        self.player.center_x = 50
        self.player.center_y = 70
        self.player_list.append(self.player)

        # Create the coins
        for coin_index in range(ENEMY_COUNT):
            self.spawn_enemy()

            # Create the enemy instance
            # Coin image from kenney.nl


        self.last_enemy_count = len(self.enemy_list)

    def spawn_enemy(self, emeny=r"C:\Users\WinstonBai\Downloads\Hewalk.png", angel=90, slace=SPRITE_SCALING_COIN):

        enemy = arcade.Sprite(emeny, slace)

        enemy.angle = angel
        # Position the enemy
        enemy.center_x = random.randrange(SCREEN_WIDTH)
        enemy.center_y = random.randrange(150, SCREEN_HEIGHT)

        # Add the enemy to the lists
        self.enemy_list.append(enemy)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # draw background
        arcade.draw_lrwh_rectangle_textured(self.background_0_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_lrwh_rectangle_textured(self.background_1_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.background_0_x -= 1
        self.background_1_x -= 1
        if self.background_0_x<=-SCREEN_WIDTH:
            self.background_0_x=SCREEN_WIDTH
        if self.background_1_x<=-SCREEN_WIDTH:
            self.background_1_x=SCREEN_WIDTH


        # Draw all the sprites.
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.explosions_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        if self.playerbreathing==False:
            if not self.game_over:
                self.game_over = True
                self.t1 = time.time()
            arcade.draw_text(f"you die!!!!", start_x=SCREEN_WIDTH//2-200, start_y=SCREEN_HEIGHT//2, color=arcade.color.WHITE, font_size=60, width=400, align="center")
            arcade.draw_text(f"Time: {round(self.t1-self.t0, 1)} secs, Wow you really suck don't you", start_x=SCREEN_WIDTH // 2 - 200, start_y=100, color=arcade.color.WHITE, font_size=14, width=400, align="center")
        if self.score>=ENEMY_COUNT:
            if not self.game_over:
                self.game_over = True
                self.t1 = time.time()
            arcade.draw_text(f"you did it!!!!, you killed all the set ships now can you go on with this blocking your view", start_x=SCREEN_WIDTH // 2 - 200, start_y=SCREEN_HEIGHT // 2, color=arcade.color.WHITE, font_size=60, width=400, align="center")
            arcade.draw_text(f"Time: {round(self.t1 - self.t0, 1)} secs, Wow you really are slow aren't you",start_x=SCREEN_WIDTH // 2 - 200, start_y=100, color=arcade.color.WHITE, font_size=14,width=400, align="center")
        if self.playerbreathing == True:
            #health bar display
            #graphical health bar
            arcade.draw_text(self.player_health, self.player.center_x, self.player.center_y-40, color=arcade.color.WHITE, font_size=14)
            width=50
            relative=self.player_health/PLAYER_HEALTH
            a_color=(255-255*relative,255*relative,0)
            arcade.draw_rectangle_filled(self.player.center_x, self.player.center_y-40, 5, width*relative, a_color, 90)






            # text health bar
            # arcade.draw_text(self.player_health, self.player.center_x-20, self.player.center_y+30, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player.center_x = x
        self.player.center_y= y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        if MOUSE_BUTTON_LEFT==button:
            # Gunshot sound
            arcade.sound.play_sound(random.choice(self.gun_sound))

            # Create a bullet
            bullet = Bullet(r"C:\Users\WinstonBai\Downloads\hahafunnygunimage.jpg", SPRITE_SCALING_LASER, owner="player")

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 90

            # Give it a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player.center_x
            bullet.bottom = self.player.top+25

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)
        elif MOUSE_BUTTON_RIGHT==button:
            #Gunshot sound
            arcade.sound.play_sound(random.choice(self.gun_sound))

            # Create a bullet
            bullet = Bullet(r"C:\Users\WinstonBai\Downloads\Cowboytrump.png", 0.1,
                            owner="player_right")

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = self.spinnygunangle - 90

            # Give it a speed
            bullet.change_x = BULLET_SPEED * math.cos(math.radians(self.spinnygunangle))
            bullet.change_y = BULLET_SPEED * math.sin(math.radians(self.spinnygunangle))

            # Position the bullet
            bullet.center_x = self.player.center_x + PLAYUH_BOLLET_BAOH*math.cos(math.radians(self.spinnygunangle))
            bullet.center_y = self.player.center_y + PLAYUH_BOLLET_BAOH * math.sin(math.radians(self.spinnygunangle))

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)

            # Gunshot sound
            arcade.sound.play_sound(random.choice(self.gun_sound))

            # Create a bullet
            bullet = Bullet(r"C:\Users\WinstonBai\Downloads\Cowboytrump.png", 0.1,
                            owner="player_right")

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = self.spinnygunangle + 90

            # Give it a speed
            bullet.change_x = BULLET_SPEED * math.cos(math.radians(self.spinnygunangle + 180))
            bullet.change_y = BULLET_SPEED * math.sin(math.radians(self.spinnygunangle + 180))

            # Position the bullet
            bullet.center_x = self.player.center_x + PLAYUH_BOLLET_BAOH * math.cos(math.radians(self.spinnygunangle+180))
            bullet.center_y = self.player.center_y + PLAYUH_BOLLET_BAOH * math.sin(math.radians(self.spinnygunangle+180))

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)
    def on_update(self, delta_time):
        self.spinnygunangle+=1
        if self.spinnygunangle>=360:
            self.spinnygunangle=0
        """ Movement and game logic """
        self.frame_count += 1
        # Call update on bullet sprites
        self.bullet_list.update()
        self.explosions_list.update()
        #EVEN MORE ENEMIES
        if len(self.enemy_list)<self.last_enemy_count:
            memes=[
                r"C:\Users\WinstonBai\Downloads\Hi_Bingus.jpg",
                r"C:\Users\WinstonBai\Downloads\Bingus1_.webp",
                r"C:\Users\WinstonBai\Downloads\1557869169124.jpg",
                r"C:\Users\WinstonBai\Downloads\143123615_1036704740152192_6194344176986618483_n.png",
                r"C:\Users\WinstonBai\Downloads\Rick-Astley-Music-Video-Remastered-in-4K-Featured-image.jpg"
            ]
            for i in range(1):
                self.spawn_enemy(random.choice(memes),slace=random.uniform(0.01,0.1))
            self.last_enemy_count=len(self.enemy_list)




        if self.player_health<=0:
            self.playerbreathing = False
            self.player.remove_from_sprite_lists()

        # Loop through each bullet
        for bullet in self.bullet_list:
            smoke = Smoke(5, color=GOOFYAHHRAINBOWS[self.frame_count % len(GOOFYAHHRAINBOWS)])
            smoke.position = bullet.position
            self.explosions_list.append(smoke)
            #Homer bullet
            if bullet.owner=="enemy":
                x_distance=self.player.center_x-bullet.center_x
                y_distance=self.player.center_y-bullet.center_y
                angle = math.atan2(y_distance, x_distance)
                bullet.angle=(math.degrees(angle))
                bullet.change_x=math.cos(angle)*BULLET_SPEED
                bullet.change_y=math.sin(angle)*BULLET_SPEED
            elif bullet.owner=="player":
                if self.enemy_list:
                    x_distance = self.enemy_list[0].center_x - bullet.center_x
                    y_distance = self.enemy_list[0].center_y - bullet.center_y
                    angle = math.atan2(y_distance, x_distance)
                    bullet.angle = (math.degrees(angle))
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED
            elif bullet.owner=="player_right":
                pass


            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            epiccer_die = arcade.check_for_collision_with_list(bullet, self.player_list)




            # If it did...
            if len(hit_list) > 0 or len(epiccer_die) > 0:
                # Get rid of the bullet
                bullet.remove_from_sprite_lists()
                if len(epiccer_die) >= 0:
                    self.player_health -= 1




            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                # Make an explosion
                self.make_explosion(coin)
                self.score += 1

                # Hit Sound
                arcade.sound.play_sound(random.choices(self.hit_sound, cum_weights=(20, 30, 50), k=1)[0])

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0:
                bullet.remove_from_sprite_lists()

        # Loop through each enemy that we have
        for enemy in self.enemy_list:

            collisionmaymayday = arcade.check_for_collision(self.player, enemy)

            if collisionmaymayday:
                # Make an explosion
                self.make_explosion(enemy)
                self.score += 1
                self.make_explosion(self.player)
                self.playerbreathing=False


            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle) + 180

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 60 == 0:
                bullet = Bullet(":resources:images/space_shooter/laserBlue01.png", owner="enemy", breathing_time=1)
                bullet.center_x = start_x + ENEMY_BULLET_OFFSET*math.cos(math.radians(enemy.angle-180))
                bullet.center_y = start_y + ENEMY_BULLET_OFFSET*math.sin(math.radians(enemy.angle-180))

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.bullet_list.append(bullet)
            if self.playerbreathing == True:
                enemy.center_x -= ENEMY_SPEED
                if enemy.center_x<=0:
                    enemy.center_x = SCREEN_WIDTH

    def make_explosion(self, coin: arcade.Sprite):
        # Make an explosion
        for i in range(PARTICLE_COUNT):
            particle = Particle(self.explosions_list)
            particle.position = coin.position
            self.explosions_list.append(particle)

        smoke = Smoke(50, color=GOOFYAHHCOLORS())
        smoke.position = coin.position
        self.explosions_list.append(smoke)
        coin.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.center_window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
