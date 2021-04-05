#include <stdio.h>
#include <stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->link = NULL;

    list->number_of_nodes += 1;
    Node *p = list->head;
    if (list->head == NULL)
    {
        list->head = temp;
        return;
    }
    while (p->link != NULL)
        p = p->link;
    p->link = temp;
    return;
}

void list_delete_front(List *list)
{
    Node *temp = list->head;
    if (list->head == NULL)
    {
        return;
    }
    list->number_of_nodes -= 1;
    list->head = (list->head)->link;
    free(temp);
}

void list_insert_at(List *list, int data, int position)
{
    int count = 0;
    Node *temp, *prev, *newNode;
    prev = NULL;
    temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->link = NULL;

    newNode = list->head;
    while ((newNode != NULL) && (count < position))
    {
        prev = newNode;
        newNode = newNode->link;
        count++;
    }
    if (newNode != NULL)
    {
        if (prev == NULL)
        {
            temp->link = list->head;
            list->head = temp;
        }
        else
        {
            prev->link = temp;
            temp->link = newNode;
        }
    }
    else 
    {
        if (count == position) 
            prev->link = temp;
        else
            return;
    }
    list->number_of_nodes += 1;
}

void list_reverse(List *list)
{
    Node *prev = NULL;
    Node *curr = list->head;
    Node *next = NULL;
    if (curr == NULL)
    {
        return;
    }
    while (curr != NULL)
    {
        next = curr->link;
        curr->link = prev;
        prev = curr;
        curr = next;
    }
    list->head = prev;
}
