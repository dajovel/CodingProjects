#distance = devided (X2 - X1)Squared + (Y1 + Y1)Squared
#d	=	distance
#(x_1, y_1)	=	coordinates of the first point
#(x_2, y_2)	=	coordinates of the second point
#slope = y2 - y1 / x2-x1
# m	=	slope
# (x_1, y_1)	=	coordinates of first point in the line
# (x_2, y_2)	=	coordinates of second point in the line
#Homework
#Given 2 quardinates in form of a tuple
#Line object and cylinder class

class Line:
    
    def __init__(self, coor1,coor2):
        '''taking cordinates in as tuples. This way we will take cordinates in as attributes. Later we will use tuple unpacking to grab individual components of tese tuples'''
        
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
    
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)


coordinate1 = (3,2)
coordinate2 = (8,10)

myline = Line(coordinate1,coordinate2)

print(myline.distance())
print(myline.slope())

class Cylinder:
    '''We are going to get the math of a cylinder. This 
    will allow for math to auto be done for height and radius of the Cylinder requested'''

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius
    
    def volume(self):
        '''Volume for a cylinder is height * 3.14(pi)'''

        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):
        
        top = 3.14 * (self.radius**2)

        return (2*top) + (2*3.14*self.radius*self.height)
        

mycyl = Cylinder(2,3)
print(mycyl.height)
print(mycyl.radius)
print(mycyl.volume())
print(mycyl.surface_area())
 