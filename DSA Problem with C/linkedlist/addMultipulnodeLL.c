#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node * next;
};

struct node * head=NULL;

void addNode(int data )
{
    struct node * newnode=(struct node *)malloc(sizeof(struct node));

    if(newnode==NULL)
    {
        printf("memory is not allocate suceesfully.");
        return;
    }

    newnode->data=data;
    newnode->next=NULL;

    if(head==NULL){
        head=newnode;
        return;
    }

    struct node * temp=head;

    while(temp->next!=NULL)
    {
        temp=temp->next;
    }

    temp->next=newnode;
    // newnode->next=NULL;

}

void displayLinkedlist()
{
    struct node * temp=head;
    if(temp==NULL)
    {
        printf("linked list contain no eliment");
    }
    printf("The linkedlist is:");
    while(temp!=NULL)
    {
        printf(" %d ->",temp->data);
        temp=temp->next;
    }

}

int main()
{
    int data;
    printf("enter integer you want to insert in linkedlist \nput -1 if you want to stop the input:\n");

    while(1){
        printf("Enter data:");
        scanf("%d",&data);

        if(data==-1)
        {
            break;
        }
        addNode(data);

    }
    displayLinkedlist();
    printf(" NULL");
    return 0;
}