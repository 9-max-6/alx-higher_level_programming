#include "lists.h"
#include <stddef.h>
/**
 * insert_node - Adds a number into an ordered singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to be added
 * Return: A pointer to the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}