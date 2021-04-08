from libs.py_react import createElement as CR
from components.charachters.char_item import CharItem
from components.ui.spinner import Spinner


def CharGrid(props):
    items = props['items']
    isLoading = props['isLoading']
    get_item = lambda item : CR(CharItem, {'key': item['char_id'],'item': item} )
    lst_items = list(map( get_item ,items))
    section = CR('section',{'className':'cards'} , lst_items)

    return Spinner if isLoading  else section 