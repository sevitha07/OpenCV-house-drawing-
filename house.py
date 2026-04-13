import cv2
import numpy as np

# A blank white image
img = np.ones((500, 700, 3), dtype=np.uint8) * 255

# House body
cv2.rectangle(img, (200, 200), (500, 400), (0, 0, 0), 2)

# Roof
# Roof fill
roof_points = np.array([[200, 200], [350, 100], [500, 200]], np.int32)
cv2.fillPoly(img, [roof_points], (0, 0, 255))
# Roof outline
cv2.line(img, (200, 200), (350, 100), (0, 0, 0), 2)
cv2.line(img, (350, 100), (500, 200), (0, 0, 0), 2)

# Door
cv2.rectangle(img, (320, 300), (380, 400), (0, 0, 0), 2)

# Door knob
cv2.circle(img, (370, 350), 5, (255, 0, 0), -1)

# Left window
cv2.rectangle(img, (240, 250), (300, 310), (255, 0, 0), 2)
cv2.line(img, (270, 250), (270, 310), (255, 0, 0), 2)
cv2.line(img, (240, 280), (300, 280), (255, 0, 0), 2)

# Right window
cv2.rectangle(img, (400, 250), (460, 310), (255, 0, 0), 2)
cv2.line(img, (430, 250), (430, 310), (255, 0, 0), 2)
cv2.line(img, (400, 280), (460, 280), (255, 0, 0), 2)

# Chimney
cv2.rectangle(img, (420, 120), (460, 180), (0, 0, 0), -1)

# Sun
cv2.circle(img, (100, 100), 40, (0, 255, 255), -1)

# Green land
cv2.rectangle(img, (0, 400), (700, 500), (0, 255, 0), -1)

# Tree on the left side
# Tree trunk
cv2.rectangle(img, (80, 280), (110, 400), (19, 69, 139), -1)

# Tree leaves
cv2.circle(img, (95, 240), 50, (0, 150, 0), -1)
cv2.circle(img, (60, 260), 40, (0, 180, 0), -1)
cv2.circle(img, (130, 260), 40, (0, 180, 0), -1)

# Tree on the right side
# tree trunk
cv2.rectangle(img, (590, 280), (620, 400), (19, 69, 139), -1)

# tree leaves
cv2.circle(img, (605, 240), 50, (0, 150, 0), -1)
cv2.circle(img, (570, 260), 40, (0, 180, 0), -1)
cv2.circle(img, (640, 260), 40, (0, 180, 0), -1)

# Center cloud
cv2.circle(img, (300, 60), 25, (255, 200, 100), -1)
cv2.circle(img, (330, 50), 30, (255, 200, 100), -1)
cv2.circle(img, (360, 60), 25, (255, 200, 100), -1)

# Right-end cloud
cv2.circle(img, (600, 90), 25, (255, 200, 100), -1)
cv2.circle(img, (630, 80), 30, (255, 200, 100), -1)
cv2.circle(img, (660, 90), 25, (255, 200, 100), -1)

# Show image
cv2.imshow("House Drawing", img)

cv2.waitKey(0)
cv2.destroyAllWindows()