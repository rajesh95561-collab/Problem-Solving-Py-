#include<stdio.h>
#include<stdlib.h>

struct node{
    int coeff,pow;
    struct node * next;
};

struct node * createnode(int coeff,int pow)
{
    struct node * newnode=(struct node *)malloc(sizeof(struct node));
    newnode->coeff=coeff;
    newnode->pow=pow;
    newnode->next=NULL;
    return newnode;
}

void insertelment(struct node ** poly,int coeff,int pow)
{
    struct node * newnode=createnode(coeff,pow);

    if(*poly==NULL)
    {
        *poly=newnode;
        return;
    }

    struct node * temp=(*poly);
    while (temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;

}

void display(struct node *poly)
{
    while(poly!=NULL)
    {
        printf("%dX^%d",poly->coeff,poly->pow);
        poly=poly->next;
        if(poly!=NULL)
         printf("+");
    }
      
}

struct node * addpoly(struct node * poly1,struct node * poly2)
{
    struct node * result=NULL;
    while(poly1!=NULL&&poly2!=NULL)
    {
        if(poly1->pow > poly2->pow)
        {
            insertelment(&result,poly1->coeff,poly1->pow);
            poly1=poly1->next;
        }
        else if(poly1->pow < poly2->pow)
        {
            insertelment(&result,poly2->coeff,poly2->pow);
            poly2=poly2->next;
        }
        else
        {
            int sum=poly1->coeff+poly2->coeff;
            insertelment(&result,sum,poly1->pow);
            poly1=poly1->next;
            poly2=poly2->next;
        }
    }

    while(poly1!=NULL)
    {
        insertelment(&result,poly1->coeff,poly1->pow);
        poly1=poly1->next;
    }
    while(poly2!=NULL)
    {
        insertelment(&result,poly2->coeff,poly2->pow);
        poly2=poly2->next;
    }

    return result;
}


int main()
{
    struct node * poly1=NULL;
    struct node * poly2=NULL;
    struct node * result=NULL;

    insertelment(&poly1,5,3);
    insertelment(&poly1,4,2);
    insertelment(&poly1,2,0);

    insertelment(&poly2,5,2);
    insertelment(&poly2,5,1);
    insertelment(&poly2,5,0);

    printf("poly1:");
    display(poly1);

    printf("\npoly2:");
    display(poly2);

    printf("\nresult:");
    result=addpoly(poly1,poly2);
    display(result);


    return 0;
}