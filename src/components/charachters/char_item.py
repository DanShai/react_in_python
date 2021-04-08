from libs.py_react import createElement as CR

def CharItem(props):
    item = props['item']
    li_nick = CR('li' , None , 'Nickname : ' + item['nickname'])
    li_status = CR('li' , None , 'Status : ' + item["status"])
    ul = CR('ul', None , li_nick,li_status)
    h1 = CR('h1', None , item['name'])
    div_back = CR('div', {'className':'card-back'} ,h1,ul)
    img = CR('img', {'src': item['img'] ,'alt':'' } )
    div_front = CR('div', {'className':'card-front'} ,img)
    div_inner = CR('div', {'className':'card-inner'} ,div_front,div_back)
    div_card = CR('div', {'className':'card'} ,div_inner)
    return div_card
    
    
    