#!/usr/bin/python
import sys
import re
import json

def get_name(content):
    name_index = content.find('gene_name')
    start_index = content.find('"', name_index)
    stop_index = content.find(';', name_index)
    output = content[start_index+1:stop_index-1]
    return output

def get_profile(name, chr, startPos, endPos):
    dict = {}
    dict["geneName"] = name
    dict["chr"] = chr
    dict["startPos"] = int(startPos)
    dict["endPos"] = int(endPos)
    return dict

with open(sys.argv[1], 'r') as f:
    all_genes = []
    for line in f:
        l = re.split(r'\t+', line.rstrip('\t'))
        if (len(l) > 1):
            if (l[2] == "gene"):
                gene_name = get_name(l[8])
                gene_profile = get_profile(gene_name, l[0], l[3], l[4])
                all_genes.append(gene_profile)
    with open('data.txt', 'w') as outfile:
	json.dump(all_genes, outfile)
