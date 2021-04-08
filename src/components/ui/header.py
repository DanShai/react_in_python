from libs.py_react import createElement as CR
from libs.py_react import require # __:skip

def Header():
    h =  CR('header' , {'className':'center'},
    CR('img',{'src':require('../img/logo.png'),'alt':''},None) )
    return h