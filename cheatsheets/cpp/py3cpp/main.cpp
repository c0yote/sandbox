#include <iostream>

#include <Python.h>

int main(int argc, char *argv[]) {
  std::cout << "C++!" << std::endl;
  
  wchar_t *app = Py_DecodeLocale(argv[0], NULL);
  if (app == NULL) {
    std::cerr << "Fatal error: cannot decode argv[0]\n";
    exit(1);
  }
  Py_SetProgramName(app);
  Py_Initialize();
  
  FILE* pf = fopen("file.py", "r");
  PyRun_AnyFile(pf, "file.py");
  
  if(Py_FinalizeEx() < 0) {
    exit(120);
  }
  PyMem_RawFree(app);
  return 0;
}