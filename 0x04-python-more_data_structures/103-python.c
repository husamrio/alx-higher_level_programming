#include <Python.h>

/**
* print_python_bytes - Prints basic information about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
unsigned char i, size;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes"))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)p)->ob_size > 10)
size = 10;
else
size = ((PyVarObject *)p)->ob_size + 1;

printf("  first %d bytes: ", size);
i = 0;
while (i < size)
{
printf("%02hhx%s", bytes->ob_sval[i], i == size - 1 ? "\n" : " ");
i++;
}
}

/**
* print_python_list - Prints basic information about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
int size, alloc, i;
const char *type;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

size = var->ob_size;
alloc = list->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

i = 0;
while (i < size)
{
type = list->ob_item[i]->ob_type->tp_name;
printf("Element %d: %s\n", i, type);
if (!strcmp(type, "bytes"))
print_python_bytes(list->ob_item[i]);
i++;
}
}
