for x in range(00,150):
	TGREEN =  '\033['+str(x)+'m' # Green Text
	print (TGREEN + "This is some green text!" + "       " + str(x))
