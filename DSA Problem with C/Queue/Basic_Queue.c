#include<stdio.h>
#include<stdlib.h>

struct queue
{
    int size;
    int r;
    int f;
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

void printqueue(struct queue * ptr)
{
    if (isempty(ptr))
    {
        printf("the queue is empty");
        return;
    }
    else
    {
        for(int i=ptr->f+1; i<=ptr->r;i++)
        {
            printf(" %d ",ptr->arr[i]);
        }
    }
    
}

int main()
{
    struct queue  q;
    q.size=10;
    q.f = -1; q.r=-1;
    q.arr=(int *)malloc(q.size * sizeof(int));

    enqueue(&q,34);
    enqueue(&q,35);
    enqueue(&q,39);
    enqueue(&q,54);
    enqueue(&q,50);

    printqueue(&q);

    dequeue(&q);

    printf("\nafter dequeue:");
    printqueue(&q);

    free(q.arr);

   return 0;
}
