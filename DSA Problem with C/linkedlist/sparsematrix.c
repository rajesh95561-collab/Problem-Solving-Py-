#include<stdio.h>
#include<stdlib.h>

struct node
{
  int row ,col,value;
    struct node * next; 
};

struct node * createnode(int row ,int col ,int val)
{
    struct node * newnode=(struct node * )malloc(sizeof(struct node));
    newnode->row=row;
    newnode->col=col;
    newnode->value=val;
    newnode->next=NULL;
    return newnode;
}

void insertnode(struct node **head,int row ,int col ,int val)
{
    struct node * newnode=createnode(row,col,val);
    if(newnode==NULL)
    {
        printf("memory allocation faild");
        return;
    }
    if(*head==NULL)
    {
        *head=newnode;
        return;
    }

    struct node * ptr=*head;
    while(ptr->next!=NULL)
    {
        ptr=ptr->next;
    }
    ptr->next=newnode;

}

void displaymatrix(struct node * head)
{
    struct node * ptr=head;
    printf("\trow\tcolumn\tvalue\n");

    while(ptr!=NULL)
    {
       printf("\t%d\t%d\t%d\n",ptr->row,ptr->col,ptr->value); 
       ptr=ptr->next;
    }
}

int main()
{
    struct node * head=NULL;

    int m,n;

    printf("enter value for rows");
    scanf("%d",&m);
    printf("enter value for column");
    scanf("%d",&n);

    int arr[m][n];

    printf("enter value for matrix");
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }

    }

    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(arr[i][j]!=0)
            {
                insertnode(&head,i,j,arr[i][j]);
            }
        }

    }
printf("the sparse matrix is:\n");
displaymatrix(head);
    
}