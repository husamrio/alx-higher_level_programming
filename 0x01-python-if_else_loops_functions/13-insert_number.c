#include "lists.h"

/**
 * insert_node - Allocates and inserts a node into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: Data for the new node
 * Return: Address of the new node, or NULL if failed
 * *****
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new_node = NULL;

	if (!head)
		return (NULL);

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/* If the linked list is empty, insert the node as the only member */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	/* If there is only one node in the linked list, compare and insert */
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_node->n)
			(*head)->next = new_node;
		else
		{
			new_node->next = *head;
			*head = new_node;
		}
		return (new_node);
	}

	/* If there are multiple nodes in the linked list, compare and insert */
	current = *head;
	while (current->next != NULL)
	{
		/* If the new node's number is smaller than the first node, insert */
		if (new_node->n < current->n)
		{
			new_node->next = current;
			*head = new_node;
			return (new_node);
		}
		/* If the new node's number is the same as an existing node or falls between two nodes, insert */
		if (((new_node->n > current->n) && (new_node->n < (current->next)->n)) ||
		    (new_node->n == current->n))
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}

	/* If the new node is the greatest and was never inserted, insert it now */
	current->next = new_node;
	return (new_node);
}
