
@SET WIN_UCRT_INC="C:\Program Files (x86)\Windows Kits\10\Include\10.0.10150.0\ucrt"
@SET VC_INC="C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include"

@SET WIN_UCRT_LIB="C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10150.0\ucrt\x86"
@SET VC_LIB="C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib"
@SET WIN_LIB="C:\Program Files (x86)\Windows Kits\8.1\Lib\winv6.3\um\x86"

del test.exe
cl.exe test.cpp /I%WIN_UCRT_INC% /I%VC_INC% /link /LIBPATH:%WIN_UCRT_LIB% /LIBPATH:%VC_LIB%  /LIBPATH:%WIN_LIB% 


