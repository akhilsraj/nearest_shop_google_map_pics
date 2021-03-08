import cv2
import argparse
import numpy as np
import collections

img = cv2.imread(r'C:\Users\Akhil S R\Downloads\Images_new\Images\tmp_3.png')
dim = img.shape
def nearest_shop(img,anchor_point_x,anchor_point_y):
    shop = [255,251,240]
    road = [255,255,255]
    building = [241,243,244]
    park = [197,232,197]
    flag_road = 1
    flag_shop  = 1
    flag_building = 1
    flag_park = 1
    global shop_x,shop_y,road_x,road_y,building_x,building_y,park_x,park_y 
    for x, y in [(0,0),(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]: # directions    
        for i in range(0,dim[0]):
            for j in range(0,dim[1]):
                if((anchor_point_x + i*x < 500) and (anchor_point_y + j*y < 640)):
                    rgb = img[anchor_point_x + i*x][anchor_point_y + j*y]
                    if((rgb == road).all() and flag_road == 1):
                        road_x,road_y = anchor_point_x + i*x,anchor_point_y + j*y
                        flag_road = 0
                    elif(collections.Counter(rgb) == collections.Counter(shop) and flag_shop == 1):
                        shop_x,shop_y = anchor_point_x + i*x,anchor_point_y + j*y
                        flag_shop = 0
                    elif(collections.Counter(rgb) == collections.Counter(building) and flag_building == 1):
                        building_x,building_y = anchor_point_x + i*x,anchor_point_y + j*y
                        flag_building = 0
                    elif(collections.Counter(rgb) == collections.Counter(park) and flag_park == 1):
                        park_x,park_y = anchor_point_x + i*x,anchor_point_y + j*y
                        flag_park = 0
    distance_version_2(flag_road,flag_shop,flag_building,flag_park)
def distance_version_2(flag_road,flag_shop,flag_building,flag_park):
    if(flag_shop == 1):
        print("Shop isnt in the picture")
    else:
        shop = np.array((int(shop_x),int(shop_y)))
    if(flag_building == 1):
        print("Building isnt in the picture")
    else:
        building = np.array((int(building_x),int(building_y)))
    if(flag_road == 1):
        print("Road isnt in the picture")
    else:
        road = np.array((int(road_x),int(road_y)))
    if(flag_park == 1):
        print("Park isnt in the picture")
    else:
        park = np.array((int(park_x),int(park_y)))
    try:
        print("Road",np.linalg.norm(shop - road))
    except:
        print("An exception occurred probably road or shop isnt there in the picture")
    try:
        print("Building",np.linalg.norm(shop - building))
    except:
        print("An exception occurred probably building or shop isnt there in the picture")    
    try:
        print("Park",np.linalg.norm(shop - park))
    except:
        print("An exception occurred probably park or shop isnt there in the picture")

nearest_shop(img,340,250)

