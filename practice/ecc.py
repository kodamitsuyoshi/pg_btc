from unittest import TestCase   

from fieldelement import FPrime
from point import daenPoint,daenPointI
class ECCTest(TestCase):
    def test_on_curve(self):
        prime =223
        FP =FPrime(prime)
        a, b = FP(0) ,FP(7)
        DPoint = daenPoint(a,b)
        valid_points = ((192,105),(17,56),(1,193))
        invalid_points = ((200,119),(42,99))

        for _x ,_y in valid_points:
            x,y = FP(_x) ,FP(_y)
            DPoint(x,y)

        for _x ,_y in invalid_points:
            x,y = FP(_x) ,FP(_y)
            with self.assertRaises(ValueError):
                DPoint(x,y)

    def add_test(self):
        add_list =(  ( (170,142), (60,139) ,(220,181)) , ((47,71),(17,56),(215,68) ) ,((143,98),(76,66),(47,71))  )
        FP = FPrime(223)
        a,b = FP(0),FP(7)
        DPoint = daenPoint(a,b)
        for i in add_list:
            v1,v2,v3 = i
            x1 ,y1 = FP(v1[0]), FP(v1[1])
            x2 ,y2 = FP(v2[0]), FP(v2[1])
            x3 ,y3 = FP(v3[0]), FP(v3[1])
            P1 = DPoint(x1,y1)
            P2 = DPoint(x2,y2)
            P3 = DPoint(x3,y3)
            #x,y = FP(_x),FP(_y)
            self.assertEqual(P1+P2,P3)



 