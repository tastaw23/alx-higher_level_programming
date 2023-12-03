#include <Python.h>

/**
 * print_python_list_info - prints basic information about Python lists
 * @p: pointer to a Python object (assumed to be a list)
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (PyList_Check(p))
    {
        size = PyList_Size(p);
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", alloc);

        for (i = 0; i < size; ++i)
        {
            item = PyList_GetItem(p, i);
            printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
    else
    {
        fprintf(stderr, "Invalid Python List\n");
    }
}

// Example usage
int main(void)
{
    Py_Initialize();
    
    // Create a Python list
    PyObject *my_list = PyList_New(3);
    PyList_SetItem(my_list, 0, Py_BuildValue("s", "Hello"));
    PyList_SetItem(my_list, 1, Py_BuildValue("i", 42));
    PyList_SetItem(my_list, 2, Py_BuildValue("f", 3.14));

    // Call the function to print information about the list
    print_python_list_info(my_list);

    // Clean up
    Py_DECREF(my_list);
    Py_Finalize();

    return 0;
}

