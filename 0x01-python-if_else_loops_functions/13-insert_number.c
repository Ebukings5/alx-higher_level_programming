#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert number to a sorted singly linked
 * @head: pointer to pointer of first node
 * @number: interger to include in new node
 *
 * Return: Address or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new, *prev;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	new = *head;
	prev = NULL;

	while (new != NULL && new->n < number)
	{
		prev = new;
		new = new->next;
	}
	if (prev == NULL)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		prev->next = node;
		node->next = new;
	}
	return (node);
}
