x = 0
y = 60
z = 0


iv = (x)
tspor = int(input("Input Time (in seconds)"))
accel = (int(input("Input Acceleration (m/s2)")))
dst = int(input("Input Distance"))
sl = (y)
c = "*"



for i in range (0,tspor):
    s = (dst * i+ 0.5*accel*(i)**2)
    v = (s/10)
    print("Duration: ", i, " Distance: ", ("*"*int(v)))