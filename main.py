#!/usr/bin/env python3

from calc_window import CalcBody_Init, UpdateScreen, SetAngleModeText

from calc_internal import GetExpressionStr, GetExpression, GetAns, GetAngleMode
from calc_internal import Btn_Ans, Btn_Operator, Btn_ChangeAngleMode, Btn_ClosePar, Btn_Const, Btn_Dot, Btn_Number, Btn_EqualSign, Btn_Erase, Btn_Func, Btn_OpenPar

def Call_EqualFunction():
    ans = Btn_EqualSign()
    if ans is None:
        ans = GetAns()
    UpdateScreen(ans)
def Call_Btn_Press(func):
    func()
    UpdateScreen(GetExpressionStr())
    
window, screen = CalcBody_Init(
    title="Calculator++",
    geometry="700x640",
    
    equal_function=Call_EqualFunction,
    ans_function=lambda:Call_Btn_Press(Btn_Ans),
    erase_function=lambda mode: Call_Btn_Press(lambda:Btn_Erase(mode)),
	anglemode_function=lambda: (Btn_ChangeAngleMode(), SetAngleModeText(GetAngleMode())),

    const_function=lambda c: Call_Btn_Press(lambda:Btn_Const(c)),
    function_function=lambda f:Call_Btn_Press(lambda:Btn_Func(f)),
    number_function=lambda n: Call_Btn_Press(lambda:Btn_Number(n)),
    operator_function=lambda op: Call_Btn_Press(lambda:Btn_Operator(op)),
    
    dot_function=lambda: Call_Btn_Press(Btn_Dot),
    openpar_function = lambda: Call_Btn_Press(Btn_OpenPar),
    closepar_function= lambda: Call_Btn_Press(Btn_ClosePar),
)

window.mainloop()
