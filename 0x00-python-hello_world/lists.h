#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @num: integer
 * @next: Next node pointer
 *
 * Description: Singly linked list node structure
 * for Alx project
 */
typedef struct listint_s
{
	int num;
	struct listint_s *next;
} listint_t;

size_t print_list(const listint_t *h);
listint_t *add_node(listint_t **head, const int num);
void free_list(listint_t *head);
int check_cycle_list(listint_t *list);

#endif /* LISTS_H */
