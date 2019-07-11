import sys
import cv2

from run import process

"""
main.py

 How to run:
 python main.py

"""

def main():
	dress = cv2.imread("input.png")

	h = dress.shape[0]

	w = dress.shape[1]

	dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)

	watermark = process(dress)

	watermark =  cv2.resize(watermark, (w,h), interpolation=cv2.INTER_CUBIC)

	cv2.imwrite("output.png",watermark)


	#sys.exit()

if __name__ == '__main__':
	main()
