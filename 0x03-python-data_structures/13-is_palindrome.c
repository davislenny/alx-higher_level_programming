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
	listint_t *tmp = *head;
	int nodes = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp)
	{
		nodes++;
		tmp = tmp->next;
	}
	array = malloc(sizeof(int) * nodes);
	tmp = *head;
	while (tmp)
	{
		array[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (array[i] != array[nodes - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
