@echo off

:: Builds the module for Windows
setlocal EnableDelayedExpansion
CALL "C:\Program Files\Microsoft SDKs\Windows\v7.0\Bin\SetEnv.cmd" /x64 /release
set DISTUTILS_USE_SDK=1

::  Run the builder and make it in-place
python setup.py build_ext --inplace