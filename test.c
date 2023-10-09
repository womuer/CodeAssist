void findDuplicates(int arr[], int n) {
    int i, j;
    printf(
);
    
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                printf(
, arr[i]);
            }
        }
    }
}