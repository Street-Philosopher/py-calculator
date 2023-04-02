#why import the regular math functions when you can make your own lmao
from math import factorial #only math thing i import, promise
from math import atan as t #also atan because yes
from enum import Enum



class angleMode(Enum):
	rad = 0
	deg = 1

def Sqrt(x):
	return x ** .5

#FUNCTIONS
def cos(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	if x == float("inf") or x == -float("inf"):  #if it is, the folllowing loop will go infinite
		return float("inf")#float("nan")
	#this prevents angles from being bad
	if mode == angleMode.deg:
		x *= DEG2RAD #convert to rad because i'm lazy
	if isinstance(x, float):
		while x > +pi:
			x -= 2 * pi
		while x < -pi:
			x += 2 * pi

	if sigfigs > 15: #we don't want to show imprecisions
		sigfigs = 15
	
	# I N F I N I T E S E R I E S
	result = 0
	for n in range(precision):
		change = (-(x**2)) ** n
		change /= factorial(2 * n)
		result += change
	#END FOR

	if (isinstance(result, float)):
		return round(result, sigfigs)
	else:
		return result
#END COS

#lol
def sin(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	if mode == angleMode.deg:
		x *= DEG2RAD
	return cos((x - (pi/2)), angleMode.rad, precision, sigfigs)

def tan(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	#END CASE CHECK
	tn = sin(x, mode, precision, sigfigs) / cos(x, mode, precision, sigfigs)
	return round(tn, sigfigs)

def sec(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	res = 1 / cos(x, mode, precision, sigfigs)
	return res

def csc(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	res = 1 / sin(x, mode, precision, sigfigs)
	return res

def cot(x : float, mode : angleMode = angleMode.rad, precision = 22, sigfigs = 15) -> float:
	if x == (90 if mode == angleMode.deg else pi/2):
		return 0
	res = 1 / tan(x, mode, precision, sigfigs)
	return res

def asin(x : float, mode : angleMode = angleMode.rad, precision : int = 60) -> float:
	direction = 0   #one for increase, neg one for decrease
	if x > 0:
		direction = +1
	elif x < 0:
		direction = -1
	else:
		return 0
	
	delta = 45  #we'll start using degrees, it's easier to keep track of
	estimate = 0  #too lazy to google more infinite sums
	if abs(x) > 1:
		return None

	for i in range(precision):
		estimate += delta * direction
		delta /= 2   #reduce delta, so we can get closer to the actual value
		sn = sin(estimate, angleMode.deg)
		if sn > x:
			direction = -1
		elif sn < x:
			direction = +1
		else:
			#we don't immediately return because first we convert
			break #we found a result! yay! never going to happen lol

	if mode == angleMode.rad:
		estimate *= DEG2RAD

	#at the end of the process we'll return the estimate
	return estimate
#END
def acos(x : float, mode : angleMode = angleMode.rad, precision : int = 60) -> float:
	direction = 0
	if x < 0:
		direction = +1
	elif x > 0:
		direction = -1
	else:#  x is 0
		if mode == angleMode.rad: return pi/2
		else: return 90
	#END dir check
	delta = 45
	estimate = 90
	if abs(x) > 1: return None

	for i in range(precision):
		estimate += delta * direction
		delta /= 2
		cs = cos(estimate, angleMode.deg)
		if cs < x:
			direction = -1
		elif cs > x:
			direction = +1
		else: break
	#END FOR
	if mode == angleMode.rad:
		estimate *= DEG2RAD
	
	return estimate
#END
def atan(x : float, mode : angleMode = angleMode.rad, precision : int = 500) -> float:
	retVal = t(x)
	return retVal * (RAD2DEG if mode == angleMode.deg else 1)

	def neg1to1(x, p):
		tot = 0
		for n in range(p):
			delta = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
			tot += delta
		return tot
	def rest(x, p):
		tot = 0
		for n in range(p):
			delta = ((-1)**n) / ((2*n + 1) * (x**(2*n + 1)))
			tot += delta
		return tot
	#END

	res = 0
	if abs(x) <= 1:
		res = neg1to1(x, precision)
	else:
		res = rest(x, precision)
	
	if mode == angleMode.deg:
		res *= RAD2DEG
	
	return res

def rec(x : float):
	"""reciprocal"""
	return (1 / x)

#yes.
def EXP(x : float, precision = "infinity") -> float:
	return e ** x

#more precision will break stuff
def ln(x : float, precision = 400) -> float:
	if isinstance(x, float):
		if x <= 0:
			return None

	def formula(n, p):
		return 2 * ((n - EXP(p)) / (n + EXP(p)))
	
	result = 0
	for i in range(precision):
		result += formula(x, result)
	
	return result

def log(a : float, b : float = 10, precision = 400):
	return (ln(a, precision) / ln(b, precision))

#returns e to the "i * x" power
def eix(x : float) -> complex:
	real = cos(x)
	imag = sin(x)
	return complex(real, imag)

#CONSTANTS
i   = complex(0, 1)
pi  = 3.1415926535897932384626433
e   = 2.7182818284590452353602875
tau = 2 * pi
phi = (1 + (5 ** .5)) / 2
inf = float("inf")


DEG2RAD = pi / 180
RAD2DEG = 180 / pi
