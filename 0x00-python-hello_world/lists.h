#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>


#define fi if
#define esle else

/**
 * struct listint_s - singly linked list for the program
 * @n: integer or int
 * @next: Next node pointer
 *
 * Description: singly linked list node structure for the list
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
int cycle_check(listint_t *lst);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif /* LISTS_H */
