#ifndef PYTHON_H
#define PYTHON_H

/* Definitions and declarations related to the Python C API */

/* Types */
typedef struct {
    /* ... */
} PyObject;

typedef struct {
    /* ... */
} PyListObject;

/* Functions */
PyObject* PyList_New(int size);
void PyList_SetItem(PyObject* list, int index, PyObject* item);
PyObject* PyLong_FromLong(long value);
PyObject* PyUnicode_FromString(const char* str);

/* Macros */
#define Py_INCREF(obj) /* ... */
#define Py_DECREF(obj) /* ... */

#endif /* PYTHON_H */

