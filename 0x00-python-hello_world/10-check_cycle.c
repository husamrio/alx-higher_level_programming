#include "lists.h"

/**
* cycle_check - checks for a cycle in a list of the program
* @lst: list to check
* Return: 1 if cycle found, otherwise 0
*/
int cycle_check(listint_t *lst)
{
listint_t *fast = lst;
listint_t *slow = lst;

if (!lst)
return (0);

while (1)
{
if (fast->next && fast->next->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
else
return (0);
}
}

