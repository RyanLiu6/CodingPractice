import java.util.Arrays;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Hello World!");

        int arr[] = {1, 2, 55, 28, 83, 3, 4, 11, 42};
        int target = 83;
        Arrays.sort(arr);

        int value = binarySearch(arr, 0, arr.length - 1, target);

        System.out.println(value);

        for (int val : arr)
        {
            System.out.print(val + " ");
        }
    }

    public static int binarySearch(int arr[], int left, int right, int target)
    {
        if (right >= 1)
        {
            int mid = (left + right)/2;

            if (arr[mid] == target)
            {
                return mid;
            }
            else if (arr[mid] > target)
            {
                return binarySearch(arr, left, mid - 1, target);
            }
            else
            {
                return binarySearch(arr, mid + 1, right, target);
            }
        }

        return -1;
    }
}
