
from enum import Enum
#used in the "erase" function. first means to just do backspace, second is "AC"
class EraseMode(Enum):
	bks = 0,
	all = 1
del(Enum)
