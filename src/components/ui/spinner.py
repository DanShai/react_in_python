from libs.py_react import createElement as CR
from libs.py_react import require # __:skip

def Spinner():
    istyle = {{ 'width': '200px', 'margin': 'auto', 'display': 'block' }}
    return CR('img' , {'src':require('../img/spinner.gif') ,  'alt':'loading','style':istyle})
    