import tkinter as _tk

from mathfuncs import angleMode as _anglemode_t
from common import EraseMode


BOOT_MESSAGES = [
	"better than the Windows default calculator since 2021",
	"never trust youtube links",
	"ready to calculate the answer to life, the universe and everything?",
	"42",
]

EQUAL_COLOURS = [ "brown1", "tomato" ]
OP_COLOURS    = [ "lightsteelblue2", "lightsteelblue3" ]
CONST_COLOURS = [ "light cyan", "cadet blue" ]
FUNC_COLOURS  = [ "medium sea green", "sea green" ]
KEY_COLOURS   = [ "grey26", "grey81" ]

DEFAULTHEIGHT = 3
DEFAULTWIDTH  = 5


#WINDOW SETUP
def CalcBody_Init(geometry, title, equal_function, number_function, dot_function, const_function, operator_function, openpar_function, closepar_function, function_function, erase_function, anglemode_function, ans_function) -> tuple[_tk.Tk, _tk.Frame]:
	window=_tk.Tk()
	window.geometry(geometry)
	window.title(title)
	window.config(background='gray')

	ROWOFFSET = 4
	COLOFFSET = 1

	#these two just make the screen look nicer
	_tk.Button(window, height=DEFAULTHEIGHT, width=DEFAULTWIDTH, bg="gray", state=_tk.DISABLED).grid(row=1)
	_tk.Button(window, height=DEFAULTHEIGHT, width=DEFAULTWIDTH, bg="gray", state=_tk.DISABLED).place(x=520, y=0)


	# BUTTON DEFINITIONS
	btnNums = []
	btnNums.append(_tk.Button(window, text="0", command=lambda:number_function(0), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="1", command=lambda:number_function(1), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="2", command=lambda:number_function(2), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="3", command=lambda:number_function(3), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="4", command=lambda:number_function(4), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="5", command=lambda:number_function(5), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="6", command=lambda:number_function(6), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="7", command=lambda:number_function(7), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="8", command=lambda:number_function(8), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	btnNums.append(_tk.Button(window, text="9", command=lambda:number_function(9), width=DEFAULTWIDTH,height=DEFAULTHEIGHT))
	# update 2/4/2023: i wrote this `for` like a year and a half ago, and i now have no idea what the fuck it's doing
	for i in range(1, len(btnNums)):
		#overcomplicated way of setting button positions automatically
		_row = 1+(2 - ((i - 1) // 3)) + ROWOFFSET
		_col = ((i - 1) % 3) + COLOFFSET
		btnNums[i].grid(row = _row, column = _col)
	#END FOR
	btnNums[0].grid(column = COLOFFSET + 1, row = ROWOFFSET + 4)

	dotBtn = _tk.Button(window, text=".", command=dot_function, width=DEFAULTWIDTH,height=DEFAULTHEIGHT)
	dotBtn.grid(column = COLOFFSET, row = ROWOFFSET + 4)



	piBtn  = _tk.Button(window, text="π", command=lambda:const_function("π"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=CONST_COLOURS[0], activebackground=CONST_COLOURS[1])
	eBtn   = _tk.Button(window, text="e", command=lambda:const_function("e"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=CONST_COLOURS[0], activebackground=CONST_COLOURS[1])
	phiBtn = _tk.Button(window, text="φ", command=lambda:const_function("φ"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=CONST_COLOURS[0], activebackground=CONST_COLOURS[1])
	tauBtn = _tk.Button(window, text="τ", command=lambda:const_function("τ"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=CONST_COLOURS[0], activebackground=CONST_COLOURS[1])
	
	piBtn .grid(row=ROWOFFSET, column=COLOFFSET+0)
	eBtn  .grid(row=ROWOFFSET, column=COLOFFSET+1)
	phiBtn.grid(row=ROWOFFSET, column=COLOFFSET+2)
	tauBtn.grid(row=ROWOFFSET, column=COLOFFSET+3)


	addBtn = _tk.Button(window, text="+",   command=lambda:operator_function("+"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	subBtn = _tk.Button(window, text="-",   command=lambda:operator_function("-"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	mulBtn = _tk.Button(window, text="*",   command=lambda:operator_function("*"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	divBtn = _tk.Button(window, text="/",   command=lambda:operator_function("/"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	powBtn = _tk.Button(window, text="^",   command=lambda:operator_function("^"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	oppBtn = _tk.Button(window, text="(",   command=openpar_function, 			   width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	clpBtn = _tk.Button(window, text=")",   command=closepar_function,			   width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])
	modBtn = _tk.Button(window, text="mod", command=lambda:operator_function("%"), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=OP_COLOURS[0], activebackground=OP_COLOURS[1])

	powBtn.grid(column=COLOFFSET+3, row=ROWOFFSET+5)
	divBtn.grid(column=COLOFFSET+3, row=ROWOFFSET+1)
	mulBtn.grid(column=COLOFFSET+3, row=ROWOFFSET+2)
	subBtn.grid(column=COLOFFSET+3, row=ROWOFFSET+3)
	addBtn.grid(column=COLOFFSET+3, row=ROWOFFSET+4)
	modBtn.grid(column=COLOFFSET+0, row=ROWOFFSET+5)
	oppBtn.grid(column=COLOFFSET+1, row=ROWOFFSET+5)
	clpBtn.grid(column=COLOFFSET+2, row=ROWOFFSET+5)



	qrtBtn = _tk.Button(window, text="√",    command=lambda:function_function("√"),    width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	sinBtn = _tk.Button(window, text="sin",  command=lambda:function_function("sin"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	cosBtn = _tk.Button(window, text="cos",  command=lambda:function_function("cos"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	tanBtn = _tk.Button(window, text="tan",  command=lambda:function_function("tan"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	asnBtn = _tk.Button(window, text="asin", command=lambda:function_function("asin"), width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	acsBtn = _tk.Button(window, text="acos", command=lambda:function_function("acos"), width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	atnBtn = _tk.Button(window, text="atan", command=lambda:function_function("atan"), width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	lnBtn  = _tk.Button(window, text="ln",   command=lambda:function_function("ln"),   width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	expBtn = _tk.Button(window, text="exp",  command=lambda:function_function("exp"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	logBtn = _tk.Button(window, text="log",  command=lambda:function_function("log"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	recBtn = _tk.Button(window, text="rec",  command=lambda:function_function("rec"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	absBtn = _tk.Button(window, text="abs",  command=lambda:function_function("abs"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	secBtn = _tk.Button(window, text="sec",  command=lambda:function_function("sec"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	cscBtn = _tk.Button(window, text="csc",  command=lambda:function_function("csc"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	cotBtn = _tk.Button(window, text="cot",  command=lambda:function_function("cot"),  width=2*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])
	facBtn = _tk.Button(window, text="!",    command=lambda:function_function("fact"), width=1*DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=FUNC_COLOURS[0], activebackground=FUNC_COLOURS[1])

	qrtBtn.grid(column=COLOFFSET+4, row=ROWOFFSET+0)
	logBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+0)
	# facBtn.grid(column=COLOFFSET+6, row=ROWOFFSET+0)
	sinBtn.grid(column=COLOFFSET+4, row=ROWOFFSET+1)
	asnBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+1)
	cosBtn.grid(column=COLOFFSET+4, row=ROWOFFSET+2)
	acsBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+2)
	tanBtn.grid(column=COLOFFSET+4, row=ROWOFFSET+3)
	atnBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+3)
	lnBtn .grid(column=COLOFFSET+4, row=ROWOFFSET+4)
	expBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+4)
	recBtn.grid(column=COLOFFSET+4, row=ROWOFFSET+5)
	absBtn.grid(column=COLOFFSET+5, row=ROWOFFSET+5)
	secBtn.grid(column=COLOFFSET+6, row=ROWOFFSET+2)
	cscBtn.grid(column=COLOFFSET+6, row=ROWOFFSET+1)
	cotBtn.grid(column=COLOFFSET+6, row=ROWOFFSET+3)



	delBtn = _tk.Button(window, text="⌫", command=lambda:erase_function(EraseMode.bks), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=KEY_COLOURS[0], activebackground=KEY_COLOURS[1])
	delBtn.grid(row=ROWOFFSET-1, column=COLOFFSET)
	acBtn  = _tk.Button(window, text="AC", command=lambda:erase_function(EraseMode.all), width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=KEY_COLOURS[0], activebackground=KEY_COLOURS[1])
	acBtn.grid(row=ROWOFFSET-1, column=COLOFFSET+1)
	ansBtn = _tk.Button(window, text="ANS", command=ans_function, width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=KEY_COLOURS[0], activebackground=KEY_COLOURS[1])
	ansBtn.grid(row=ROWOFFSET-1, column=COLOFFSET+2)

	global angleModeBtn
	angleModeBtn = _tk.Button(window, text="rad", command=anglemode_function, width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=KEY_COLOURS[0], activebackground=KEY_COLOURS[1])
	angleModeBtn.grid(row=ROWOFFSET-1, column=COLOFFSET+3)


	evalBtn = _tk.Button(window, text="=", command=equal_function, width=DEFAULTWIDTH,height=DEFAULTHEIGHT, bg=EQUAL_COLOURS[0], activebackground=EQUAL_COLOURS[1])
	evalBtn.grid(row=ROWOFFSET + 4, column=COLOFFSET+2)

	global screen
	screen = _tk.Text(window, height = 3, width = 56)
	screen.place(x=70, y=2)   #sorry Noor, but i'm not sorry

	import random,time
	random.seed(time.time())
	screen.insert(1.0, random.choice(BOOT_MESSAGES))
	del(random,time)
	#disabled to, yk, prevent arbitrary code execution
	screen["state"] = _tk.DISABLED

	#for debug purposes
	#_tk.Button(window, text="p", command=lambda:print(expression)).grid(row=5,column=5)

	return (window, screen)
#END

def UpdateScreen(message):
	screen["state"] = _tk.NORMAL	#I love that to write you have to enable it, and then disable afterwards. idk why, it reminds me of programming the GB
	screen.delete(1.0, "end")		#what is this terribleness
	screen.insert(1.0, message)
	screen["state"] = _tk.DISABLED	#btw this allows for arbitrary code execution lmao

def SetAngleModeText(mode: _anglemode_t):
	angleModeBtn["text"] = "deg" if mode == _anglemode_t.deg else "rad"

