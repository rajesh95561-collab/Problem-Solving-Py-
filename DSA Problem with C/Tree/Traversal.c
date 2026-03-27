#include<stdio.h>
#include<stdlib.h>

struct node {
  int data;
  struct node* left;
  struct node* right;
};

struct node * createNode(int data){
  struct node* newnode=(struct node *)malloc(sizeof(struct node));
  newnode->data=data;
  newnode->left=NULL;
  newnode->right=NULL;
  return newnode;
}

void preOrder(struct node * root){
    if (root!=NULL)
    {
        printf("%d ",root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
    
}

void postOrder(struct node* root){
    if(root!=NULL){
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ",root->data);
    }
}

void inOrder(struct node* root){
    if(root!=NULL){
        inOrder(root->left);
        printf("%d ",root->data);
        postOrder(root->right);
    }
}

struct node* insertioninBst(struct node* root,int val){

  if(root==NULL){
    return createNode(val);
  }
  if(root->data < val){
    root->right=insertioninBst(root->right,val);
  }
  else if(root->data > val){
    root->left=insertioninBst(root->left,val);
  }

}
struct node * inOrderPredesesor(struct node *root)
{
  root=root->left;
  while(root->right != NULL){
    root=root->right;
  }
  return root;
}

struct node* deletion_bst(struct node* root,int val)
{
  struct node * ipre;
  if(root==NULL){
    return NULL;
  }
  //if we found the leaf node 
  if(root->left==NULL && root->right==NULL){
    free(root);
    return NULL;
  }
  //search the node which is to be deleted
  if(val > root->data){
    root->right=deletion_bst(root->right,val);
  }
  else if(val < root->data){
    root->left=deletion_bst(root->left,val);
  }
  //afer we found that node we delete that node
  else{
    ipre=inOrderPredesesor(root);
    root->data=ipre->data;
    root->left=deletion_bst(root->left,ipre->data);
  }
  return root;
}
int main(){
  struct node * root=NULL;

  struct node * r=createNode(90);
  struct node * a=createNode(80);
  struct node * b=createNode(95);
  struct node * c=createNode(60);
  struct node * d=createNode(100);
  root=r;

  r->left=a;
  r->right=b;
  a->left=c;
  b->right=d;

  printf("preorder traversal is: ");
    preOrder(r);
    printf("\npostorder traversal is: ");
    postOrder(r);
    printf("\ninorder traversal is: ");
    inOrder(r);

    insertioninBst(r,20);
    insertioninBst(r,53);

    printf("\nAfter insertion\n");
    printf("preorder traversal is: ");
    preOrder(r);
    printf("\npostorder traversal is: ");
    postOrder(r);
    printf("\ninorder traversal is: ");
    inOrder(r);

    deletion_bst(r,100);
    deletion_bst(r,53);

    printf("\nAfter deletion\n");
    printf("preorder traversal is: ");
    preOrder(r);
    printf("\npostorder traversal is: ");
    postOrder(r);
    printf("\ninorder traversal is: ");
    inOrder(r);
  return 0;
}
