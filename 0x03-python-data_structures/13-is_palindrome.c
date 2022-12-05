#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list
 * is palindromic
 * @head: pointer to head node
 * Return: 1 true 0 false
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int array[10240], size = 0, n = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (temp)
	{
		temp = temp->next;
		size += 1;
	}
	if (size == 1)
		return (1);
	temp = *head;
	while (temp)
	{
		array[n++] = temp->n;
		temp = temp->next;
	}
	for (n = 0; n < size / 2; n++)
	{
		if (array[n] != array[size - 1 - n])
			return (0);
	}
	return (1);
}

