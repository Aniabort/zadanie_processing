def setup():
    size(400, 400)
    textSize(100)
    textAlign(CENTER)
    fill(100)
    background(150,15,105)
def draw():
    
    if mousePressed:
        text("A", width/2-75, height/2)
        text("B", width/2+75, height/2)
   
    
    if (mouseX >= 90 and mouseX <= 163 and mouseY >= 113 and mouseY <= 200):
        fill(100, 255, 0)
        text("A", width/2-75, height/2)
        fill(250)
        
    if (mouseX >= 237 and mouseX <= 311 and mouseY >= 113 and mouseY <= 200):
        fill(300, 80, 0)
        text("B", width/2+75, height/2)
        fill(250)
        
        
 
    if keyPressed:
        if key == "a" or key == "A":
            text("A", width/2-75, height/2)
            fill(405, 600, 0)
                
        if key == "b" or key == "B":
            text("B", width/2+75, height/2)
            fill(255, 150, 210)


        if keyCode == 39:
            text("B", width/2+75, height/2)
            fill(255, 0, 0)

        
        if keyCode == 37: 
            text("B", width/2+75, height/2)
            fill(255, 0, 0)
    


        
    s = createShape()
    s.beginShape()
    s.fill(405,600,55)
    s.noStroke()
    s.vertex(3, (height/5)*4+10)
    s.vertex(width/2-10, (height/3)*3+10)
    s.vertex(width/5, (height/5)*4+20)
    s.vertex(width, (height/7)*3)
    s.endShape(CLOSE)
    shape(s,25,25)
