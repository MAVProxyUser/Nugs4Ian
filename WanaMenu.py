#!/usr/bin/env python3
# Description:
# WanaBrands gummy ratio calculations
# https://www.wanabrands.com/product-category/products/ohio/medical-ohio/
# https://www.wanabrands.com/archive/2019/wana-brands-offers-medical-patients-in-ohio-a-variety-of-ratios-and-classes-for-simple-and-consistent-dosing/
#
# Requirements:
# $ pip3 install pick
# 
# Usage:
# python3 WanaMeny.py
#
# Use space bar to select gummies to be used in the dose. Press enter when done. Select number of gummies when asked, press enter. Repeat for each type.

from pick import pick
import sys

# Specific batches for base refrence
flavorRatios = {
	# Bottle notation                                     # CBD:TBC notation
#	'blood_orange'        : "109.09,  0.00,   4",         # 0:1   (Sativa)
	'blueberry'           : "103.05,  4.05,   10",        # 0:1   (Indica)
	'exotic_yuzu'         : "99.86,   205.14, 10",        # 2:1
	'mango'               : "98.1,    13.11,  10",        # 0:1   (Sativa)
	'pomegranate'         : "95.46,   456.56, 20",        # 5:1   
#	'raspberry_limeaid'   : "113.32,  3.69,   4",         # 0:1   (Indica)
	'strawberry'          : "10.66,   107.1,  10",        # 10:1
	'strawberry_lemonade' : "98.68,   98.95,  10",        # 1:1
	'watermelon'          : "102.05,  0.0,    10",        # 0:1   (Hybrid)
}

if len(sys.argv) > 1:
	for gummy, ratios in flavorRatios.items():
		print("%s - THC %s : CBD : %s, per %s" % (gummy, ratios.split(",")[0], ratios.split(",")[1], ratios.split(",")[2]))
	sys.exit(0)

title = 'Choose the Wana gummies being used with the space bar, press enter when done: '
options = ['blueberry', 'exotic_yuzu', 'mango', 'pomegranate', 'strawberry', 'strawberry_lemonade', 'watermelon']
selected = pick(options, title, multiselect=True, min_selection_count=1)

totalCBD = 0
totalTHC = 0

for flavor in selected:
	flavorTHC = 0
	flavorCBD = 0

	title = 'how many quarter (1/4) chunks of ' + flavor[0] + "?"
	options = ['one', 'two', 'three', 'four', 'five', 'six']
	selected = pick(options, title)

	thc = float(flavorRatios[flavor[0]].split(",")[0])
	cbd = float(flavorRatios[flavor[0]].split(",")[1])
	count = float(flavorRatios[flavor[0]].split(",")[2])

	flavorTHC = flavorTHC + (((thc/count)/4) * (selected[1]+1))
	flavorCBD = flavorCBD + (((cbd/count)/4) * (selected[1]+1))

	totalTHC = totalTHC + flavorTHC
	totalCBD = totalCBD + flavorCBD

	
print(["Total THC",totalTHC,"Total CBD",totalCBD])
