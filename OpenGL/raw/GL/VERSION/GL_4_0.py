'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_4_0'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_4_0',False)
_p.unpack_constants( """GL_SAMPLE_SHADING 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE 0x8C37
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET 0x8E5F
GL_TEXTURE_CUBE_MAP_ARRAY 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY 0x900F""", globals())
@_f
@_p.types(None,_cs.GLfloat)
def glMinSampleShading( value ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBlendEquationi( buf,mode ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparatei( buf,modeRGB,modeAlpha ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendFunci( buf,src,dst ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBlendFuncSeparatei( buf,srcRGB,dstRGB,srcAlpha,dstAlpha ):pass
