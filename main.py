# coding: utf8
import sys
import cv2
import argparse

from run import process

"""
main.py

 How to run:
 python main.py

"""


def main(inputpath, outpath):
	dress = cv2.imread(inputpath)

	h = dress.shape[0]

	w = dress.shape[1]

	dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)

	watermark = process(dress)

	watermark = cv2.resize(watermark, (w,h), interpolation=cv2.INTER_CUBIC)

	cv2.imwrite(outputpath, watermark)

	#sys.exit()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="simple deep nude script tool")
	parser.add_argument("-i", action="store", default="input.png")
	parser.add_argument("-o", action="store", default="output.png")
	inputpath, outputpath = parser.parse_args().i, parser.parse_args().o
	main(inputpath, outputpath)
