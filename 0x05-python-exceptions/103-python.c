#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p);

void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *element;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else if (PyFloat_Check(element)) {
            print_python_float(element);
        }
        // Add more checks for other object types if needed
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);

    /* Limit the displayed bytes to the first 10 */
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    str = PyBytes_AsString(p);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", PyFloat_AsDouble(p));
}

int main(void) {
    // Your testing code can go here
    return 0;
}

