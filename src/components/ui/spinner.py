from libs.py_react import createElement as CR
from libs.py_react import require # __:skip
spnimg = require('../img/spinner.gif')


def Spinner():
    istyle = {{ 'width': '200px', 'margin': 'auto', 'display': 'block' }}
    return CR('img' , {'src':spnimg ,  'alt':'loading','style':istyle})
    