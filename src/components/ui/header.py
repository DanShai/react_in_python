from libs.py_react import createElement as CR
from libs.py_react import require # __:skip
logo = require('../img/logo.png')

def Header():
    h =  CR('header' , {'className':'center'},
    CR('img',{'src':logo,'alt':''},None) )
    return h