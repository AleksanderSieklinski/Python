#include <Python.h>
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b,c;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "iii|O", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			//s+=d[i];
			s+=PyLong_AsLong(PyList_GetItem(d, i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject* insertion_sort(PyObject* self, PyObject* args)
{
    PyObject* list;
    if(!PyArg_ParseTuple(args,"O",&list))
    {
        return NULL;
    }  
    int n = PyList_Size(list);
    int tab[n];
    for(int i=0;i<n;i++)
    {
        PyObject* item = PyList_GetItem(list,i);
        if(PyLong_Check(item))
        {
            tab[i] = PyLong_AsLong(item);
        }
    }
    #include "insertion.c"
	cinsertion_sort(tab,n);
    PyObject* result = PyList_New(n);
    for(int i=0;i<n;i++)
    {
        PyList_SetItem(result,i,PyLong_FromLong(tab[i]));
    }
    return result;
}

static PyObject* Algorytm_Euklidesa(int a, int b)
{
    if(b==0)
    {
        return PyLong_FromLong(a);
    }
    else
    {
        return Algorytm_Euklidesa(b,a%b);
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
    for(size_t i=0;i<n;i++)
    {
        PyObject* key = PyList_GetItem(keys,i);
        PyObject* value = PyDict_GetItem(dict,key);
        if(PyLong_Check(key) && PyLong_Check(value))
        {
            PyObject* gcd = Algorytm_Euklidesa(PyLong_AsLong(key),PyLong_AsLong(value));
            PyDict_SetItem(result,key,gcd);
        }
    }
    return result;
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"insertion_sort", (PyCFunction)insertion_sort, METH_VARARGS, "Funkcja ..."},
	{"gcd", (PyCFunction)gcd, METH_VARARGS, "Funkcja ..."},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
