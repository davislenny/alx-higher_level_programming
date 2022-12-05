#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list
 * is palindromic
 * @head: pointer to head node
 * Return: 1 true 0 false
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	unsigned int size = 0, n = 0;
	int *array; 

	if (!head)
		return (0);
	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		temp = temp->next;
		size += 1;
	}

	while (temp)
	{
		array[n++] = temp->n;
		temp = temp->next;
	}

	for (n = 0; n <= (size / 2); n++)
	{
		if (array[n] != array[size - n - 1])
			return (0);
	}
	return (1);
}
