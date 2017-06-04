import llvmlite.binding as llvm

mod = llvm.parse_assembly("curl-7.54.0/src/.libs/curl.0.4.opt.bc")
mod.verify()
for func in mod.functions:
  print llvm.get_function_cfg(func)
