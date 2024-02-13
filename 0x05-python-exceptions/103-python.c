#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p) {
    setbuf(stdout, NULL);  // Ensure unbuffered output

    if (PyList_Check(p)) {
        Py_ssize_t size = PyObject_Size(p);
        Py_ssize_t allocated = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *element = PyList_GetItem(p, i);
            const char *type_str = PyObject_Type(element)->tp_name;

            printf("Element %zd: %s\n", i, type_str);

            if (strcmp(type_str, "bytes") == 0) {
                printf("[.] bytes object info\n");
                Py_ssize_t bytes_size = PyObject_Size(element);
                printf("  size: %zd\n", bytes_size);

                if (bytes_size > 10) {
                    bytes_size = 10;
                }

                printf("  trying string: %s\n", PyUnicode_AsUTF8(element));
                printf("  first %zd bytes: ", bytes_size);
                for (Py_ssize_t j = 0; j < bytes_size; j++) {
                    printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
                }
                printf("\n");
            }
        }
    } else {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: PyObject representing a Python float
 */
void print_python_float(PyObject *p) {
    setbuf(stdout, NULL);  // Ensure unbuffered output

    if (PyFloat_Check(p)) {
        double value = PyFloat_AsDouble(p);

        printf("[.] float object info\n");
        printf("  value: %f\n", value);
    } else {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
    }
}

