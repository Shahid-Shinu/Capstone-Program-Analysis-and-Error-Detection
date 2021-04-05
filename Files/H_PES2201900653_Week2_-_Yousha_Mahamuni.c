#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) {
	Node *temp,*p;//temp is the new node created. p is used to traverse
    temp=(Node*)malloc(sizeof(Node));//dynamic allocation of memory
    if(temp==NULL) return;//checking if not allocated properly
    if(list->number_of_nodes>999) return;//if n >999, it means already having 1000 nodes, which is out of the constraint
    temp->data=data;//filling info in new node
    temp->link=NULL;
    p=list->head;//used to store the address of headpointer
    if(p==NULL){
        list->head=temp;//if no node, then temp is first node directly
    }
    else{
    while(p->link!=NULL){
        p=p->link;//traverse through 
    }
    p->link=temp;}
    list->number_of_nodes+=1;//added a node

    return;
}

void list_delete_front(List* list) {
	Node *p=list->head;
    if(list->head==NULL) return;
    list->head=p->link;
    list->number_of_nodes-=1;//deleted node
    
    return;
}

void list_insert_at (List *list, int data, int position)
{
	int n;
    n=list->number_of_nodes;
    if(position<0 ||position>n) return;
    if(list->number_of_nodes>999) return;
    Node *temp,*p;
    temp=(Node*)malloc(sizeof(Node));
    if(temp==NULL) return;
    temp->data=data;
    p=list->head;
    if(position==0){
        temp->link=p;
        list->head=temp;
        return;
    }
    for(int i=1;i<position;i++)
    	{
        		p=p->link;
    	}

    	temp->link=p->link;
    	

    	p->link=temp;
        list->number_of_nodes+=1;
    
	}

void list_reverse(List* list)
{ 
	Node *b4 = NULL; 
	Node *current = list->head; 
	Node *link = NULL; 
	while (current != NULL) { 
		link = current->link; 
		current->link = b4; 
		b4 = current; 
		current = link; 
	} 
	list->head = b4; 

} 
 	
