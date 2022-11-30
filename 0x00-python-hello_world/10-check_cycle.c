#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: 1 in cycle present, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *forward = list, *backwards = list;

	while (forward && forward->next)
	{
		forward = forward->next->next;
		backwards = backwards->next;
		if (forward == backwards)
			return (1);
	}
	return (0);
}
