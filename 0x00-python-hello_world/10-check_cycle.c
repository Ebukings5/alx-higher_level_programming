#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: pointer to the linked list
 *
 * Return: 1 if cirlce is there else 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
			return(1);

		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
