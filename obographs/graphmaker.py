import itertools
import re
import json

import networkx

def add_obograph_digraph(og, digraph, labeldict):
    """
    Converts a single obograph to Digraph edges and adds to an existing networkx DiGraph

    """
    for n in og['nodes']:
        is_obsolete =  'is_obsolete' in n and n['is_obsolete'] == 'true'
        if is_obsolete:
            continue
        digraph.add_node(n['id'], attr_dict=n)
    for e in og['edges']:
        digraph.add_edge(e['sub'], e['obj'], pred=e['pred'])


def convert_json_string(obographstr):
    """
    Return a networkx MultiDiGraph of the ontologies
    serialized as a json string

    """
    return convert_json_object(json.loads(obographstr))

def convert_json_file(obographfile):
    """
    Return a networkx MultiDiGraph of the ontologies
    serialized as a json string

    """
    f = open(obographfile, 'r')
    jsonstr = f.read()
    f.close()
    return convert_json_string(jsonstr)

def convert_json_object(obographdoc):
    """
    Return a networkx MultiDiGraph of the ontologies
    serialized as a json object

    """

    
    digraph = networkx.MultiDiGraph()
    labeldict = {}
    for og in obographdoc['graphs']:
        add_obograph_digraph(og, digraph, labeldict)

    return digraph

