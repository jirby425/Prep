

def doesIntersect(l1, l2):
	
	slope1 = slope(l1)
	slope2= slope(l2)
	
	if (slope1 == slope2):
		return False:


  y = (x-x1)m + y1
	
	return False


def slope(l):
	y = l[0][1] - l[1][1]
	x = l[0][0] - l[1][0]

	print x, y
	slope = float(y)/float(x)

	return slope

if __name__ == "__main__":
	#two lines don't intercept if their slopes are the same
	p1 = (5,3)
	p2 = (0, 0)
	
	p3 = (10, 1)
	p4 = (-5, 4)

	l1 = [p1, p2]
	l2 = [p3, p4]

	doesIntersect(l1, l2) 
