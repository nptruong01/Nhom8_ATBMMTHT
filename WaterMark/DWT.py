import numpy as np
import cv2
import pywt  # Thư viện hỗ trợ Wavelet transforms


def DWT(coverImage, watermarkImage):
    # Đọc và đổi kích cỡ
    coverImage = cv2.resize(coverImage, (300, 300))
    cv2.imshow('ANH GOC', coverImage)
    watermarkImage = cv2. resize(watermarkImage, (150, 150))
    cv2.imshow('LOGO', watermarkImage)

    # Thực hiện DWT trên ảnh cover
    coverImage = np.float32(coverImage)
    coverImage /= 255

    coeffC = pywt.dwt2(coverImage, 'haar')
    cA, (cH, cV, cD) = coeffC

    watermarkImage = np. float32(watermarkImage)
    watermarkImage /= 255

    # Nhúng
    apha_c = 1
    apha_w = 0.3
    coeffW = (apha_c*cA + apha_w*watermarkImage, (cH, cV, cD))
    watermarkedImage = pywt.idwt2(coeffW, 'haar')
    cv2.imshow('ANH DA THEM LOGO', watermarkedImage)

    # Rút trích
    coeffWM = pywt.dwt2(watermarkedImage, 'haar')
    hA, (hH, hV, hD) = coeffWM

    extracted = (hA-apha_c*cA)/apha_w
    extracted *= 255
    extracted = np. uint8(extracted)
    cv2.imshow('LOGO SAU KHI THEM', extracted)

    # Lưu ảnh đã đóng dấu và ảnh dấu nước đã trích xuất

    cv2.imwrite('Watermark_DWT.png', watermarkedImage*255)
    cv2.imwrite('sign.png', extracted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Sử dụng hàm DWT với ảnh gốc là cover.jpg và ảnh dấu nước là logo.png
coverImage = cv2.imread('watermark/hinhnen.jpg', 0)
watermarkImage = cv2.imread('logo.png', 0)

DWT(coverImage, watermarkImage)
