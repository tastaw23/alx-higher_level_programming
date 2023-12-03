#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
static listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *temp;

	while (head != NULL)
	{
		temp = head->next;
		head->next = prev;
		prev = head;
		head = temp;
	}

	return prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: first list
 * @list2: second list
 * Return: 1 if lists are equal, 0 otherwise
 */
static int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;
		list1 = list1->next;
		list2 = list2->next;
	}

	return 1;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *first_half, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* An empty list or a list with one element is considered a palindrome */

	/* Use Floyd's Tortoise and Hare algorithm to find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	second_half = reverse_list(slow);

	/* Compare the reversed second half with the first half */
	first_half = *head;
	return (compare_lists(first_half, second_half));
}

