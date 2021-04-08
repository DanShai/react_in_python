from libs.py_react import useState,useEffect,axios, createElement as CR
from components.ui.header import Header
from components.ui.search import Search
from components.charachters.char_grid import CharGrid


def App():
    items, setItems = useState([])
    isLoading, setIsLoading = useState(True)
    query, setQuery = useState('')
    
    def get_chars(): 
        async def fetch_chars():
            setIsLoading(True) 
            try:
                result = await axios('https://www.breakingbadapi.com/api/characters?name='+query)
                setItems(result.data)
                setIsLoading(False)
            except Exception as e:
                print(e)
        fetch_chars()

    useEffect( get_chars,[query]) 
    get_query = lambda q : setQuery(q)
    header = CR(Header,None)
    search_q = CR(Search,{'get_query': get_query},None)
    char_grid = CR(CharGrid, {'isLoading':isLoading, 'items':items},None)
    div_container = CR('div' ,{'className':'container'} , 
                    header , search_q,char_grid)
    return div_container