#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list
 * is palindromic
 * @head: pointer to head node
 * Return: 1 true 0 false
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	ssize_t size = 0;
	int *array, n = 0;

	if (!head)
		return (0);
	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		array[n] = temp->n;
		temp = temp->next;
		size += 1;
		n++;
	}

	for (n = 0; n <= (size / 2); n++)
	{
		if (array[n] != array[size - n - 1])
			return (0);
	}
	return (1);
}
