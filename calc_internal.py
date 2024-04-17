
#TODO: cursor, factorial, use keyboard input

from common import EraseMode

from mathfuncs import inf as Infinity
from mathfuncs import angleMode

expression=[]        							#full expression to be evaluated
openParenthesis = 0  							#incremented every time we press "(" and decremented when ")"
ANS = 0							 							#last result
ANSFlag = False      							#did we just press equal?
currentAngleMode = angleMode.rad  #rad or deg?


# lists for categorising all the tokens
OPERATORS = [
	"+",
	"-",
	"*",
	"/",
	"^",
	"√",
	"%"
]
#this is dumb, but it's used in the parenthesis function when opening a new one
NUMBERS = [
	"0",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9"
]
CONSTANTS = [
	"e",
	"π",
	"τ",
	"φ",
	"ANS"
]
FUNCTIONS = [
	"sin",
	"cos",
	"tan",
	"asin",
	"acos",
	"atan",
	"ln",
	"exp",
	"log",
	"√",
	"abs",
	"rec",
	"fact",
	"sec",
	"csc",
	"cot"
]
anglemode_funcs = ["sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "cot(", "csc(", "sec("]

# BUTTON FUNCS

def Btn_Number(num):
	global expression, ANSFlag
	if ANSFlag == True:   #true if we just pressed equal
		expression = [str(num)]
		ANSFlag = False
		return
	if len(expression) == 0:
		expression += [str(num)]
		return
	if expression[-1] == ")" or expression[-1] in CONSTANTS:
		expression += ["*"]
	if expression[-1] == "0" and len(expression) == 1:
		expression.pop()
	expression += [NUMBERS[num]] #big brain time

def Btn_Dot():
	global expression, ANSFlag
	if ANSFlag == True:
		ANSFlag = False
		expression = ["."]
		return
	if len(expression) == 0:
		expression += ["."]
		return
	if expression[-1] in CONSTANTS:
		expression += ["*"]
	if not expression[-1] == ".":
		expression += ["."]

def Btn_Const(const : str):
	global expression, ANSFlag
	if ANSFlag == True:  #if we just pressed equal, in this case the logic is the same as below so just reset the flag
		expression += ["*"]
		ANSFlag = False
	if not len(expression) == 0:
		if expression[-1] == ")" or expression[-1] in CONSTANTS or expression[-1] in NUMBERS or expression[-1] == ".":
			expression += ["*"]
		if expression[-1] == "0" and len(expression) == 1:
			expression.pop()
	#END IF
	expression += [const]

def Btn_Func(func : str):
	global expression, openParenthesis, ANSFlag
	if func not in FUNCTIONS:
		raise Exception("wot")
	if ANSFlag == True:  #for functions and operators, usually you want to keep the result
		expression = [(func + "("), "ANS"]
		openParenthesis += 1
		ANSFlag = False
		return
	elif not len(expression) == 0:
		if expression[-1] == ")" or expression[-1] in CONSTANTS or expression[-1] in NUMBERS or expression[-1] == ".":
			expression += ["*"]
	expression += [(func + "(")]
	openParenthesis += 1


def Btn_Ans():
	global expression, ANSFlag
	if ANSFlag == True:
		ANSFlag = False
		expression = []
	elif not len(expression) == 0:
		if expression[-1] in NUMBERS or expression[-1] in CONSTANTS:
			expression += ["*"]
	expression += ["ANS"]


def Btn_Erase(mode : EraseMode):
	global expression, openParenthesis, ANSFlag
	if mode == EraseMode.all:
		expression = []
		openParenthesis = 0
	else:
		if len(expression) == 0:
			return
		#we can't just check if it's equal, as most of the time there's going to be funcs. instead check this
		if "(" in expression[-1]:
			openParenthesis -= 1
		elif expression[-1] == ")":
			openParenthesis += 1
		expression.pop()
	ANSFlag = False


def Btn_Operator(operator: str):
	global expression, ANSFlag
	sign_operators = ["-", "+"]
	# exit to prevent errors, except special cases for operators that can give a sign to numbers
	if (len(expression) == 0) or ("(" in expression[-1]):
		if operator in sign_operators:
			expression += [ operator ]
		return
	
	# we'll add the answer and then the operator
	if ANSFlag == True:
		expression = ["ANS"]
		ANSFlag = False

	#if we have already an operator we want to remove it before adding ours
	while expression[-1] in OPERATORS:
		# this means: if the operator we're trying to add is a sign operator (+ or -) and we wrote any other operator
		if operator in sign_operators and expression[-1] not in sign_operators:
			# we'll add the operator anyways, plus a parenthesis for improved readability
			Btn_OpenPar()
			expression += [ operator ]
		else:
			# this is reached if:
			#	1) the operator we're writing is not a sign operator
			#	2) the operator we're writing is a sign operator but there is already a sign operator
			# in this case we overwrite the previous ones
			expression.pop()
			if len(expression) == 0: break	# here to prevent IndexError if we remove all operators

	expression += [ operator ]


def Btn_OpenPar():
	global expression, openParenthesis, ANSFlag
	if ANSFlag == True:  #we do everything normally, so just reset flag
		ANSFlag = False
	elif not len(expression) == 0:
		if expression[-1] in NUMBERS or expression[-1] in CONSTANTS:
			expression += ["*"]
	#END IF
	expression += ["("]
	openParenthesis += 1

def Btn_ClosePar():
	global expression, openParenthesis
	if len(expression) == 0:
		return
	if ANSFlag == True:
		return
	if expression[-1] in OPERATORS or "(" in expression[-1]:
		expression += ["0"]
	expression += [")"]
	openParenthesis -= 1


def Btn_ChangeAngleMode():
	global currentAngleMode
	if currentAngleMode == angleMode.deg:
		currentAngleMode = angleMode.rad
	else:
		currentAngleMode = angleMode.deg
		

def Btn_EqualSign() -> None | str:
	"""return a message to print, if any, or None if we just want to show the expression's result"""
	global openParenthesis, expression, ANS, ANSFlag, currentAngleMode
	if len(expression) == 0:
		ANS = 0
		expression = ["0"]
		return
	if openParenthesis > 0:
		while openParenthesis > 0:
			Btn_ClosePar()
	else:
		pars = "(" * abs(openParenthesis)  #we'll open this number of parenthesis, to compensate for the closed ones
		openParenthesis = 0
		expression.insert(0, pars) #insert at the beginning. this way, if for example the user says "9)*2)" we'll change the string to say "((9)*2)"
	#END PAR CHECK
	
	if currentAngleMode == angleMode.deg:
		count = 0
		for i in range(len(expression)):
			currentToken = expression[i]

			if count > 0 and currentToken == ")":
				count -= 1
				expression.insert(i, ", angleMode.deg")

			if currentToken in anglemode_funcs:
				count += 1
	#END ANGLE CHECK

	#convert custom operators to things readable by python
	tokenConversion = {
		"^" : "**",
		"√(" : "Sqrt(",		# TODO: see if the root causes problems somehow
	}
	for i in range(len(expression)):
		if expression[i] in tokenConversion:
			expression[i] = tokenConversion[expression[i]]
	expressionToString = "".join(expression)
	
	#TODO: inconsistency between the use of OverflowError and Infinity. only one should be used
	try:
		from mathfuncs import e
		from mathfuncs import pi as π
		from mathfuncs import phi as φ
		from mathfuncs import tau as τ
		from mathfuncs import sin, cos, tan, asin, acos, Sqrt, ln, log, atan, rec, sec, csc, cot
		from mathfuncs import EXP as exp
		from mathfuncs import factorial as fact
		ANS = eval(expressionToString)
		if isinstance(ANS, complex): raise complex # yes
		if ANS == None: raise None
	except SyntaxError:
		return_message = "Invalid Syntax"
		return return_message
	except ZeroDivisionError:
		ANS = Infinity
	except OverflowError:
		return_message = "Overflow Error"
		return return_message
	except Exception as exc:   #if there's an exception some value could have had an invalid thing like asin(2), so catch
		# manage exception
		import traceback
		print("".join(traceback.format_exception(exc)))				#console is not seen by user anyways
		# return the message that there was an error in the expression
		import random, time
		random.seed(time.time())
		return_message = "Math Error" if random.randint(0, 9) > 0 else "UNKNOWN ERROR: TO FIX, PLEASE VISIT:\nhttps://www.youtube.com/watch?v=doEqUhFiQS4"
		expression = []		#change it to show in screen, and change it back with no update
		return return_message
	
	ANSFlag = True
	expression = []
	for char in str(ANS):
		expression.append(char)
	if ANS == Infinity or ANS == -Infinity:  #infinity is unsigned. change my mind.
		expression = [ "Infinity" ]
	print(ANS)
#END


# OTHER FUNCS
def GetExpression() -> list[str]:
	return expression
def GetExpressionStr() -> str:
	return "".join(expression)

def GetAns() -> str:
	return str(ANS)
def GetAngleMode() -> angleMode:
	return currentAngleMode
