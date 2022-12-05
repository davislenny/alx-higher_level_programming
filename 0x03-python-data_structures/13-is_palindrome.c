#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
	int *array = NULL; 

	if (!head)
		return (0);
	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		temp = temp->next;
		size += 1;
	}
	array = malloc(sizeof(int) * size);
	temp = *head;
	while (temp)
	{
		array[n++] = temp->n;
		temp = temp->next;
	}

	for (n = 0; n <= (size / 2); n++)
	{
		if (array[n] != array[size - n - 1])
			free(array);
			return (0);
	}
	free(array);
	return (1);
}
