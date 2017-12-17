# -*- coding: utf-8 -*-

import re
import os
from num2words import num2words


def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))



def preprocess2(filename):
	
	# Open the file with read only permit
	# I opened the file all at once b/c it was easier to parse this way, but 
	# for a larger file it would be neccesary to buffer in some way
	f_in = open("./Gutenberg/txt/"+filename, 'r+', encoding="ISO-8859-1")
#	f_in = open("test.txt", 'r+', encoding="ISO-8859-1")
	f_out = open("thatFile.txt", 'a')

	text = f_in.read()

	# first, cut the text by sentences
	sentences = []

	# replace curly single quotes with straight single quotes
	text = text.replace("‘", "'")
	text = text.replace("’", "'")
#	text = text.replace("_", " ")

	# preserve punctuation with split
	text = text.replace(".",".<stop>")
	text = text.replace("?","?<stop>")
	text = text.replace("!","!<stop>")
	#text = re.sub(r"^[a-zA-Z0-9]+[\^\']*[a-zA-Z0-9]+[\^\']*[a-zA-Z0-9]*", "", text)
	text = re.sub(r"[a-zA-Z]+[0-9]+", "", text)
	text = re.sub(r"[0-9]+[il]", "[0-9]+[1]", text)
	text = re.sub(r"[0-9]+[oO]", "[0-9]+[0]", text)
	text = re.sub(r"[0-9]+[']+[0-9]*", "[0-9]+[ ]+[0-9]*", text)
	text = text.replace("\n", " ")
	sentences += re.split("<stop>", text)

	# for each sentence, split into individual words
	word_regex = r"\w[\w']*[\w]+|[.?!]|\w"
	all_words = [re.findall(word_regex, sentence) for sentence in sentences]

	num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	ordinal_list = ["rd", "th", "nd", "st", "TH", "RD", "ND", "ST"]
	ordinal_list_ = ["_rd", "_th", "_nd", "_st", "_TH", "_RD", "_ND", "_ST"]

	for sentence in all_words:
		for word in sentence:
#			word = word.replace("_","")	
			if word[0] in num_list and word[-1] in num_list:
				word = int_to_en(int(word))	
			if word[0] in num_list and word[-3:] in ordinal_list_:
                                word = word[:-3]
                                #word = re.findall('(\d+(st|nd|rd|th))', word)
                                word = num2words(int(word), ordinal=True)
                                word = word.replace("-", " ")
			if word[0] in num_list and word[-2:] in ordinal_list:
				word = word[:-2]
				#word = re.findall('(\d+(st|nd|rd|th))', word)
				word = num2words(int(word), ordinal=True)
				word = word.replace("-", " ")
		#	if word == "." or word == "?" or word == "!":
		#		f_out.write(word + "\n")
#			for char in word:
#				char = char.replace("_", "")
		#	else: 
#				word = word.replace("_", " ")
		#		f_out.write(" " + word)
				#word = (" " + word)
			#word = word.replace("_", " ")
			#f_out.write(" " + word)

	for sentence in all_words:
		for word in sentence:
			if "_" in word:
				word = word.replace("_", "")
			if word == "." or word == "?" or word == "!":
                                f_out.write(word + "\n")
			else:
                        	f_out.write(" " + word)	
	# f2_in = open("thatFile.txt", 'r+', encoding="ISO-8859-1")
	# f2_out = open("thatOtherFile.txt", "a")

	#for line in f2_in:
	#	for char in line:
	#		char = char.replace("_", "")
	#		f2_out.write(char)

	
	#f2_in.close()
	#f2_out.close()
	f_in.close()
	f_out.close()

for f in os.listdir("./Gutenberg/txt/"):
	print(f)
	preprocess2(f)
