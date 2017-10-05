#Gary Li
#10/5/17
#warmup10.py

from ggame import *
blue=Color(0xFF0,1)

triangle1 = PolygonAsset([(0,0), (120,180), (60,300)],LineStyle(1,blue), blue)

for j in range(10):
    for i in range(10):
        Sprite(triangle1,(20+50*i,20+50*j))
App().run()
