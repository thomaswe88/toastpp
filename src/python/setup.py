from distutils.core import setup, Extension
import os
import sys
from distutils.sysconfig import get_python_inc
import numpy.distutils as npd

toastdir = os.getenv('TOASTDIR')
toastver = os.getenv('TOASTVER')
major = "%d" % sys.version_info[0]
minor = "%d" % sys.version_info[1]
pyinc = get_python_inc(plat_specific=1)
npinc = npd.misc_util.get_numpy_include_dirs()

module1 = Extension('ctoast',
                    include_dirs = [pyinc,
                                    npinc[0],
                                    toastdir,
                                    toastdir+'/include',
                                    toastdir+'/src/libmath',
                                    toastdir+'/src/libfe',
                                    toastdir+'/src/libstoast'],
                    libraries = ['math','fe','stoast'],
                    library_dirs = [toastver+'/lib'],
                    sources = ['toastmodule.cc'])

setup (name = 'ctoast',
       version = '1.0',
       description = 'Python TOAST extension',
       ext_modules = [module1],
       packages = ['toast']
)
