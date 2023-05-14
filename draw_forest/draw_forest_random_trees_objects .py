#####################################FUENTES###########################################################
## https://www.youtube.com/watch?v=-LsuiVGO-88                                                       ##
## Draw a Forest of Random Tree Objects with Python OpenCV - Classes and OOP Practice for Beginners  ##
## https://github.com/MariyaSha/OpenCV_DrawImages/blob/main/completeCode_OpenCVForest.ipynb          ##
#######################################################################################################
# class X():
#     class_attribute_1 = 0
#     class_attritube_2 = 0
#     class_attritube_3 = 0
    
#     def __init__(self, instance_attribute_1, instance_attribute_2): #constructor
#         self.instance_attribute_1 = instance_attribute_1
#         self.instance_attribute_2 = instance_attribute_2
        
#     def metodo(self):
#         print("...")
        
#     def __str__(self): #representacion, ejemplo: tipo de objeto
#         return f"The values are: {self.instance_attribute_1}"
#         self.instance_attribute_2 = instance_attribute_2
    
#     def __len__(self): #representacion, ejemplo: tipo de objeto
#         return len(self.instance_attribute_1)
    
#     def __getitem__(self, pos):
#         return self.instance_attribute_1[pos]    
    
#     def __setitem__(self, pos, value):
#         self.instance_attribute_1[pos] = value
        
#     def __iter__(self):
#         for pos in range(0, len(self.instance_attribute_1)):
#             yield f"Value[{pos}]: {self.instance_attribute_1[pos]}"
    
        
#     def metodo(self):
#         print("...")
            

# x67i = X([5, 12], 0)
# print(x67i)
# len(x67i)
# for vec in x67i:
#     print(vec)
######################################################################################################
######################################################################################################
import numpy as np
import cv2 as cv
import random

######################
##general parameters##
######################
width = 900
height = 600
n_trees = 30
ground_level = height -100

###############
##blank image##
###############
bg = np.zeros((height, width, 3), dtype = np.uint8)

############
##draw sky##
############
cv.rectangle(bg, (width, 0), (0, ground_level), (225, 225, 95), -1)

################
class Tree(object):
    def __init__(self, image):
        self.img = image
        self.loc =int(np.random.choice(range(900), 1))
        self.ht = int(np.random.choice(range(200, 350), 1))
        self.radius = 50
        self.scale = np.random.choice(np.linspace(0.5, 2.5, num=8), 1)
        
    ###########
    ##colours##
    ###########    
    def generate_colours(self):
        green = (0, random.randint(130, 200), 0)
        light_green = (35, random.randint(200, 250), 35)
        brown = random.choice([(2, 30, 85), (5, 55, 120), (0, 70, 140)])
        return green, light_green, brown
        
    def draw(self):
        small_radius = int(self.radius*self.scale-20*self.scale)
        green, light_green, brown = self.generate_colours()
        #leafs=> cv.circle(image, center_coordinates, radius, color, thickness)
        cv.circle(self.img, (self.loc, ground_level-self.ht), int(self.radius*self.scale), green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale), ground_level-self.ht + small_radius), small_radius, green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level-self.ht + small_radius), small_radius, green, -1)
        #trunk=> cv.line(image, start_point, end_point, color, thickness) 
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.ht), brown, int(20*self.scale))
        cv.line(self.img, (self.loc, ground_level-self.ht + int(75*self.scale)), (self.loc-int(45*self.scale), ground_level-self.ht + small_radius), brown, int(5*self.scale))
        cv.line(self.img, (self.loc, ground_level-self.ht + int(75*self.scale)), (self.loc+int(45*self.scale), ground_level-self.ht + small_radius), brown, int(5*self.scale))
        #leafs-shadows
        cv.circle(self.img, (self.loc, ground_level-self.ht), int(self.radius*self.scale-10*self.scale), light_green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale), ground_level-self.ht + small_radius), small_radius-int(10*self.scale), light_green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level-self.ht + small_radius), small_radius-int(10*self.scale), light_green, -1)
        ###############
        ##draw ground##
        ###############
        cv.rectangle(bg, (width, ground_level), (0, height), (70, 180, 75), -1)
        return self.img
################  




      
    

#################
##display image##
#################
for i in range(n_trees):
    img = Tree(bg).draw()

##############################
##show in individual windows##
##############################
cv.imshow('forest of objects', bg)
cv.waitKey(0)
cv.destroyAllWindows()













