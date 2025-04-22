from matplotlib import pyplot

plot = pyplot.plot
axis = pyplot.axis
subplot = pyplot.subplot
title = pyplot.title
show = pyplot.show

dt = 0.01

#pt vna-der-pol

def init_vars():
    global x, y, xres, yres
    x = y = 0.1
    xres = [x]
    yres = [y]

def observe():
    global x,y, xres, yres
    xres.append(x)
    yres.append(y)

def update():
    global x,y, xres, yres

    nextx = x + y * dt
    nexty = y + (-r * (x**2 -1) * y -x ) * dt
    x,y = nextx, nexty

def plot_phase_space():
    init_vars()
    for t in range(10000):
        update()
        observe()

    plot(xres, yres)
    axis('image')
    axis([-3,3,-3,3])
    title('r = ' + str(r))

rs = [-1, -0.1, 0, .1, 1] 
for i in range(len(rs)):
    subplot(1,len(rs), i+1)
    r = rs[i]
    plot_phase_space()
show()

