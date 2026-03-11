#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node * next;
};
void linkedLIst(struct node * ptr){

    while (ptr!=NULL)
    {
        printf("eliment : %d\n",ptr -> data);
        ptr=ptr -> next;
    }
}
int main()
{
    struct node * head;
    struct node * second;
    struct node * third;
    struct node * fourth;
    
    head=(struct node *)malloc(sizeof(struct node));
    second=(struct node *)malloc(sizeof(struct node));
    third=(struct node *)malloc(sizeof(struct node));
    fourth=(struct node *)malloc(sizeof(struct node));

    head -> data=8;
    head -> next=second;

    second -> data=10;
    second -> next=third;

    third -> data=18;
    third -> next=fourth;

    fourth -> data=8;
    fourth -> next=NULL;

    linkedLIst(head);
    
    return 0;
}
