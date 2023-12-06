#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", ((PyVarObject *)p)->ob_size);
    
    // Print the string representation using a loop
    printf("  trying string: ");
    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; ++i) {
        printf("%c", ((PyBytesObject *)p)->ob_sval[i]);
    }
    printf("\n");

    printf("  first 10 bytes: ");
    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    Py_ssize_t limit = (size > 10) ? 10 : size;

    for (Py_ssize_t i = 0; i < limit; ++i) {
        printf("%02x ", (unsigned char)(((PyBytesObject *)p)->ob_sval[i]));
    }
    printf("\n");
}

