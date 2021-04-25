#include<stdio.h>
#include<stdlib.h>
#include "sll.h"

void insert_at_end(List *list, int data) {
	//Create a new node to be inserted by allocating memory
	struct Node *temp;
	temp=(struct Node*)malloc(sizeof(Node));

	//Initialize temp variable 
	temp->data=data;
	temp->link=NULL;
	
	//Check if list is empty i.e head points to NULL 
	if(list->head==NULL)
		list->head=temp; 

	//If list empty then make the node to be interted first node of the list	
	else
	{
		struct Node* q; //Temporary node created to traverse through list
		q=list->head;   //Contains head data from list struct
		while(q->link!=NULL) //If link of node is NULL , then it is last node
			q=q->link;
		q->link=temp;	//link new node to previous node 
	}
}

void list_delete_front(List* list) {
	//Temporary node to store the location of head node and delete element 
	struct Node*q;
	q=list->head;
	list->head=q->link;
	free(q);	
}

void list_insert_at (List *list, int data, int position)
{
	struct Node *prev,*temp,*q;
	// Previous node keeps track of node behind the current node 
	//Temp node contains data for new node to be inserted 
	//q contains the information for head memory location and helps traverse through the linked list
	//i keeps a check on the position i.e ith element of the list 

	//INITIALIZATION
	int i=0; 
	q=list->head;
	prev=NULL;

	//Memeory allocation for temp variable 
	temp=(struct Node*)malloc(sizeof(Node));
	temp->data=data;
	temp->link=NULL;

	//Traverse through the list to reach required position 
	while((q!=NULL)&&(i<position))
	{
		prev=q;
		q=q->link;
		i++;
	}
	//Stops at one position before the required position 
	//Node has to be inserted between prev and q 
	if(q!=NULL) //POSITION FOUND 
	{
		if(prev==NULL) //First node in list 
		{
			temp->link=list->head; //Change position of head node 
			list->head=temp;       
		}
		else 		//Middle of the list  
		{
			prev->link=temp; 
			temp->link=q;
		}
	}
	else if(q==NULL) //insertion at the end of list 
	{
		if(i==position) //position is valid 
			prev->link=temp;
		else
		{
			//INVALID POSITION
		}		
	}
}

void list_reverse(List* list)
{
	//prev to store memory location of node before the current node
	//q is used to traverse through the list 
	//next is to store memory location of node after current node 

 	struct Node* previous=NULL;
	struct Node* q=list->head;
	struct Node* next = NULL;

	while(q!=NULL)	//if list is not empty i.e head does not point to NULL
	{
		next=q->link; //store next location 
		q->link=previous; //reverse current node pointer  
		previous=q;
		q=next;
	}
	list->head=previous; //Change location of head node 
}

/* SAMPLE TEST CASE 1:
2
1 10
1 20
1 40
1 50 
2
4 30 2
2
3 
5
2

OUTPUT:
EMPTY 
10 20 40 50
10 20 30 40 50
20 30 40 50
50 40 30 20
*/

