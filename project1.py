#Name:        Isaac Rodriguez
#Student ID:  002810209
#Date:        9/9/16
#Assignment:  Project 1 - Median Filter


from PIL import Image     #Allows you to process images
im1 = Image.open ("1.png")
im2 = Image.open ("2.png")
im3 = Image.open ("3.png")
im4 = Image.open ("4.png")
im5 = Image.open ("5.png")
im6 = Image.open ("6.png")
im7 = Image.open ("7.png")
im8 = Image.open ("8.png")
im9 = Image.open ("9.png")

imStorage = [im1, im2, im3, im4, im5, im6, im7, im8, im9] #stores all nine images in the list imStorage

rlist = []
glist = []
blist = []

def median(imStorage):                #Median function
	imsLength = len(imStorage)        #stores length of imStorage into imsLength
	sortedValues = sorted(imStorage)  #sorts imStorage and stores it into sortedValues
	middleIndex = ((imsLength+1)/2)-1 #Gives location of middle value
	return sortedValues[middleIndex]  #Returns what is located at the middle value

for x in range (0,494):      #loop from 0 to width-1 
	for y in range (0,556):  #loop from 0 to height-1
		for image in imStorage: 
			
			r,g,b = image.getpixel((x,y)) 
			
			rlist.append(r) #pushes data from r to rlist[]
			glist.append(g) #pushes data from g to glist[]
			blist.append(b) #pushes data from b to blist[]
		

		

	
#Sources:
#http://pillow.readthedocs.io/en/3.3.x/reference/Image.html
#https://drive.google.com/a/csumb.edu/file/d/0B6aGWtqrdN2gc1JpSEdjaWpLbG8/view
#https://drive.google.com/file/d/0B6aGWtqrdN2gRFdfN1Y0R25VYkE/view
#John Sullivan(TA for CST 205)
#Siddarth Krishnan (Classmate in CST 205)