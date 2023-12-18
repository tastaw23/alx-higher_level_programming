#ifndef PYTHON_H
#define PYTHON_H

/* Define basic types */
typedef struct _object PyObject;
typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
} PyTupleObject;

/* Function declarations from Python API */
PyObject* Py_BuildValue(const char *format, ...);
PyObject* PyDict_New(void);
int PyDict_SetItem(PyObject *p, PyObject *key, PyObject *value);
PyObject* PyTuple_Pack(Py_ssize_t n, ...);

/* Error handling macros */
#define Py_RETURN_NONE return Py_INCREF(Py_None), Py_None
#define Py_XDECREF(op) do { if (op) Py_DECREF(op); } while (0)
#define Py_XINCREF(op) do { if (op) Py_INCREF(op); } while (0)
#define PyErr_Print() fprintf(stderr, "Error occurred\n")

/* Constants */
#define Py_None ((PyObject *)NULL)

#endif /* PYTHON_H */

