
def function(y):
	return (0.25*y)**(2) # Modify return value based on given polynomial.

def invfunction(y):
	return (2*y)**(1/2) # Modify return value based on given polynomial.

lowerbound = 0  # Modify return value based on given interval.
upperbound = 20  # Modify return value based on given interval.


#################


def deriv(x):
	return (function(x+0.0000000001) - function(x))/0.0000000001

def secderiv(x):
	return (deriv(x+0.0000000001) - deriv(x))/0.0000000001

def tester():
	# Returns True if function is always decreasing.
	"""
	>>> tester()
	-1 * function
	"""
	a = lowerbound 
	while secderiv(a) <= 0:
		a += 0.01
		if a == upperbound: 
			return True
	return False


import math 
def pointgen(): 
	if tester() == True:
		z = function(upperbound)
		f = open('3dprint.gcode', 'w')
		f.write('G21\nM107\nM190 S55\nM104 S196\nG28\nG1 Z5 F5000\nM109 S196\nG90\nG92 E0\nM83\n')
		while z <= function(lowerbound):
			f.write('G1 X'+str(100+invfunction(z))+' Y100 Z'+str(z)+'\n')
			f.write('G2 X'+str(100+invfunction(z))+' Y100 I'+str(-invfunction(z))+' J0 E'+str((invfunction(z))*math.pi/5)+'\n')
			f.write('G1 X'+str(99.6+invfunction(z))+' Y100 Z'+str(z)+'\n')
			f.write('G2 X'+str(99.6+invfunction(z))+' Y100 I'+str(-invfunction(z))+' J0 E'+str((invfunction(z))*math.pi/5)+'\n')
			f.write('G1 X'+str(99.2+invfunction(z))+' Y100 Z'+str(z)+'\n')
			f.write('G2 X'+str(99.2+invfunction(z))+' Y100 I'+str(-invfunction(z))+' J0 E'+str((invfunction(z))*math.pi/5)+'\n')
			z += 0.04
		f.close()

	else:
		z = function(upperbound)
		f = open('3dprint.gcode', 'w')
		f.write('G21\nM107\nM190 S55\nM104 S196\nG28\nG1 Z5 F5000\nM109 S196\nG90\nG92 E0\nM83\n')
		while z >= function(lowerbound):
			f.write('G1 Z'+str((function(upperbound))-z)+' F900\n')
			f.write('G1 X'+str(100-invfunction(z))+' Y100\n')
			f.write('G17 G2 X'+str(100-invfunction(z))+' Y100 I'+str(invfunction(z))+' J0 E'+str((invfunction(z))*math.pi)+' F900\n')
			f.write('G1 X'+str(99.6-invfunction(z))+' Y100\n')
			f.write('G17 G2 X'+str(99.6-invfunction(z))+' Y100 I'+str(invfunction(z)-0.04)+' J0 E'+str((invfunction(z)-0.04)*math.pi)+'\n')
			f.write('G1 X'+str(99.2-invfunction(z))+' Y100\n')
			f.write('G17 G2 X'+str(99.2-invfunction(z))+' Y100 I'+str(invfunction(z)-0.08)+' J0 E'+str((invfunction(z)-0.08)*math.pi)+'\n')
			z -= 0.04
		f.close()

def runcode():
	return pointgen()


