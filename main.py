import cv2

#configurable parameters

source="h.jpg"
destination="newimg.png"
scale_percent = 50
image = cv2.imread(source,cv2.IMREAD_UNCHANGED)

#calculates 50 percent of the dimensions
new_width=int(image.shape[1] * scale_percent / 100)
new_height=int(image.shape[0] * scale_percent / 100)

#resized iamge

output = cv2.resize(image,(new_width,new_height))


cv2.imwrite(destination , output)
cv2.waitKey(0)