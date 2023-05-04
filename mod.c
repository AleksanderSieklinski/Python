
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

static PyObject* met(PyObject* self, PyObject* args)
{
    //jezeli jednym z argumentow jest lista, to sumujemy jej elementy i dodajemy do sumy pozostale argumenty
    //jezeli nie ma listy, to sumujemy wszystkie argumenty
    int sum = 0;
    size_t n = PyTuple_Size(args);
    for(int i=0;i<n;i++)
    {
        PyObject* item = PyTuple_GetItem(args,i);
        if(PyList_Check(item))
        {
            size_t m = PyList_Size(item);
            for(int j=0;j<m;j++)
            {
                PyObject* item2 = PyList_GetItem(item,j);
                if(PyLong_Check(item2))
                {
                    sum += PyLong_AsLong(item2);
                }
            }
        }
        else if(PyLong_Check(item))
        {
            sum += PyLong_AsLong(item);
        }
    }
    return Py_BuildValue("i",sum);
}

static PyObject* insertion_sort(PyObject* self, PyObject* args)
{
    PyObject* list;
    if(!PyArg_ParseTuple(args,"O",&list))
    {
        return NULL;
    }  
    size_t n = PyList_Size(list);
    int* tab = malloc(sizeof(int)*n);
    for(int i=0;i<n;i++)
    {
        PyObject* item = PyList_GetItem(list,i);
        if(PyLong_Check(item))
        {
            tab[i] = PyLong_AsLong(item);
        }
    }
    for(int i=1;i<n;i++)
    {
        int key = tab[i];
        int j = i-1;
        while(j>=0 && key<tab[j])
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = key;
    }
    PyObject* result = PyList_New(n);
    for(int i=0;i<n;i++)
    {
        PyList_SetItem(result,i,PyLong_FromLong(tab[i]));
    }
    free(tab);
    return result;
}

static PyObject* Euclid(int a, int b)
{
    if(b==0)
    {
        return PyLong_FromLong(a);
    }
    else
    {
        return Euclid(b,a%b);
    }
}

static PyObject* gcd(PyObject* self, PyObject* args)
{
    PyObject* dict;
    if(!PyArg_ParseTuple(args,"O",&dict))
    {
        return NULL;
    }
    PyObject* result = PyDict_New();
    PyObject* keys = PyDict_Keys(dict);
    size_t n = PyList_Size(keys);
    for(int i=0;i<n;i++)
    {
        PyObject* key = PyList_GetItem(keys,i);
        PyObject* value = PyDict_GetItem(dict,key);
        if(PyLong_Check(key) && PyLong_Check(value))
        {
            PyObject* gcd = Euclid(PyLong_AsLong(key),PyLong_AsLong(value));
            PyDict_SetItem(result,key,gcd);
        }
    }
    return result;
}

static PyMethodDef mod_methods[] = {
    {"met",met,METH_VARARGS,""},
    {"insertion_sort",insertion_sort,METH_VARARGS,""},
    {"gcd",gcd,METH_VARARGS,""},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "mod",
    "",
    -1,
    mod_methods
};

PyMODINIT_FUNC PyInit_mod(void)
{
    return PyModule_Create(&mod_module);
}
