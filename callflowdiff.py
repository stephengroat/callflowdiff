import llvmlite.binding as llvm

mod = llvm.parse_bitcode(open("curl-7.54.0/src/.libs/curl.0.4.opt.bc", 'r').read())
mod.verify()
for func in mod.functions:
  print llvm.get_function_cfg(func)
