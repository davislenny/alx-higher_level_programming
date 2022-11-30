#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 * @head: first node
 * @number: n list element
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *temp = *head;

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!temp || temp->n >= new->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp && temp->next && temp->next->n < new->n)
			temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
