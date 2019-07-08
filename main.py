import sys
import cv2

from run import process

"""
main.py

 How to run:
 python3 main.py

"""

def main2():
	dress = cv2.imread("input.png")

	watermark = process(dress)

	cv2.imwrite("output.png",watermark)


# ------------------------------------------------- main()
def main(i):

	#Read input image
	dress = cv2.imread("j"+str(i)+".jpg")

	#Process
	watermark = process(dress)

	# Write output image
	cv2.imwrite("./out/oj"+str(i)+"out.jpg", watermark)

	#Exit
	#sys.exit()

if __name__ == '__main__':
	#main(5)
	#main(6)
	#main(7)
	#main(8)
	#main(9)
	#main(10)
	#main(11)
	main2()
