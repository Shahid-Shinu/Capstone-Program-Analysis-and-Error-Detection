#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) 
{
    struct Node *new_node = malloc(sizeof(struct Node));//node to store the data
    new_node->data = data;
    new_node->link = NULL;

    if (list->head == NULL) // insert at sart if list is empty 
	{
        list->head = new_node;
    }
    struct Node* temp = list->head;
    while (temp->link != NULL) // traverse to end of linked list 
	{
        temp = temp->link;
    }
    temp->link = new_node;//making last node in list to point to the new node
    list->number_of_nodes++; 
}


void list_delete_front(List* list) 
{
    if (list->head != NULL) // check if list is empty
	{
        struct Node* rem = list->head;// pointer to head node as it is to  be removed 
        list->head = rem->link;
        list->number_of_nodes --;
    }
}

void list_insert_at (List *list, int data, int position) 
{

    if (position == 0) // check if node should be inserted at the beginning
	{
        struct Node *new_node = malloc(sizeof(struct Node));
        new_node->data = data;
        new_node->link = list->head;
        list->head = new_node;
        list->number_of_nodes += 1;
    }

    else if (position <= list->number_of_nodes) 
	{
        struct Node* new_node = malloc(sizeof(struct Node));
        new_node->data = data;
        struct Node* prev = list->head;
        for (int i = 0; i <= position; i++)// traverse to deired position
		 {
            if (i == position - 1 ) // stops at the node previous to required position
			{
                new_node->link = prev->link;
                prev->link = new_node;// makes the previous node point the new node
                list->number_of_nodes += 1;
            }
            prev = prev->link;
        }
    }

}

void list_reverse(List* list) 
{ 
    struct Node* prev = NULL; 
    struct Node* cur = list->head; 
    struct Node* next = NULL; 
    while (cur != NULL) 
	{ 
        next = cur->link; //point to next  node
        cur->link = prev; //make current node point to previous 
        prev = cur; // made to point to current node
        cur = next; //move to next node 
    } 
    list->head = prev; // assign head to the last node effectively reversing the list
}