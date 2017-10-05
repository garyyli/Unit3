#Gary Li
#10/5/17
#warmup10.py

from ggame import *
blue=Color(0xFF0,1)
red=Color(0xFFF000,1)

triangle1 = PolygonAsset([(0,0), (80,0), (40,40)],LineStyle(1,blue), blue)
triangle2 = PolygonAsset([(0,100), (80,-40), (40,0)],LineStyle(1,red), red)

for j in range(10):
    for i in range(10):
        Sprite(triangle1,(20+70*i,20+70*j))
        Sprite(triangle2,(20+70*i,20+70*j))
App().run()
