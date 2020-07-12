# -*- coding:utf-8 -*-
# @Description: numpy introduction
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import numpy
import cv2

n = numpy.arange(27)
print(n)  # arrray([ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26])
print(type(n))  # <class 'numpy.ndarray'>
new1 = n.reshape(3, 9)
print(new1)
"""
we get two dimensional array
[[ 0  1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16 17]
 [18 19 20 21 22 23 24 25 26]]
"""
new2 = n.reshape(3, 3, 3)
print(new2)
"""
three dimensional array
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]

"""
# read image file
im_g = cv2.imread("file/smallgray.png", 0)
print(im_g)
"""
type: uint8
255 represents white
0 represents black
[[187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]]
"""
print(type(im_g))  # <class 'numpy.ndarray'>
im_g2 = cv2.imread("file/smallgray.png", 1)
print(im_g2)
"""
[[[187 187 187]
  [158 158 158]
  [104 104 104]
  [121 121 121]
  [143 143 143]]    (blue layer)

 [[198 198 198]
  [125 125 125]
  [255 255 255]
  [255 255 255]
  [147 147 147]]    (green layer)

 [[209 209 209]
  [134 134 134]
  [255 255 255]
  [ 97  97  97]
  [182 182 182]]]    (red layer)
"""
# create new image file(same image)
cv2.imwrite("file/newsmallgray.png", im_g)

# indexing, slicing, and iterating numpy arrays
sliced = im_g[0:2, 1:4]
print(sliced)
"""
[[158 104 121]
 [125 255 255]]
"""
print(im_g[2, 4])  # 182
for i in im_g:
    print(i)
"""
[187 158 104 121 143]
[198 125 255 255 147]
[209 134 255  97 182]
"""
for i in im_g.T:
    print(i)
"""
[187 198 209]
[158 125 134]
[104 255 255]
[121 255  97]
[143 147 182]

"""
for i in im_g.flat:
    print(i)
"""
187
158
104
121
143
198
125
255
255
147
209
134
255
97
182
"""
# stacking anf splitting numpy arrays
ims = numpy.hstack((im_g, im_g))
print(ims)      # horizontally stack
"""
[[187 158 104 121 143 187 158 104 121 143]
 [198 125 255 255 147 198 125 255 255 147]
 [209 134 255  97 182 209 134 255  97 182]]
"""
ims2 = numpy.vstack((im_g, im_g))
print(ims2)   # vertically stack
"""
[[187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]
 [187 158 104 121 143]
 [198 125 255 255 147]
 [209 134 255  97 182]]
"""
lst = numpy.vsplit(ims2, 3)
print(lst)
"""
[array([[187, 158, 104, 121, 143], [198, 125, 255, 255, 147]], dtype=uint8), 
array([[209, 134, 255,  97, 182], [187, 158, 104, 121, 143]], dtype=uint8), 
array([[198, 125, 255, 255, 147], [209, 134, 255,  97, 182]], dtype=uint8)]
"""