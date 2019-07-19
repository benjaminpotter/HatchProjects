planets = []

class Planet:

    def __init__(self, color, size, position, speed):
        self.color = color
        self.size = size
        self.x = 0
        self.y = position
        self.rotation = 0
        self.speed = speed

def createPlanets():
    planets.append(Planet(color(112, 16, 16), 15, 60, 2))
    planets.append(Planet(color(188, 66, 66), 20, 80, 1.75))
    planets.append(Planet(color(88, 117, 188), 20, 100, 1.5))
    planets.append(Planet(color(255, 0, 0), 15, 120, 1.25))
    planets.append(Planet(color(224, 187, 132), 35, 150, 1))
    planets.append(Planet(color(255, 240, 219), 20, 180, 0.75))
    planets.append(Planet(color(66, 140, 214), 20, 200, 0.5))
    planets.append(Planet(color(67, 125, 135), 20, 220, 0.25))
    planets.append(Planet(color(136, 146, 147), 5, 230, 0.10))
createPlanets()

def drawPlanets():
    for p in planets:
        translate(200, 200)
        rotate(p.rotation)

        p.rotation += p.speed

        fill(p.color)
        ellipse(0, p.y, p.size, p.size)

        resetMatrix()

def draw():
    background(0, 0, 0)
    fill(255, 255, 0)
    ellipse(200, 200, 100, 100)
    drawPlanets()
