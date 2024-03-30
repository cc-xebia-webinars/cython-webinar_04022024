#include <stdio.h>
#include <Python.h>

PyObject *create_double_nums(PyObject *self, PyObject *args)
{
    PyObject *list;

    if (!PyArg_ParseTuple(args, "O", &list))
    {
        PyErr_SetString(PyExc_TypeError, "A list argument must be provided.");
        return NULL;
    }

    if (!PyList_Check(list))
    {
        PyErr_SetString(PyExc_TypeError, "Argument must be a list.");
        return NULL;
    }

    Py_ssize_t len = PyList_Size(list);
    PyObject *new_list = PyList_New(len);

    for (Py_ssize_t i = 0; i < len; i++)
    {
        PyObject *item = PyList_GetItem(list, i);
        if (!PyLong_Check(item))
        {
            return NULL;
        }
        long num = PyLong_AsLong(item);
        PyList_SetItem(new_list, i, PyLong_FromLong(num * 2));
    }

    return new_list;
}

static PyMethodDef double_nums_methods[] = {
    {"create_double_nums",
     create_double_nums,
     METH_VARARGS,
     "Double numbers in a list"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef double_nums_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "double_nums",
    .m_doc = "double_nums module",
    .m_size = -1,
    .m_methods = double_nums_methods};

PyMODINIT_FUNC PyInit_double_nums()
{
    return PyModule_Create(&double_nums_module);
}