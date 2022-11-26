import pygame, time, random, math

from objects import Circle

pygame.init()
pygame.font.init()
SHEIGHT = 650
SWIDTH = 700
background_color = (114, 120, 114)
fps_tick = 60
window = pygame.display.set_mode((SWIDTH, SHEIGHT))
pygame.display.set_caption('Collision')

light_blue = (137, 178, 243)
light_orange =(169, 61, 118)
masses = []


ball1 = Circle(40,40,10,light_blue, [30,30])
masses.append(ball1)



class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        self.text = self.font.render(str(self.clock.get_fps()), True,  (255,255,255))


    def render(self, window):
        self.text = self.font.render('FPS:' + str(round(self.clock.get_fps(),None)), True, (255,255,255))
        window.blit(self.text, (SWIDTH - (SWIDTH * .1),10))

fps = FPS()

def draw(time):
    window.fill(background_color)
    fps.render(window)


    fps.clock.tick(fps_tick)

    for ball in masses:
        ball.draw(window)

        

    for ball in masses:
        ball.update(SHEIGHT, SWIDTH, time)


    for i in range(len(masses)):
        first = masses[i]
        for j in range(i+1, len(masses) ):
            if first.collision(masses[j]):
                first.collision_resulation(masses[j])


    pygame.display.update()




def main():
    last_time = time.time()
    running = True
    while running:
        now = time.time()
        dtime = now - last_time

        last_time = now
        draw(dtime)

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                new_particle = Circle(pos[0],pos[1],random.randint(10, 60),(random.randint(1, 250), random.randint(1, 250), random.randint(1, 255)), [random.randint(-5, 5),random.randint(-5, 5)])
                masses.append(new_particle)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    masses.pop()
        

main()