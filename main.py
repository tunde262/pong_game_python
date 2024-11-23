import pygame, sys
import asyncio  # Import asyncio for asynchronous execution, useful for web hosting environments.

# Ball class handles the behavior and movement of the game ball.
class Ball:
    def __init__(self, screen, color, posX, posY,radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0  # Horizontal speed
        self.dy = 0  # Vertical speed

        self.show()  # Draw the ball initially

    def show(self):
        # Draw the ball on the screen.
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius)

    def start_moving(self):
        # Start the ball's movement.
        self.dx = 10
        self.dy = 5

    def move(self):
        # Update the ball's position.
        self.posX += self.dx
        self.posY += self.dy

    def paddle_collision(self):
        # Reverse the ball's horizontal direction upon hitting a paddle.
        self.dx = -self.dx

    def wall_collision(self):
        # Reverse the ball's vertical direction upon hitting a wall.
        self.dy = -self.dy

    def restart_pos(self):
        # Reset the ball to its initial position and stop its movement.
        self.posX = WIDTH // 2
        self.posY = HEIGHT // 2
        self.dx = 0
        self.dy = 0
        self.show()

# Paddle class handles the behavior of player paddles.
class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'  # Paddle's movement state ('up', 'down', or 'stopped')
        self.show()

    def show(self):
        # Draw the paddle on the screen.
        pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height ) )

    def move(self):
        # Update the paddle's position based on its state.
        if self.state == 'up':
            self.posY -= 10
        elif self.state == 'down':
            self.posY += 10
    
    def clamp(self):
        # Prevent the paddle from moving beyond the screen boundaries.
        if self.posY <= 0:
            self.posY = 0

        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height

    def restart_pos(self):
        # Reset the paddle to its initial position.
        self.posY = HEIGHT // 2 - self.height // 2
        self.state = 'stopped'
        self.show()

# Score class manages the display and tracking of the player's scores.
class Score:
    def __init__(self, screen, points, posX, posY):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.font = pygame.font.SysFont("monospace", 80, bold=True) # Font for score display
        self.label = self.font.render( self.points, 0, WHITE )
        self.show()

    def show(self):
        # Draw the score on the screen.
        self.screen.blit( self.label, ( self.posX - self.label.get_rect().width // 2, self.posY ) )

    def increase(self):
        # Increase the score by 1.
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render( self.points, 0, WHITE )
    
    def restart(self):
        # Reset the score to 0.
        self.points = '0'
        self.label = self.font.render( self.points, 0, WHITE )

# CollisionManager class checks for collisions between game objects.
class CollisionManager:
    def between_ball_and_paddle1(self, ball, paddle1):
        # Check if the ball collides with paddle1.
        if ball.posY + ball.radius > paddle1.posY and ball.posY - ball.radius < paddle1.posY + paddle1.height:
            if ball.posX - ball.radius <= paddle1.posX + paddle1.width:
                return True
        
        return False
    
    def between_ball_and_paddle2(self, ball, paddle2):
        # Check if the ball collides with paddle2.
        if ball.posY + ball.radius > paddle2.posY and ball.posY - ball.radius < paddle2.posY + paddle2.height:
             if ball.posX + ball.radius >= paddle2.posX:
                return True
        
        return False

    def between_ball_and_walls(self, ball):
        # Check if the ball collides with the top or bottom walls.

        # top collison
        if ball.posY - ball.radius <= 0:
            return True

        # bottom collison
        if ball.posY + ball.radius >= HEIGHT:
            return True
        
        return False

    def check_goal_player1(self, ball):
        # Check if player1 scores a goal.
        return ball.posX - ball.radius >= WIDTH

    def check_goal_player2(self, ball):
        # Check if player2 scores a goal.
        return ball.posX + ball.radius <= 0

# Game setup
pygame.init()

WIDTH = 900     # Screen width
HEIGHT = 500    # Screen height
BLACK = (0, 0, 0)   # Background color
WHITE = (255, 255, 255) # Object color

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )   # Initialize the screen
pygame.display.set_caption( 'PONG' )    # Set the game title

def paint_back():
    # Draw the background and the center line.
    screen.fill( BLACK )
    pygame.draw.line( screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5 )

def restart():
    # Reset the game to its initial state.
    paint_back()
    score1.restart()
    score2.restart()
    ball.restart_pos()
    paddle1.restart_pos()
    paddle2.restart_pos()

paint_back()

# Create game objects
ball = Ball( screen, WHITE, WIDTH // 2, HEIGHT // 2, 15 )
paddle1 = Paddle( screen, WHITE, 15, HEIGHT // 2 - 60, 20, 120 )
paddle2 = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT // 2 - 60, 20, 120 )
collision = CollisionManager()
score1 = Score( screen, '0', WIDTH // 4, 15 )
score2 = Score( screen, '0', WIDTH - WIDTH // 4, 15 )

# VARIABLES
playing = False # Game state

clock = pygame.time.Clock()  # Will be used to Set frame rate

# Main game loop with asynchronous execution.
async def main(): # Remove 'async' function to run regular python version - for web hosting purposes
    global playing
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # -- Handle keypress events --
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    ball.start_moving()
                    playing = True

                if event.key == pygame.K_r:
                    restart()
                    playing = False
                
                if event.key == pygame.K_w:
                    paddle1.state = 'up'
                
                if event.key == pygame.K_s:
                    paddle1.state = 'down'
                
                if event.key == pygame.K_UP:
                    paddle2.state = 'up'

                if event.key == pygame.K_DOWN:
                    paddle2.state = 'down'

            # Stop paddle movement when keys are released
            if event.type == pygame.KEYUP:
                paddle1.state = 'stopped'
                paddle2.state = 'stopped'

        if playing:
            paint_back()    # Clear and redraw background
            
            # Update and draw the ball
            ball.move()
            ball.show()

            # Update and draw paddle1
            paddle1.show()
            paddle1.clamp()
            paddle1.move()

            # Update and draw paddle2
            paddle2.show()
            paddle2.clamp()
            paddle2.move()

            # check for collisons
            if collision.between_ball_and_paddle1(ball, paddle1):
                ball.paddle_collision()

            if collision.between_ball_and_paddle2(ball, paddle2):
                ball.paddle_collision()

            if collision.between_ball_and_walls(ball):
                ball.wall_collision()
            
            # Check scoring conditions
            if collision.check_goal_player1(ball):
                paint_back()
                score1.increase()
                ball.restart_pos()
                paddle1.restart_pos()
                paddle2.restart_pos()
                playing = False
            
            if collision.check_goal_player2(ball):
                paint_back()
                score2.increase()
                ball.restart_pos()
                paddle1.restart_pos()
                paddle2.restart_pos()
                playing = False
        
        # Draw scores
        score1.show()
        score2.show()

        pygame.display.update() # Update the display

        clock.tick(60)  # Set frame rate to 60 frames per second

        # -- for web hosting purposes --
        await asyncio.sleep(0) # Remove this to run regular python version

# Run the game loop asynchronously - for web hosting purposes
asyncio.run(main()) # Remove this to run regular python version

# uncomment this to run regular python version

# main()