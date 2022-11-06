打つコマンド
python setup.py install
pip freeze
python hello.py

ターミナルの反応

PS C:\Users\nowas\OneDrive - 同志社大学\ドキュメント\生産システム研究室\program\python_C_Api> python setup.py install
running install
running build
running build_ext
building 'myModule' extension
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\bin\HostX86\x86\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -IC:\Users\nowa
s\AppData\Local\Programs\Python\Python38-32\include -IC:\Users\nowas\AppData\Local\Programs\Python\Python38-32\include "-IC:\Program Files (x86)\Microsoft Visual 
Studio\2019\Community\VC\Tools\MSVC\14.24.28314\ATLMFC\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\include
" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\shared" "-IC:\Program Files 
(x86)\Windows Kits\10\include\10.0.18362.0\um" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\winrt" "-IC:\Program Files (x86)\Windows Kits\10\inc
lude\10.0.18362.0\cppwinrt" /EHsc /Tppy_hello.cpp /Fobuild\temp.win32-3.8\Release\py_hello.obj
py_hello.cpp
creating C:\Users\nowas\OneDrive - 同志社大学\ドキュメント\生産システム研究室\program\python_C_Api\build\lib.win32-3.8
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\bin\HostX86\x86\link.exe /nologo /INCREMENTAL:NO /Lpy_hello.cpp
creating C:\Users\nowas\OneDrive - 同志社大学\ドキュメント\生産システム研究室\program\python_C_Api\build\lib.win32-3.8C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\bin\HostX86\x86\link.exe /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO /LIBPATH:C:\Users\nowas\AppData\Local\Programs\Python\Python38-32\libs /LIBPATH:C:\Users\nowas\AppData\Local\Programs\Python\Python38-32\PCbuild\win32 "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\ATLMFC\lib\x86" "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.24.28314\lib\x86" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0\ucrt\x86" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0\um\x86" /EXPORT:PyInit_myModule build\temp.win32-3.8\Release\py_hello.obj /OUT:build\lib.win32-3.8\myModule.cp38-win32.pyd /IMPLIB:build\temp.win32-3.8\Release\myModule.cp38-win32.lib
   ライブラリ build\temp.win32-3.8\Release\myModule.cp38-win32.lib とオブジェクト build\temp.win32-3.8\Release\myModule.cp38-win32.exp を作
成中コード生成しています。
コード生成が終了しました。
running install_lib
copying build\lib.win32-3.8\myModule.cp38-win32.pyd -> C:\Users\nowas\AppData\Local\Programs\Python\Python38-32\Lib\site-packages
running install_egg_info
Writing C:\Users\nowas\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\myModule-1.0.0-py3.8.egg-info

PS C:\Users\nowas\OneDrive - 同志社大学\ドキュメント\生産システム研究室\program\python_C_Api> pip freeze
astroid==2.3.3
asttokens==2.0.5
autopep8==1.4.4
backcall==0.2.0
colorama==0.4.1
cycler==0.11.0
debugpy==1.6.0
decorator==5.1.1
entrypoints==0.4
executing==0.8.3
fonttools==4.32.0
ipykernel==6.13.0
ipython==8.2.0
isort==4.3.21
jedi==0.18.1
jupyter-client==7.2.2
jupyter-core==4.10.0
kiwisolver==1.4.2
lazy-object-proxy==1.4.3
matplotlib==3.5.1
matplotlib-inline==0.1.3
mccabe==0.6.1
myModule==1.0.0
nest-asyncio==1.5.5
numpy==1.22.1
packaging==21.3
parso==0.8.3
pickleshare==0.7.5
Pillow==9.1.0
prompt-toolkit==3.0.29
psutil==5.9.0
pure-eval==0.2.2
pybind11==2.9.2
pycodestyle==2.5.0
Pygments==2.12.0
pylint==2.4.4
pyparsing==3.0.8
python-dateutil==2.8.2
pywin32==303
pyzmq==22.3.0
six==1.13.0
stack-data==0.2.0
tornado==6.1
traitlets==5.1.1
wcwidth==0.2.5
wrapt==1.11.2
xlwings==0.27.3
