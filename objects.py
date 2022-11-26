import pygame, math, uuid



class Circle:
    def __init__(self, x,y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.colors = color
        self.mass = radius * 1.5

        self.id = uuid.uuid4()

        # self.velocity = [random.randint(-10, 10), random.randint(-10, 10)	]
        self.velocity = [speed[0],speed[1]]
        self.accleration = [0,0]
        

    def draw(self, window):
        pygame.draw.circle(window, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius-1)
   

    def update(self, window_height, window_width, time):
        # if you want to add accleration
        self.velocity[1] += self.accleration[1]*time*60
        self.velocity[0] += self.accleration[0]*time*60

        self.y += self.velocity[1]*time*20
        self.x += self.velocity[0]*time*20

        # down
        if self.radius + self.y >= window_height:
            self.velocity[1] *= -1

            self.y = window_height - self.radius

        # up
        if self.radius >= self.y:
            self.velocity[1] *= -1

            self.y = 0 + self.radius

        # left
        if self.x - self.radius <= 0:
            self.velocity[0] *= -1
            
            self.x = self.radius

        #right       
        if window_width <= self.radius + self.x:
            self.velocity[0] *= -1
            self.x = window_width - self.radius

    def get_info(self):

        info = [[self.x, self.y], self.velocity, self.accleration, self.mass, self.radius, self.id]

        return info



    def collision_resulation(self, i):        
        mass = self.mass - i.mass
        bottom = self.mass + i.mass

        topx = self.velocity[0]*(mass) + 2*((i.mass) * (i.velocity[0]))
        topy = self.velocity[1]*(mass) + 2*((i.mass) * (i.velocity[1]))


        smass = i.mass - self.mass

        stopx = (i.velocity[0] * smass) + (2*self.mass * self.velocity[0])
        stopy = (i.velocity[1] * smass) + (2*self.mass * self.velocity[1])

        self.velocity = ([topx/bottom,topy/bottom])

        i.velocity = ([stopx/bottom, stopy/bottom])


    def collision(self, other_info):
        if self.id != other_info.id:
            distX = self.x  - other_info.x
            distY = self.y - other_info.y

            distance = math.sqrt((distX*distX) + (distY*distY))
            if distance <= self.radius + other_info.radius:

                return True
            else:

                return False


