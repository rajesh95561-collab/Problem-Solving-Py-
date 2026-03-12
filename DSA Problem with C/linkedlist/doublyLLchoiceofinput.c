#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node * prev;
    struct node * next;
};

struct node * createNewnode(int val)
{
    struct node * newnode=(struct node *)malloc(sizeof(struct node));
    newnode->data=val;
    newnode->next=NULL;
    newnode->prev=NULL;
    return newnode;

}

void insertNewnodeAtbegin(struct node ** head,int val)
{
    struct node * newnode=createNewnode(val);

    if(newnode==NULL)
    {
        printf("memory allocation failid");
        return;
    }

    if((*head)==NULL)
    {
        *head=newnode;
        return;
    }

    struct node * temp=*head;
    temp->prev=newnode;
    newnode->next=temp;
    *head=newnode;
}

void insertatend(struct node** head, int data){

    struct node* temp=*head;
    struct node* newnode=createNewnode(data);
    while (temp->next != NULL){
        temp =temp->next;
    }
    temp->next=newnode;
    newnode->prev=temp;

}
void insertAtPosition(struct node **head, int val, int pos) {
    struct node *newnode = createNewnode(val);
    if (newnode == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    // Insert at beginning
    if (pos == 1) {
        insertNewnodeAtbegin(head, val);
        return;
    }

    struct node *temp = *head;
    int count = 1;

    // Traverse to the node before the desired position
    while (temp != NULL && count < pos - 1) {
        temp = temp->next;
        count++;
    }

    // If position is beyond current length, insert at end
    if (temp == NULL || temp->next == NULL) {
        insertatend(head, val); // Make sure insertatend accepts **head
        return;
    }

    // Insert in the middle
    newnode->next = temp->next;
    newnode->prev = temp;
    temp->next->prev = newnode;
    temp->next = newnode;
}

void deletionAnyNode(struct node ** head,int pos){
    if(*head==NULL){
        printf("linked list is empty");
        return;
    }
    struct node *temp=*head;
    int count=1;
    if(pos==1){
        (*head)=(*head)->next;
        free(temp);
        return;
    }
     while (temp != NULL && count < pos) {
        temp = temp->next;
        count++;
    }

    if (temp == NULL) {
        printf("Invalid position\n");
        return;
    }

    // Adjust pointers
    if (temp->prev != NULL)
        temp->prev->next = temp->next;
    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    free(temp);

    
}

void printNode(struct node * head)
{
    struct node * temp=head;
    if(head==NULL){
        printf("there is no node.");
        return;
    }
    printf("NULL<-");
    while(temp!=NULL)
    {
        printf(" %d ->",temp->data);
        temp=temp->next;
    }
    printf("NULL");
}
int main(){

    struct node * head=NULL;

    insertNewnodeAtbegin(&head,452);
    insertNewnodeAtbegin(&head,455);
    insertNewnodeAtbegin(&head,457);
    insertNewnodeAtbegin(&head,453);
    insertNewnodeAtbegin(&head,456);
    insertNewnodeAtbegin(&head,485);
    insertatend(&head,488);
    insertAtPosition(&head,401,3);
    deletionAnyNode(&head,1);
    deletionAnyNode(&head,9);
    printNode(head);

    return 0;
}
