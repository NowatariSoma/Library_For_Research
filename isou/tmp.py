import numpy as np
import cv2

def ripoc(a, b, m = None):
    g_a = np.asarray(cv2.cvtColor(a, cv2.COLOR_BGR2GRAY), 'float')
    g_b = np.asarray(cv2.cvtColor(b, cv2.COLOR_BGR2GRAY), 'float')

    h, w = g_a.shape
    hy = np.hanning(h)
    hx = np.hanning(w)
    hw = hy.reshape(h, 1)*hx
    
    f_a = np.fft.fftshift(np.log(np.abs(np.fft.fft2(g_a*hw))))
    f_b = np.fft.fftshift(np.log(np.abs(np.fft.fft2(g_b*hw))))

    if not m:
        l = np.sqrt(w*w + h*h)
        m = l/np.log(l)

    center = (w/2, h/2)
    flags = cv2.INTER_LANCZOS4 + cv2.WARP_POLAR_LOG
    p_a = cv2.warpPolar(f_a, (w, h), center, m, flags)
    p_b = cv2.warpPolar(f_b, (w, h), center, m, flags)
    (x, y), e = cv2.phaseCorrelate(p_a, p_b, hw)

    angle = y*360/h
    scale = (np.e)**(x/m)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    t_b = cv2.warpAffine((g_b), M, (w, h))
    (x, y), e = cv2.phaseCorrelate(g_a, t_b)

    return x, y, angle, scale

img1 = cv2.imread("/home/nowatari/repos/isou/mandrill.png")
img2 = cv2.imread("/home/nowatari/repos/isou/mandrill-s.png")

x, y, angle, scale = ripoc(img1, img2)
print(x, y, angle, scale)

h, w, ch = img1.shape
M = cv2.getRotationMatrix2D((w/2,h/2), angle, scale)
M[0][2] -= x
M[1][2] -= y

dst = cv2.warpAffine(img2, M, (w, h))
cv2.imwrite("/home/nowatari/repos/isou/mandrill-t.png", dst)