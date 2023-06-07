# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:38:08 2022

@author: congc
"""

graph = {
    "s":["a","c","d"],
    "a":[ ],
    "d":['a','c'],
    "c":['e'],
    "e":['f','g','s'],
    "g":[ ],
    "f":[ ]
    }

def bfs(graph, s):
    queue = []
    queue.append(s)
    # quick search
    seen = set()
    seen.add(s)
    while (len(queue)>0):
        # FIFO
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)
        
bfs(graph, 's')


def dfs(graph, s):
    stack = []
    stack.append(s)
    # quick search
    seen = set()
    seen.add(s)
    while (len(stack)>0):
        # LIFO
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)
        
        
dfs(graph, 's')
