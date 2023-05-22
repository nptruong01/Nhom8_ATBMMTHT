import cv2
import numpy as np
import glob
import os


logo = cv2.imread("mylogo.png")
h_logo, w_logo, _ = logo.shape

images_path = glob.glob("watermark/*.*")
print("Đang thêm watermark vào Ảnh")
for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape

    # Get the center of the original. It's the location where we will place the watermark
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)
    top_y = center_y - int(h_logo / 2)
    left_x = center_x - int(w_logo / 2)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo

    # Get ROI
    roi = img[top_y: bottom_y, left_x: right_x]

    # Add the Logo to the Roi
    result = cv2.addWeighted(roi, 1, logo, 0.3, 0)

    # Replace the ROI on the image
    img[top_y: bottom_y, left_x: right_x] = result

    # Get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite("watermarked/watermarked_" + filename, img)


print("Đã thêm watermark vào Ảnh")
