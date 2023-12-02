#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *tmp = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }

    // If the list has an odd number of elements, skip the middle one
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (slow != NULL)
    {
        if (slow->n != prev->n)
            return (0);

        slow = slow->next;
        prev = prev->next;
    }

    return (1);
}

