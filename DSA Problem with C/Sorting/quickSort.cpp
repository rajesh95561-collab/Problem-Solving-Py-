#include<stdio.h>

int partition(int arr[],int start,int end){
  int pivot=arr[end];
  int idx=start-1;
  for(int j=start;j<end;j++){
    if(arr[j] <= pivot){
      idx++;
      int temp=arr[j];
      arr[j]=arr[idx];
      arr[idx]=temp;
    }
  }
      idx++;
      int tempe=arr[idx];
      arr[idx]=arr[end];
      arr[end]=tempe;

    return idx;
}

void quickSort(int arr[],int start,int end){
  if(start<end){
    int pividx=partition(arr,start,end);
    //for left half of the partition
    quickSort(arr,start,pividx-1);
    //for right half of the partition
    quickSort(arr,pividx+1,end);
  }
}

void printArray(int arr[],int start,int end){
  printf("\n{ ");
  for(int i=start;i<end;i++){
    printf("%d ,",arr[i]);
  }
  printf("}\n");
}

int main(){
  int arr[]={7,6,5,4,3,2,1,10};
  printf("Before Sorting:");
  printArray(arr,0,8);
  quickSort(arr,0,8);
  printf("After Sorting:");
  printArray(arr,0,8);
  return 0;
}
