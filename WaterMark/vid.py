import cv2
import numpy as np
import glob
import os

video = cv2.VideoCapture("video/1.mp4")
logo = cv2.imread("mylogo.png")
print("Đang thêm watermark vào Video")

h_logo, w_logo, _ = logo.shape

# Tính toán vị trí giữa của video
w_video = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h_video = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
center_y = int(h_video / 2)
center_x = int(w_video / 2)

# Tính toán vị trí logo
top_y = center_y - int(h_logo / 2)
left_x = center_x - int(w_logo / 2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo

out = cv2.VideoWriter('video_watermarked/output.mp4', cv2.VideoWriter_fourcc(
    *'mp4v'), 30, (w_video, h_video))

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Thêm watermark vào frame
    roi = frame[top_y: bottom_y, left_x: right_x]
    result = cv2.addWeighted(roi, 1, logo, 0.3, 0)
    frame[top_y: bottom_y, left_x: right_x] = result

    # Ghi frame vào video output
    out.write(frame)

out.release()

print("Đã thêm watermark vào Video")
