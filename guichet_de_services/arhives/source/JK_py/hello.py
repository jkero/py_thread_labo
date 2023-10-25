
def JK_ma_fonc():

    from graphviz import Digraph
    
    g = Digraph('G', filename='hello.gv')
    
    g.edge('Hello', 'World')
    
    g.view()
    
JK_ma_fonc()