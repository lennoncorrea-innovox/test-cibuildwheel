#include <pybind11/pybind11.h>

namespace py = pybind11;

float add(float arg1, float arg2){
    return arg1+arg2;
}

PYBIND11_MODULE(addpy_pckg, handle){
    handle.doc() = "Module docs...";
    handle.def("addpy", &add);
}