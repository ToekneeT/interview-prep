import java.util.*;
public class MergeSort {

    public static int[] merge(int[] arrOne, int[] arrTwo) {
        int left = 0;
        int right = 0;
        int mergedIdx = 0;
        int[] mergedArr = new int[arrOne.length + arrTwo.length];

        while (left < arrOne.length && right < arrTwo.length) {
            if (arrOne[left] <= arrTwo[right]) {
                mergedArr[mergedIdx] = arrOne[left];
                left++;
            } else {
                mergedArr[mergedIdx] = arrTwo[right];
                right++;
            }
            mergedIdx++;
        }

        if (left < arrOne.length) {
            for (; left < arrOne.length; left++) {
                mergedArr[mergedIdx] = arrOne[left];
                mergedIdx++;
            }
        } else if (right < arrTwo.length) {
            for (; right < arrTwo.length; right++) {
                mergedArr[mergedIdx] = arrTwo[right];
                mergedIdx++;
            }
        }

        return mergedArr;
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        int half = arr.length / 2;
        int[] arrLeft = Arrays.copyOfRange(arr, 0, half);
        arrLeft = mergeSort(arrLeft);
        int[] arrRight = Arrays.copyOfRange(arr, half, arr.length);
        arrRight = mergeSort(arrRight);
        return merge(arrLeft, arrRight);
    }

    public static void main(String[] args) {
        int[] arrOne = {100, 200};
        int[] arrTwo = {100, 300, 400};
        int[] merged = merge(arrOne, arrTwo);
        int[] arr = {100, 500, 200, 90, 200, 30, 2};
//        int[] arr = {0};

        int[] merged = mergeSort(arr);
        System.out.println(Arrays.toString(merged));
    }
}