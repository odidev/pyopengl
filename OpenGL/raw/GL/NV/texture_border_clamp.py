'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_texture_border_clamp'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_texture_border_clamp')
GL_CLAMP_TO_BORDER_NV=_C('GL_CLAMP_TO_BORDER_NV',0x812D)
GL_TEXTURE_BORDER_COLOR_NV=_C('GL_TEXTURE_BORDER_COLOR_NV',0x1004)
