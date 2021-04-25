#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) {
	Node *temp= (Node *)malloc(sizeof(Node));
	temp->data=data;
	temp->link=NULL;
	Node *New =list->head;
	if(list->head==NULL)
    {
        list->head=temp;
        return;
    }
    while(New->link!=NULL)
        New=New->link;
    New->link=temp;
    return;
}

void list_delete_front(List* list) {
  Node *temp=list->head;
  list->head=temp->link;
  free(temp);
}

void list_insert_at (List *list, int data, int position)
{
    Node *temp,*prev,*a;
    int i = 1;
    temp =  (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->link = NULL;
    a = list->head;
    prev = NULL;
    while((a!=NULL)&&(i<position))
    {
       prev = a;
       a = a->link;
       ++i;
    }
    if(a!=NULL)
    {
    if(prev==NULL)
    {
       temp->link = list->head;
       list->head = temp;
    }
    else
    {
      prev->link = temp;
      temp->link = a;
    }
    }
    else
    {
      if(i==position)
        prev->link = temp;
    }
}

void list_reverse(List* list)
{
 	Node *prev,*temp,*current;
    prev = NULL;
    current = list->head;
    while(current!=NULL)
    {
    temp = current->link;
    current->link = prev;
    prev = current;
    current = temp;
    }
    list->head = prev;
}


