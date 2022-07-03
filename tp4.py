"""

@Este programa demuestra la búsqueda de líneas con la transformada de Hough
"""
import sys
import math
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = 'tp4-ia.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Carga una imagen
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    # Comprobar si la imagen está bien cargada
    if src is None:
        print ('¡Error al abrir la imagen!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    # Detección de bordes
    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copie los bordes a las imágenes que mostrarán los resultados en BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
     # Transformación estándar de la línea de Hough
    lines = cv.HoughLines(dst, 1, np.pi / 100, 100, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    
    cv.imshow("Fuente", src)
    cv.imshow("Líneas detectadas (en rojo) - Transformación de línea Hough estándar", cdst)
   
    
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])