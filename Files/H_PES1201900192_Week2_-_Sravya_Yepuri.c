#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) {
	Node *temp, *new;
	new = (Node *)malloc(sizeof(Node));
	new->data=data;
	new->link=NULL;
	if (list->head==NULL){
		list->head = new;
		list->number_of_nodes++;
	}
	else{
		temp = list->head;
		while(temp->link!=NULL)
			temp=temp->link;
		temp->link=new;
		list->number_of_nodes++;
	}
	return;
}

void list_delete_front(List* list) {
	Node *temp;
	if(list->head==NULL)
		return;
	else{
		temp=list->head;
		list->head=(list->head)->link;
		list->number_of_nodes--;
		return;
	}
	free(temp);
}

void list_insert_at (List *list, int data, int position)
{
	Node *temp, *prev, *new;
	int i=0;
	new = (Node *)malloc(sizeof(Node));
	new->data=data;
	new->link=NULL;
	if(list->head==NULL){
		list->head = new;
		list->number_of_nodes++;
	}
	else if(position==0){
		new->link=list->head;
		list->head=new;
		list->number_of_nodes++;
	}
	else{
		temp = list->head;
		while(temp->link!=NULL && i<position){
			prev = temp;
			temp = temp->link;
			i++;
		}
		if (i==position){
			new->link=prev;
			prev->link=new;
			list->number_of_nodes++;
		}
		else if(++i==position){
			temp->link=new;
			list->number_of_nodes++;
		}
		else
			return;
	}

}

void list_reverse(List* list)
{
	Node *prev, *temp, *curr;
	prev = NULL;
	curr=list->head;
	while(curr!=NULL){
		temp=curr->link;
		curr->link=prev;
		prev=curr;
		curr=temp;
	}
	list->head=prev;
}
	

