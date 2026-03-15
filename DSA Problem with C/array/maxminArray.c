// This C program reads an integer n from the user, then takes n elements as input to form an array. It displays the array and calculates both the maximum and minimum 
// values. The logic initializes max_num and min_num with the first element, then iterates through the array to update them accordingly. Finally, it prints the largest 
// and smallest numbers.


#include<stdio.h>
void main(){
    int n;
    printf("enter the size of the array:");
    scanf("%d",&n);
    int arr[n],max_num,min_num;
    printf("enter the value for  array:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);

    }
    printf("the array is:");
    for(int i=0;i<n;i++){
        printf(" %d ",arr[i]);  
    }
    max_num=arr[0];
    min_num=arr[0];
    for(int i=0;i<n;i++){
     if(max_num<arr[i]){
         max_num=arr[i];
     }
    }
       for(int i=0;i<n;i++){
     if(min_num>arr[i]){
         min_num=arr[i];
     }
    }
    printf("\nmax number is:%d\n",max_num);
    printf("min num:%d",min_num);

    
}