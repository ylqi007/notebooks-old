import cv2


img = cv2.imread('000001.jpg')
# Add rectangle
cv2.rectangle(img, (8, 12), (352, 498), (0, 255, 0), 1)
# Add text
cv2.putText(img, '(xmin, ymin) = (8, 12)', (8, 12), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 255, 0))
cv2.putText(img, '(xmin, ymax) = (8, 498)', (8, 498), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 255, 0))
cv2.imshow('image', img)
cv2.imwrite('000001.labeled.jpg', img)
cv2.waitKey(0)
