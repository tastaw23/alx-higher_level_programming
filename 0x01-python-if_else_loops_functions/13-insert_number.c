#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    if (head == NULL)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    current = *head;
    prev = NULL;

    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        prev->next = new_node;
        new_node->next = current;
    }

    return (new_node);
}

/* Example usage */
int main(void)
{
    listint_t *head = NULL;

    insert_node(&head, 3);
    insert_node(&head, 1);
    insert_node(&head, 5);

    return 0;
}

