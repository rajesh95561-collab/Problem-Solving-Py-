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


void insertend(struct node ** head,int val)
{
    struct node * newnode=createNewnode(val);

    if(*head==NULL)
    {
        *head=newnode;
        return;
    }
    struct node *temp=*head;

    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;


}

void sorting(struct node * head)
{
    struct node *i;
    struct node *j;
    int temp;

    for(i=head;i!=NULL;i=i->next)
    {
        for(j=i->next;j!=NULL;j=j->next)
        {
            if(i->data > j->data)
            {
                temp=i->data;
                i->data=j->data;
                j->data=temp;
            }

        }
    }
}


void printLL(struct node * head)
{
    if(head==NULL)
    {
        printf("linked list contain no element.");
        return;
    }
    struct node * ptr=head;

    while(ptr!=NULL)
    {
        printf(" %d -> ",ptr->data);
        ptr=ptr->next;
    }
    printf("NULL\n");
}




int main(){

    struct node * head=NULL;

    insertend(&head,19);
    insertend(&head,13);
    insertend(&head,29);
    insertend(&head,1);
    insertend(&head,10);
    insertend(&head,100);
    insertend(&head,35);
    printLL(head);

    printf("after sorting the linked list is:\n");
    sorting(head);
    printLL(head);


    return 0;
}