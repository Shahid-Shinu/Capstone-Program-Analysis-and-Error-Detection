#include<stdio.h>
#include<stdlib.h>
#include"sll.h"

#include <unistd.h>
#include<fcntl.h>

void init(char **argv)
{
	//printf("%s %s\n", argv[0], argv[1]);
	printf("\n");
	int fd0 = open(argv[0], O_RDONLY);
	if(fd0 == -1)
	{
		perror("open for reading"); exit(1);
	}
	int fd1 = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);
	if(fd1 == -1)
	{
		perror("open for writing"); exit(1);
	}
	
	close(0); dup(fd0);
	close(1); dup(fd1);
}
int main(int argc, char **argv) {
	if(argc > 1) init(argv);
	int choice;

	List* list = list_initialize();
	do {
		scanf("%d", &choice);
		switch(choice) {
			int element, index;
			case 1:
				/*Insert element at the End of the list*/
				scanf("%d", &element);
				insert_at_end(list, element);
				break;
			case 2:
				/* Print list contents */ 
				list_print(list);
				break;
			case 3:
				/* Remove front element */ 
				list_delete_front(list);
				break;
			case 4:
				/* Insert elements at specified positions */
				scanf("%d%d", &element, &index);
				list_insert_at(list, element, index);
				break;
			case 5:
				/*Reverses the elements of the list*/
				list_reverse(list);
				break;
		}
	} while(choice != 0);
	list_destroy(list);
	
	close(1); close(0);
	return 0;
}

List* list_initialize() {
	List* list = (List*) malloc(sizeof(List));
	list->head = NULL;
	list->number_of_nodes = 0;
	return list;
}

void list_print(List* list) 
	{
	int res;
	Node *p;
	p=list->head;
	if(p == NULL)
	{
		res = 0;
		printf("EMPTY\n");
		return;
	}
	while (p!=NULL){
		res = p->data;
		printf("%d ",p->data);
		p=p->link;
	}
	printf("\n");
}


void list_destroy (List *list)
{
	Node *t, *u=NULL;
	t=list->head;
	while (t->link!=NULL){
		u=t;
		t=t->link;
		free(u);
	}
	free(list);
}
