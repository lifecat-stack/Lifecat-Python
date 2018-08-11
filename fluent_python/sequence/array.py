from collections import namedtuple
import bisect
import cv2

City = namedtuple('City','name country population coordinates')

tokyo = City('Tokyo','JP','39.1',(23,23))

print(tokyo)