import cv2
import numpy as np

def _get_M(w, h, f, rx=0, ry=0, rz=0, dx=0, dy=0, dz=0, sx=1, sy=1, sz=1):
    A1 = np.matrix([ [1, 0, -w/2],
                    [0, 1, -h/2],
                    [0, 0, 1],
                    [0, 0, 1]])
    S =  np.matrix([[sx, 0, 0, 0],
                    [0, sy, 0, 0],
                    [0, 0, sz, 0],
                    [0, 0, 0, 1]])
    RX = np.matrix([ [1, 0, 0, 0],
                    [0, np.cos(rx), -np.sin(rx), 0],
                    [0, np.sin(rx), np.cos(rx), 0],
                    [0, 0, 0, 1]])
    RY = np.matrix([ [np.cos(ry), 0, -np.sin(ry), 0],
                    [0, 1, 0, 0],
                    [np.sin(ry), 0, np.cos(ry), 0],
                    [0, 0, 0, 1]])
    RZ = np.matrix([ [np.cos(rz), -np.sin(rz), 0, 0],
                    [np.sin(rz), np.cos(rz), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    T = np.matrix([  [1, 0, 0, dx],
                    [0, 1, 0, dy],
                    [0, 0, 1, dz],
                    [0, 0, 0, 1]])
    A2 = np.matrix([ [f, 0, w/2, 0],
                    [0, f, h/2, 0],
                    [0, 0, 1, 0]])
    R = RX * RY * RZ
    return A2 * T * R * S * A1

def transform3d(img, rx=0, ry=0, rz=0, dx=0, dy=0, dz=0, sx=1, sy=1, sz=1):
    h, w, c = img.shape
    rx, ry, rz = np.radians([rx, ry, rz])
    d = np.sqrt(h**2 + w**2)
    f = d / (2 * np.sin(rz) if np.sin(rz) != 0 else 1)
    dz = f
    M = _get_M(w, h, f, rx, ry,rz, dx, dy, dz, sx, sy)
    return cv2.warpPerspective(img.copy(), M, (w, h))
    