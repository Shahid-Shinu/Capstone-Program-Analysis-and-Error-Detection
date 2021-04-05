#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) {
	//TODO
	Node *q;
	q = list->head; //copy location of head into h

	Node *temp;
	temp = (Node*)malloc(sizeof(Node*));
	temp->data = data;
	temp->link = NULL;

	if(q==NULL) //checks if list is empty
	{
		list->head = temp;
	}
	else
	{	
		while(q->link!=NULL)
		{
			q=q->link;
		}
		q->link = temp;
	}
	list->number_of_nodes++;
}

void list_delete_front(List* list) {
	//TODO
	Node *h;
	h = list->head;

	if(h == NULL)
		printf("Empty already\n");
	else
	{	
		list->head = h->link;
	}
	free(h);
	list->number_of_nodes--;

	// printf("%p test %p", h, list->head);
}

void list_insert_at (List *list, int data, int position)
{
	//TODO
	Node *temp, *q, *prev; //q is iterator
	int count = 0;

	temp = (Node*)malloc(sizeof(Node*));
	temp->data = data;
	temp->link = NULL;

	q = list->head;
	prev = NULL;

	if(position ==0) 
	{
		temp->link = list->head;
		list->head = temp;
	}
	else if(position <= (list->number_of_nodes) && position>0)
	{
		while(q->link != NULL && count != position)
		{
			count++;
			prev = q;
			q = q-> link;
		} //now q is where pos is

		prev->link = temp;
		temp->link = q;
	}

	list->number_of_nodes++;

}

void list_reverse(List* list)
{
	 //TODO
	Node *prev, *curr, *next;
	
	curr = list->head; //location of head of the list copied to current node iterator
	prev = NULL;

	while(curr != NULL)
	{
		next = curr->link; //store next node loc
		curr->link = prev; //link curr node to prev node
		prev = curr; //move prev to curr loc
		curr = next; //move curr one node ahead
	}

	list->head = prev; //make last node the new head 
}


