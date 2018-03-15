## Dependencies

 * MSVC 14 2015 Build Tools
 * Python 3.x
 
### Build

1. Make a `build` director and change to it.
2. Use one of the following depending on architecture:
```
    cmake -G "Visual Studio 14 2015 Win64" ..
    cmake -G "Visual Studio 14 2015" ..
```
3. Then build:
```
    cmake --build . --config RELEASE
```
4. Run from the directory containing `file.py`.
```
    build\Release\py3cpp.exe
```