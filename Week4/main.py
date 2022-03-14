import utils
from Computer_Vision.ComputerVision.Week4 import edge_detector

img2 = utils.load_data()
detector = edge_detector.cannyEdgeDetector(img2, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
img = detector.detect()
utils.show_img(img, 'gray')
