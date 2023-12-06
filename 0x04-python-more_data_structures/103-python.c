#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Python List\n");
        return;
    }

    size = PyObject_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyVarObject *)p)->ob_size);

    for (i = 0; i < size; ++i) {
        item = PySequence_ITEM(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        Py_XDECREF(item);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyObject_HasAttrString(p, "encode")) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    PyObject *encoded_bytes = PyObject_CallMethod(p, "encode", NULL);
    if (encoded_bytes == NULL) {
        fprintf(stderr, "[ERROR] Failed to encode Bytes Object\n");
        return;
    }

    size = PyObject_Size(encoded_bytes);
    str = PyBytes_AsString(encoded_bytes);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; ++i) {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");

    Py_XDECREF(encoded_bytes);
}

int main() {
    // Example usage:
    Py_Initialize();

    // Create a Python list
    PyObject *myList = PyList_New(3);
    PyList_SetItem(myList, 0, PyLong_FromLong(42));
    PyList_SetItem(myList, 1, PyUnicode_FromString("Hello"));
    PyList_SetItem(myList, 2, PyFloat_FromDouble(3.14));

    // Create a Python bytes object
    PyObject *myBytes = PyBytes_FromStringAndSize("PythonBytes", 11);

    // Print info about the Python list and bytes object
    print_python_list(myList);
    print_python_bytes(myBytes);

    // Cleanup
    Py_DECREF(myList);
    Py_DECREF(myBytes);

    Py_Finalize();

    return 0;
}

