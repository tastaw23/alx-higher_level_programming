#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (PyBytes_Check(PyList_GetItem(p, i))) {
            printf("[.] bytes object info\n");
            PyBytesObject *obj = (PyBytesObject *)PyList_GetItem(p, i);
            printf("  size: %ld\n", PyBytes_GET_SIZE(obj));
            printf("  trying string: %s\n", PyBytes_AsString(obj));
            printf("  first 10 bytes: ");
            for (int j = 0; j < 10 && j < PyBytes_GET_SIZE(obj); ++j) {
                printf("%02x ", (unsigned char)obj->ob_sval[j]);
            }
            printf("\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    PyBytesObject *obj = (PyBytesObject *)p;
    printf("  size: %ld\n", PyBytes_GET_SIZE(obj));
    printf("  trying string: %s\n", PyBytes_AsString(obj));
    printf("  first 10 bytes: ");
    for (int i = 0; i < 10 && i < PyBytes_GET_SIZE(obj); ++i) {
        printf("%02x ", (unsigned char)obj->ob_sval[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    PyFloatObject *obj = (PyFloatObject *)p;
    printf("  value: %f\n", obj->ob_fval);
}


