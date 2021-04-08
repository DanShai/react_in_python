from libs.py_react import useState, createElement as CR

def Search(props):
    txt , setTxt = useState('')
    get_query = props['get_query']

    def on_change(q):
        setTxt(q)
        get_query(q)

    q_inp_prp = {'type':'text' , 'className':'form-control',
                'placeholder':'Search..','value':txt,'autoFocus':True,
                'onChange': lambda e : on_change(e.target.value) }
    q_inp = CR('input' , q_inp_prp) 
    form = CR('form',None,q_inp)
    section = CR('section',None,form)
    return section