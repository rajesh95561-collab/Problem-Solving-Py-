/*
 * Program to read an array of integers,
 * display the original array, and then
 * print the array elements in reverse order.
 */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the values for the array:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The array is:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nThe reverse array is:\n");
    for (int j = n - 1; j >= 0; j--) {
        printf("%d ", arr[j]);
    }

    free(arr);
    return 0;
}