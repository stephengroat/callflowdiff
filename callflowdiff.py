import llvmlite

mod = llvm.parse_assembly("curl-7.54.0/src/.libs/curl.0.4.opt.bc")
mod.verify()
for func in mod.functions:
  print llvmlite.binding.get_function_cfg(func)
