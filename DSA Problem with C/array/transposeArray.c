#include<stdio.h>
void main(){
    int m,n;
    printf("enter the size of row:");
    scanf("%d",&m);
     printf("enter the size of column:");
    scanf("%d",&n);
    int arr[m][n],arrT[m][n];
    printf("enter the value for  array:");
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
        scanf("%d",&arr[i][j]);
        }
    }
     printf("input array is:\n");
     for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
        printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    printf("the transpose array is:\n");

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            arrT[i][j]=arr[j][i];
            printf("%d\t",arrT[i][j]);
        }
                printf("\n");

    }
    
}