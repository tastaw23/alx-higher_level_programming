#include <Python.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    size_t i;
    for (i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (size_t i = 0; i < PyList_Size(p); ++i) {
        printf("Element %zd: ", i);

        PyObject *elem = PyList_GetItem(p, i);

        if (PyBytes_Check(elem)) {
            printf("bytes\n");
            print_python_bytes(elem);
        } else if (PyLong_Check(elem)) {
            printf("int\n");
        } else if (PyFloat_Check(elem)) {
            printf("float\n");
        } else if (PyTuple_Check(elem)) {
            printf("tuple\n");
        } else if (PyList_Check(elem)) {
            printf("list\n");
            print_python_list(elem);
        } else if (PyUnicode_Check(elem)) {
            printf("str\n");
        } else {
            printf("[ERROR] Invalid Element\n");
        }
    }
}


