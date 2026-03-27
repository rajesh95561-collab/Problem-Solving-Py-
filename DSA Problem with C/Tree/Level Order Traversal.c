#include<stdio.h>
#include<stdlib.h>

struct node
{
  int data;
  struct node * left;
  struct node * right;
};

struct queue
{
  int size;
  int f,r;
  int *arr;
};

int isempty(struct queue *ptr)
{
    if(ptr->r==ptr->f)
    return 1;
    else return 0;
}

int isfull(struct queue *ptr)
{
    if(ptr->r==ptr->size-1)
    return 1;
    else return 0;
}

void enqueue(struct queue * ptr,int value)
{
    if(isfull(ptr))
    printf("the queue is overflow");
    else
    {
        ptr->r++;
        ptr->arr[ptr->r]=value;
    
    }
}

void dequeue(struct queue * ptr)
{
    if(isempty(ptr))
    printf("the queue is empty");
    else
    {
        int a;
        ptr->f++;
        a=ptr->arr[ptr->f];
        return ;
    }
}

void levelOrder(struct node* root){
  
}

struct node* createnode(int val){
  struct node* newnode=(struct node*)malloc(sizeof(struct node));
  newnode->data=val;
  newnode->left=NULL;
  newnode->right=NULL;
  return newnode;
}

void inorder(struct node* root){
  if(root!=NULL){
    inorder(root->left);
    printf("%d\n",root->data);
    inorder(root->right);
  }
}

int main(){

  struct queue* q;
  q->size=30;
  q->f=q->r=-1;
  q->arr=(int*)malloc((q->size) * sizeof(int));
  

    struct node* r=createnode(50);
    struct node* a=createnode(40);
    struct node* b=createnode(60);
    struct node* c=createnode(20);
    struct node* d=createnode(45);
    struct node* e=createnode(55);
    struct node* f=createnode(70);

    r->left=a;
    r->right=b;
    a->left=c;
    a->right=d;
    b->left=e;
    b->right=f;

    inorder(r);

  return 0;
}