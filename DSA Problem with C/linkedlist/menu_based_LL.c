#include <stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node * next;
};

struct node * createNewnode(int data)
{
    struct node * newnode=(struct node *)malloc(sizeof(struct node));

    newnode->data=data;
    newnode->next=NULL;
    return newnode;
}

void insertBegining(struct node ** head,int value)
{
    struct node * newnode=createNewnode(value);
    struct node * ptr=(*head);

    if(*head==NULL)
    {
        *head=newnode;
        return;
    }

    newnode->next=ptr;
    (*head)=newnode;
}

void insertend(struct node * head,int val)
{
    struct node * newnode=createNewnode(val);
    struct node *temp=head;

    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;


}

void instrtmiddle(struct node ** head,int index,int val)
{
    struct node * temp=*head;
    struct node *newnode=createNewnode(val);
    
    if(index==1)
    {
        newnode->next=*head;
        *head=newnode;
        return;
    } 
    
    int i=1;
    
    while(i<index-1)
    {
        temp=temp->next;
        i++;
    }
    
    newnode->next=temp->next;
    temp->next=newnode;
    

}

void printLL(struct node * head)
{
    struct node * ptr=head;

    while(ptr!=NULL)
    {
        printf(" %d -> ",ptr->data);
        ptr=ptr->next;
    }
    printf("NULL\n");
}

void freeList(struct node *head) {
    struct node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main(){
int choice, val, index;
struct node *head = NULL;

while (1) {
    printf("\n--- Linked List Menu ---\n");
    printf("1. Insert at Beginning\n");
    printf("2. Insert at End\n");
    printf("3. Insert at Index\n");
    printf("4. Print List\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter value: ");
            scanf("%d", &val);
            insertBegining(&head, val);
            break;
        case 2:
            printf("Enter value: ");
            scanf("%d", &val);
            insertend(head, val);  // Update this to take &head
            break;
        case 3:
            printf("Enter index and value: ");
            scanf("%d %d", &index, &val);
            instrtmiddle(&head, index, val);
            break;
        case 4:
            printLL(head);
            break;
        case 5:
            printf("Exiting...\n");
            freeList(head);
            exit(0);
        default:
            printf("Invalid choice. Try again.\n");
    }
}

    return 0;
}