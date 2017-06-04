import llvmlite.binding as llvm
import pygraphviz
import networkx

mod = llvm.parse_bitcode(open("curl-7.54.0/src/.libs/curl.0.4.opt.bc", 'r').read())
mod.verify()
graph = ""
for func in mod.functions:
  graph += llvm.get_function_cfg(func)
graph2 = pygraphviz.AGraph(graph)
graph3 = networkx.Graph(graph2)
networkx.draw(graph3)
