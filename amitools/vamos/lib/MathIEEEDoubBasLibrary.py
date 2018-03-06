from amitools.vamos.AmigaLibrary import *
from amitools.vamos.lib.lexec.ExecStruct import LibraryDef
from amitools.vamos.Log import *
from amitools.util.Math import *
from amitools.vamos.Log import log_math
import math


class MathIEEEDoubBasLibrary(AmigaLibrary):
  name = "mathieeedoubbas.library"

  def __init__(self, config):
    AmigaLibrary.__init__(self, self.name, LibraryDef, config)

  def setup_lib(self, ctx):
    AmigaLibrary.setup_lib(self, ctx)

  def IEEEDPFix(self, ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    if arg > Amiga_INT_MAX:
      arg = Amiga_INT_MAX
    elif arg < Amiga_INT_MIN:
      arg = Amiga_INT_MIN
    res = int(arg)
    log_math.info("DPFix(%s) = %s", arg, res)
    return res

  def IEEEDPFlt(self, ctx):
    i = int32(ctx.cpu.r_reg(REG_D0));
    d = float(i)
    log_math.info("DPFlt(%s) = %s", i, d)
    return double_to_regs(d)

  def IEEEDPCmp(self, ctx):
    arg1 = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    arg2 = regs_to_double(ctx.cpu.r_reg(REG_D2),ctx.cpu.r_reg(REG_D3))
    if arg1<arg2:
      res = -1
    elif arg1>arg2:
      res = +1
    else:
      res =  0
    log_math.info("DPCmp(%s, %s) = %s", arg1, arg2, res)
    return res

  def IEEEDPTst(self,ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    if arg < 0.0:
      res =  -1
    elif arg > 0.0:
      res = +1
    else:
      res = 0
    log_math.info("DPTst(%s) = %s", arg, res)
    return res

  def IEEEDPAbs(self,ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    if arg < 0.0:
      res = -arg
    else:
      res = arg
    log_math.info("DPAbs(%s) = %s", arg, res)
    return double_to_regs(res)

  def IEEEDPAdd(self,ctx):
    arg1 = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    arg2 = regs_to_double(ctx.cpu.r_reg(REG_D2),ctx.cpu.r_reg(REG_D3))
    res = arg1 + arg2
    log_math.info("DPAdd(%s, %s) = %s", arg1, arg2, res)
    return double_to_regs(res)

  def IEEEDPSub(self,ctx):
    arg1 = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    arg2 = regs_to_double(ctx.cpu.r_reg(REG_D2),ctx.cpu.r_reg(REG_D3))
    res = arg1 - arg2
    log_math.info("DPSub(%s, %s) = %s", arg1, arg2, res)
    return double_to_regs(res)

  def IEEEDPMul(self,ctx):
    arg1 = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    arg2 = regs_to_double(ctx.cpu.r_reg(REG_D2),ctx.cpu.r_reg(REG_D3))
    res = arg1 * arg2
    log_math.info("DPMul(%s, %s) = %s", arg1, arg2, res)
    return double_to_regs(res)

  def IEEEDPDiv(self,ctx):
    arg1 = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    arg2 = regs_to_double(ctx.cpu.r_reg(REG_D2),ctx.cpu.r_reg(REG_D3))
    if arg2 == 0.0:
      res = float('NaN')
    else:
      res = arg1 / arg2
    log_math.info("DPDiv(%s, %s) = %s", arg1, arg2, res)
    return double_to_regs(res)

  def IEEEDPFloor(self,ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    res = math.floor(arg)
    log_math.info("DPFloor(%s) = %s", arg, res)
    return double_to_regs(res)

  def IEEEDPCeil(self,ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    res = math.ceil(arg)
    log_math.info("DPCeil(%s) = %s", arg, res)
    return double_to_regs(res, force_pos_zero=True)

  def IEEEDPNeg(self,ctx):
    arg = regs_to_double(ctx.cpu.r_reg(REG_D0),ctx.cpu.r_reg(REG_D1))
    res = -arg
    log_math.info("DPNeg(%s) = %s", arg, res)
    return double_to_regs(res)
