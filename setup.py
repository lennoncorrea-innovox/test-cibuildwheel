from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import os
import pybind11

# Specify the C++ standard
cpp_args = ['-std=c++17']

# Define the Extension module
extension = Extension(
    'addpy_pckg',  # Name of the module
    sources=['src/main.cpp'],  # Source files
    include_dirs=[pybind11.get_include()],  # Include pybind11 headers
    extra_compile_args=cpp_args,  # Extra compile arguments
    extra_link_args=[],  # Extra link arguments
    language='c++',
)

setup(
    name='addpy_pckg',
    version='0.1.0',
    #author='Your Name',
    #author_email='your.email@example.com',
    description='A Pybind11 project',
    ext_modules=[extension],  # List of extensions to build
    cmdclass={'build_ext': build_ext},  # Custom build_ext class
)
