#include "lists.h"

/**
 * check_cycle - checks for a cycle in a list
 * @list: list to check
 * Return: 1 if cycle found, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
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
