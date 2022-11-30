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
	listint_t *new, *temp = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (temp == NULL || temp->n >= new->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp)
	{
		if (temp->next == NULL || temp->n < new->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (temp);
		}
		temp = temp->next;
	}
	return (NULL);
}
