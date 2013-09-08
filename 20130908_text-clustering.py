# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/1789254/clustering-text-in-python
"""

import sys
from math import log, sqrt
from itertools import combinations

def cosine_distance(a, b):
    cos = 0.0
    a_tfidf = a["tfidf"]
    for token, tfidf in b["tfidf"].iteritems():
        if token in a_tfidf:
            cos += tfidf * a_tfidf[token]
    return cos

def normalize(features):
    norm = 1.0 / sqrt(sum(i**2 for i in features.itervalues()))
    for k, v in features.iteritems():
        features[k] = v * norm
    return features

def add_tfidf_to(documents):
    tokens = {}
    for id, doc in enumerate(documents):
        tf = {}
        doc["tfidf"] = {}
        doc_tokens = doc.get("tokens", [])
        for token in doc_tokens:
            tf[token] = tf.get(token, 0) + 1
        num_tokens = len(doc_tokens)
        if num_tokens > 0:
            for token, freq in tf.iteritems():
                tokens.setdefault(token, []).append((id, float(freq) / num_tokens))

    doc_count = float(len(documents))
    for token, docs in tokens.iteritems():
        idf = log(doc_count / len(docs))
        for id, tf in docs:
            tfidf = tf * idf
            if tfidf > 0:
                documents[id]["tfidf"][token] = tfidf

    for doc in documents:
        doc["tfidf"] = normalize(doc["tfidf"])

def choose_cluster(node, cluster_lookup, edges):
    new = cluster_lookup[node]
    if node in edges:
        seen, num_seen = {}, {}
        for target, weight in edges.get(node, []):
            seen[cluster_lookup[target]] = seen.get(
                cluster_lookup[target], 0.0) + weight
        for k, v in seen.iteritems():
            num_seen.setdefault(v, []).append(k)
        new = num_seen[max(num_seen)][0]
    return new

def majorclust(graph):
    cluster_lookup = dict((node, i) for i, node in enumerate(graph.nodes))

    count = 0
    movements = set()
    finished = False
    while not finished:
        finished = True
        for node in graph.nodes:
            new = choose_cluster(node, cluster_lookup, graph.edges)
            move = (node, cluster_lookup[node], new)
            if new != cluster_lookup[node] and move not in movements:
                movements.add(move)
                cluster_lookup[node] = new
                finished = False

    clusters = {}
    for k, v in cluster_lookup.iteritems():
        clusters.setdefault(v, []).append(k)

    return clusters.values()

def get_distance_graph(documents):
    class Graph(object):
        def __init__(self):
            self.edges = {}

        def add_edge(self, n1, n2, w):
            self.edges.setdefault(n1, []).append((n2, w))
            self.edges.setdefault(n2, []).append((n1, w))

    graph = Graph()
    doc_ids = range(len(documents))
    graph.nodes = set(doc_ids)
    for a, b in combinations(doc_ids, 2):
        graph.add_edge(a, b, cosine_distance(documents[a], documents[b]))
    return graph

def get_documents():
    texts = [
        "A power law is a functional relationship between two quantities where one quantity varies as a power of another For instance the number of cities having a certain population size is found to vary as a power of the size of the population Empirical powerlaw distributions hold only approximately or over a limited range",
        "Pink noise is a signal or process with a frequency spectrum such that the power spectral density is inversely proportional to the frequency In pink noise each octave carries an equal amount of noise power The name arises from the pink appearance of visible light with this power spectrum",
        "In stochastic processes chaos theory and time series analysis detrended fluctuation analysis is a method for determining the statistical selfaffinity of a signal It is useful for analysing time series that appear to be longmemory processes The obtined exponent is similar to the Hurst exponent except that DFA may also be applied to signals whose underlying statistics or dynamics are nonstationary It is related to measures based upon spectral techniques such as autocorrelation and Fourier transform Peng et al introduced DFA in 1994 in a paper that has been cited over 2000 times as of 2013 and represents an extension of the ordinary fluctuation analysis FA which is affected by nonstationarities",
        "The Abelian sandpile model also known as the Bak Tang Wiesenfeld model was the first discovered example of a dynamical system displaying selforganized criticality It was introduced by Per Bak Chao Tang and Kurt Wiesenfeld in a 1987 paper The model is a cellular automaton In its original formulation each site on a finite grid has an associated value that corresponds to the slope of the pile This slope builds up as grains of sand are randomly placed onto the pile until the slope exceeds a specific threshold value at which time that site collapses transferring sand into the adjacent sites increasing their slope Bak Tang and Wiesenfeld considered process of successive random placement of sand grains on the grid; each such placement of sand at a particular site may have no effect or it may cause a cascading reaction that will affect many sites These avalanches are an example of the Eden growth model The model has since been studied on the infinite lattice on other nonsquare lattices and on arbitrary graphs",
        "In physics mathematics statistics and economics scale invariance is a feature of objects or laws that does not change if scales of length energy or other variables are multiplied by a common factor The technical term for this transformation is a dilatation and the dilatations can also form part of a larger conformal symmetry",
        "Sonny John Moore better known by his stage name Skrillex is an American electronic musician and singersongwriter Growing in Northeast Los Angeles and in Northern California Sonny Moore joined the American posthardcore band From First to Last as the lead singer in 2004 and recorded two studio albums with the band before leaving to pursue a solo career in 2007 He began his first tour as a solo artist in late 2007 After recruiting a new band lineup Moore joined the Alternative Press Tour to support bands such as All Time Low and The Rocket Summer and appeared on the cover of Alternative Press annual 100 Bands You Need to Know issue",
    ]  
    return [{"text": text, "tokens": text.split()}
             for i, text in enumerate(texts)]

def main(args):
    documents = get_documents()
    add_tfidf_to(documents)
    dist_graph = get_distance_graph(documents)

    for cluster in majorclust(dist_graph):
        print "========="
        for doc_id in cluster:
            print documents[doc_id]["text"]

if __name__ == '__main__':
    main(sys.argv)
