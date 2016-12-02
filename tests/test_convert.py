import pytest
import networkx as nx
import json

"""
Draw a graph with matplotlib.
You must have matplotlib for this to work.
"""
try:
    import matplotlib.pyplot as plt
except:
    raise


def test_obj():
    import obographs.graphmaker
    G = obographs.graphmaker.convert_json_object(
        {'graphs':
         [
             {
                 'nodes': [
                     {'id': 'A',
                      'lbl': 'A'},
                     {'id': 'B',
                      'lbl': 'B'}
                 ],
                 'edges': [
                     {'sub': 'A',
                      'pred': 'is_a',
                      'obj': 'B'}
                 ]
             }
         ]}
    )
    nx.draw(G)
    plt.savefig("examples/simple_obj.png") # save as png

def test_parse():
    import obographs.graphmaker
    G = obographs.graphmaker.convert_json_file("tests/nucleus.json")
    labelmap = nx.get_node_attributes(G,'lbl')
    nx.draw_networkx(G, labels=labelmap)
    plt.savefig("examples/nucleus.png") # save as png
    

if __name__ == '__main__':
    pytest.main()
    print("HI")
