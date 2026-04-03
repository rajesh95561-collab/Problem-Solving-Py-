#include<stdio.h>
#include<stdlib.h>

struct tnode{
    int data;
    struct tnode* left;
    struct tnode* right;
};

struct tnode * createnode(int data){
    struct tnode* newnode=(struct tnode*)malloc(sizeof(struct tnode));
    newnode->data=data;
    newnode->left=NULL;
    newnode->right=NULL;
    return newnode;
}

struct tnode * search(struct tnode* root,int target){
    if(root==NULL){
        return NULL;    
    }
    if(target==root->data){
        return root;
    }
    else if(root->data > target){
       return search(root->left,target);
    }
    else
     return search(root->right,target);
}

 struct tnode *insertion(struct tnode* root,int val){
    if(root==NULL){
        return createnode(val);    
    }
    if(root->data < val){
        root->right=insertion(root->right,val);
    }
    else if(root->data>val){
     root->left=insertion(root->left,val);
    }
    return root;

}


void inorder(struct tnode * root){
    if(root != NULL)
    {
        inorder(root->left);
        printf("%d\t",root->data);
        inorder(root->right);
    }
}

int main(){

    struct tnode* r=createnode(50);
    struct tnode* a=createnode(40);
    struct tnode* b=createnode(60);
    struct tnode* c=createnode(20);
    struct tnode* d=createnode(45);
    struct tnode* e=createnode(55);
    struct tnode* f=createnode(70);

    r->left=a;
    r->right=b;
    a->left=c;
    a->right=d;
    b->left=e;
    b->right=f;

    insertion(r,88);
    insertion(r,8);
    insertion(r,44);
    // printf("%d\n",ptr->data);

    inorder(r);

    // struct tnode * n=search(r,80);
    // if(n!=NULL){
    // printf("%d",n->data);
    // }
    // else
    // printf("not found");

    return 0;
}