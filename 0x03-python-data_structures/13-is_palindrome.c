#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int data[10240];
    int size = 0, i;

    if (!head || !*head)
        return (1);

    while (temp)
    {
        data[size++] = temp->n;
        temp = temp->next;
    }

    for (i = 0; i < size / 2; i++)
        if (data[i] != data[size - i - 1])
            return (0);

    return (1);
}
