#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node * next;
};

void insertion(struct node ** ptr,int value)
{
    struct node * newnode=(struct node *)malloc(sizeof(struct node));

    if(newnode==NULL)
    {
        printf("memory allocation failed");
        return;
    }

    newnode->data=value;
    newnode->next=NULL;

    struct node * temp=*ptr;

    if((*ptr)==NULL)
    {
        (*ptr)=newnode;
        return;
    }
    else{

    while((temp)->next!=NULL)
    {
        temp=(temp)->next;
    }
    temp->next=newnode;
}

}


void printLl(struct node * ptr)
{
    struct node * temp=ptr;
    while(temp!=NULL)
    {
        printf("%d->",temp->data);
        temp=temp->next;
    }
}

void evenoddCount(struct node * ptr){
    struct node * even=NULL;
    struct node * odd=NULL;

    struct node *temp=ptr;

    while(temp!=NULL){
    if(temp->data%2==0){
        insertion(&even,temp->data);
       
    }
    else{
         insertion(&odd,temp->data);
    }
    temp=temp->next;
}

printf("\n the even eliment:");
printLl(even);

printf("\n the odd eliment:");
printLl(odd);

}

void freeList(struct node *head) {
    struct node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}


int main()
{
    struct node * first=(struct node *)malloc(sizeof(struct node));
    struct node * sec=(struct node *)malloc(sizeof(struct node));
    struct node * third=(struct node *)malloc(sizeof(struct node));
    struct node * fourth=(struct node *)malloc(sizeof(struct node));
    struct node * fifth=(struct node *)malloc(sizeof(struct node));

    struct node * head=first;

    first->data=34;
    first->next=sec;

    sec->data=39;
    sec->next=third;

    third->data=19;
    third->next=fourth;

    fourth->data=30;
    fourth->next=fifth;

    fifth->data=9;
    fifth->next=NULL;

    printLl(head);
    evenoddCount(head);

    freeList(head);

    return 0;
}