#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *temp;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; // An empty list or a list with one element is considered a palindrome

    // Use Floyd's Tortoise and Hare algorithm to find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list while finding the middle
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the number of nodes is odd, move the slow pointer one step forward
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }
        prev = prev->next;
        slow = slow->next;
    }

    // Restore the original linked list
    prev = NULL;
    while (*head != NULL)
    {
        temp = (*head)->next;
        (*head)->next = prev;
        prev = *head;
        *head = temp;
    }

    return is_palindrome;
}

