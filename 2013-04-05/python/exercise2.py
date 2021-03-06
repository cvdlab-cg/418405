from pyplasm import *

GRID = COMP([INSR(PROD),AA(QUOTE)])

#floor0

square01 = GRID([[0.5+2.2+0.5],[-0.5-9.1,0.5+1.8+0.5],[0.14]])
square02 = GRID([[-0.5-2.2,0.5+2+0.5+4.7+0.5+4.7+0.5],[-0.5-3.6,1.7+1.5+0.5+1.8+0.5+1.8+0.5],[0.14]])
square03 = GRID([[-0.5-2.2-0.5-2-0.5-4.7-0.5-4.7-0.5,0.6],[-0.5-3.6-1.7,1.5],[0.14]])
square04 = GRID([[-0.5-2.2-0.5-2-0.5-4.7-0.5-4.7-0.5,1.9],[-0.5-3.6-1.7-1.5,0.5+1.8+0.5+1.8+0.5],[0.14]])
square05 = GRID([[-0.5-2.2,0.5+1.2+0.5],[-0.5-3.6+0.7,0.7],[0.14]])

cyl01 = T([1,2])([0.5+2.2+0.5+2+0.5+4.7+0.5+4.7+0.5+1.9,-2.55+0.5+9.1+0.5+1.8+0.5])(CYLINDER([2.55,0.14])(36))
cyl02 = T([1,2])([-1.1+0.5+2.2+0.5+1.2+0.5,0.5+3.6-0.7])(CYLINDER([1.1,0.14])(36))




floor0 = STRUCT([square01,square02,square03,square04,square05,cyl01,cyl02])

#floor1

square11 = GRID([[0.25,-0.25-0.9,1.3+0.5+2+((0.5+4.7)*3)+0.5],[-0.5,9.1],[0.14]])
square12 = GRID([[0.5+1.7+0.5+0.5+2+0.5,-4.7-0.5-0.5,4.2+0.5+4.7+0.5],[-0.5-9.1-0.25-0.25,1.8],[0.14]])
square13 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.25-0.25-1.8,+0.5],[0.14]])
square14 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1,0.5],[0.14]])
square15 = GRID([[((0.5+4.7)*4)+0.5],[0.5],[0.14]])

balcony = T([1,2,3])([-2.2,0.5+9.1+0.3,0.04])(CUBOID([2.2,2,0.1]))

floor1 = T([3])([2.36+0.14])(STRUCT([square11,square12,square13,balcony,square14,square15]))

#floor2

square21 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.5-1.8,0.5],[0.14]])
square22 = GRID([[0.5,-2.2-0.5-2-0.5-3.3,1.4+0.5+4.7+0.5+4.7+0.5],[-0.5-9.1-0.25,0.25+1.8],[0.14]])
square23 = GRID([[0.5+0.9+0.25,-1.05-0.5-2,0.5],[-0.5-9.1,0.25],[0.14]])
square24 = GRID([[0.5,-0.9,1.3+0.5+2+0.5+4.7+0.5+4.7+0.5+4.7+0.5],[-0.5-9.1-0.25,0.25],[0.14]])
pol = MKPOL([[[10.4,0.5],[10.4+0.5+4.7+0.5+4.7+0.5,0.5],[10.4+0.5+4.7+0.5+4.7+0.5,0.5+9.1+0.25],[10.4-1.9,0.5+9.1+0.25]],[[1,2,3,4]],None])
square25 = PROD([pol,Q(0.14)])
square26 = GRID([[((0.5+4.7)*4)+0.5],[+0.5],[0.14]])
square27 = GRID([[0.25],[-0.5,9.1],[0.14]])

floor2 = T([3])([(2.36+0.14)*2])(STRUCT([square21,square22,square23,square24,square25,square26,square27]))

#floor3

square31 = GRID([[((0.5+4.7)*4)+0.5],[0.5+9.1+0.25+0.25],[0.14]])
square32 = GRID([[0.5+1.7+0.5+0.5+2+0.5+4.7+0.5,-4.7-0.5-0.5,+4.2+0.5],[-0.5-9.1-0.25,0.25+1.8],[0.14]])
square33 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.25-0.25-1.8,+0.5],[0.14]])

floor3 = T([3])([(2.36+0.14)*3])(STRUCT([square31,square32,square33]))

#floor4

square41 = GRID([[((0.5+4.7)*4)+0.5],[0.25],[0.14]])
square42 = GRID([[0.25,-0.25-4.7-0.5-4.7,((0.5+4.7)*2)+0.5],[-0.25,0.25+9.1],[0.14]])
square43 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1,0.5+1.8+0.5],[0.14]])

floor4 = T([3])([(2.36+0.14)*4])(STRUCT([square41,square42,square43]))

floors = STRUCT([floor0,floor1,floor2,floor3,floor4])

building = STRUCT([pillars,floors])