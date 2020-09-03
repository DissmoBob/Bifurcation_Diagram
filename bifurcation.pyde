def pointify(coord):
    return (coord[0]/4*560+620,coord[1]/1*-675+700)

def firstGraph(r):
    fill(255)
    strokeWeight(0)
    stroke(255)
    rect(0,0,590,750)
    fill(0)
    stroke(0)
    strokeWeight(1)
    line(20,25,20,700)
    line(15,25,25,25)
    line(20,700,580,700)
    for a in range(0,9): line(560/8*a+20,720,560/8*a+20,680)
    bruh = " "*18
    textSize(10.5)
    text("0"+bruh+"4"+bruh+"8"+bruh+"12"+bruh+"16"+bruh+"20"+bruh+"24"+bruh+"28"+bruh+"32",300,733)
    text("1",10,25)
    textSize(20)
    text("f(n+1)=r*f(n)*(1-f(n)), f(0)=0.5",300,25)
    num = 0.5
    prev = 0
    for a in range(33):
        apla = [float(a)/32*560+20,num/1*-675+700]
        fill(255,230,255)
        strokeWeight(2)
        circle(apla[0],apla[1],10)
        if prev!=0:
            strokeWeight(2)
            fill(0)
            line(prev[0],prev[1],apla[0],apla[1])
        num = recursion(num, r, -1)
        prev = list(apla)
            

def recursion(num, r, time):
    if time <= 49 and time >=0: return recursion(r*num*(1-num), r, time + 1)
    elif time == -1: return r*num*(1-num)
    else: 
        #print("HI")
        ble = 0
        gob = True
        allcoords = []
        the = num
        while ble<50 and gob:
            conk = True
            for _ in allcoords:
                if abs(recursion(the, r, -1)-_[0])<=0.01:conk = False
            if conk:
                allcoords.append([r,the])
                the = recursion(the, r, -1)
            else:
                gob = False
            ble+=1
            #print(ble)
        #print(allcoords)
        return list(map(lambda x: pointify(x), allcoords))
    
def setup():
    global start, number
    number = 0
    start = False
    size(1200,750)
    background(255)
    textSize(10.5)
    fill(0)
    strokeWeight(3)
    line(600,25,600,750)
    strokeWeight(1)
    line(620,25,620,700)
    line(615,25,625,25)
    line(620,700,1180,700)
    for a in range(0,5): line(560/4*a+620,720,560/4*a+620,680)
    textAlign(CENTER)
    bruh = " "*40
    text("0"+bruh+"1"+bruh+"2"+bruh+"3"+bruh+"4",900,733)
    text("1",610,30)
    textSize(20)
    text("r",1180,675)
    textSize(20)
    text("lim   (f(n+1)=r*f(n)*(1-f(n)))",900,25)
    textSize(15)
    text("n->inf",785,40)
    line(20,25,20,700)
    line(15,25,25,25)
    line(20,700,580,700)
    textSize(20)
    text("n",580,675)
    for a in range(0,9): line(560/8*a+20,720,560/8*a+20,680)
    bruh = " "*18
    textSize(10.5)
    text("0"+bruh+"4"+bruh+"8"+bruh+"12"+bruh+"16"+bruh+"20"+bruh+"24"+bruh+"28"+bruh+"32",300,733)
    text("1",10,30)
    textSize(20)
    text("f(n+1)=r*f(n)*(1-f(n)), f(0)=0.5",300,25)
    
def draw():
    global start, number
    if start:
        if number<4:
            fill(0)
            stroke(0)
            strokeWeight(1)
            if number >= 4: number = 3.99
            firstGraph(number)
            coords = recursion(0.5, number, 0)
            #print(coords)
            for _ in coords: circle(_[0], _[1],1)
            if number <=3.2: number += 0.008
            elif number>3.2 and number<3.4: number+=0.005
            elif number>=3.4:number+=0.002
    else:
        if mousePressed: start = True
