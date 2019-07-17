heroX = 50
heroY = 200
heroImg = getImage("space/octopus")
projectileSpeed = 3
imageMode(CENTER)
projectile = {
  “x” : “heroX”,
  “y” : “heroY”,
  “thrown” : FALSE
}
def moveHero():
  image(heroImg,heroX,heroY,80,80)
  heroY = constrain(mouseY,30,350)

def moveProjectile():
  if projectile.thrown == TRUE :
    projectile.x += projectileSpeed
  else:
    projectile.y = heroY
  ellipse(projectile.x,projectile.y+10,10,10)

def throwProjectile():
  if mousePressed :
    projectile.thrown = TRUE
  
  if projectile.x > 400 :
    projectile.x = heroX
    projectile.thrown = FALSE

def draw():
  background(0)
  moveProjectile()
  moveHero()
  throwProjectile()
