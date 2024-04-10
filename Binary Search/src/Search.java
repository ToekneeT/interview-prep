import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
public class Search {

    public static void linSearch(ArrayList<String> words, String target) {
        boolean found = false;
        int index = 0;
        // Used to calculate elapsed time.
        long finish = 0;
        long start = System.nanoTime();
        for (int i = 0; i < words.size(); i++) {
            if (words.get(i).equals(target)) {
                finish = System.nanoTime();
                index = i;
                found = true;
                break;
            }
        }
        System.out.println("Linear Search:");
        if (found) {
            System.out.printf("%s found at index %d\n", target, index);
            double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
            System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
            return;
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void indexOf(ArrayList<String> words, String target) {
        long start = System.nanoTime();
        int indexOf = words.indexOf(target);
        long finish = System.nanoTime();
        System.out.println("Index of:");
        if (indexOf != -1) {
            System.out.printf("%s found at index %d\n", target, indexOf);
            double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
            System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
            return;
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void binarySearch(ArrayList<String> words, String target) {
        long start = System.nanoTime();
        long finish = 0;
        // low and high are inclusive bounds representing pointers inside the word array.
        // The bounds represent the current search range we're considering,
        // such taht we know the target word is somewhere between [low, high] (which is initially
        // the entire array). During the search, we also know that the word cannot possibly be between
        // [0, low - 1], or between [high + 1, words.size() - 1], as these portions of the array have been
        // eliminated by binary search.
        int low = 0;
        int high = words.size() - 1;
        System.out.println("Binary Search:");

        while (low <= high) {
            int mid = (low + high) / 2;
            if (words.get(mid).equals(target)) {
                finish = System.nanoTime();
                System.out.printf("%s found at index %d\n", target, mid);
                double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
                System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
                return;
            }
            // Adjusting the search range based on the comparison between the target and the midpoint word.
            // For example, if target = "zebra" and the word at mid index = "monkey", since "zebra" is lexicographically
            // greater than "monkey", we eliminate the left half of the current search range including "monkey" by
            // setting low = mid + 1. Conversely, if "zebra" was less than "monkey", we would eliminate the right half
            // of the search range by setting high = mid - 1.
            if (words.get(mid).compareTo(target) < 0) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // Stick the words in the word file into an arraylist.
        ArrayList<String> words = new ArrayList<>();
        try {
            File w = new File("words_alpha.txt");
            Scanner reader = new Scanner(w);
            while (reader.hasNextLine()) {
                words.add(reader.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error has occurred.");
            e.printStackTrace();
        }

        System.out.println("Enter a word to search: ");
        String lookup = input.nextLine().toLowerCase();

        while (!lookup.equals("quit program")) {
            linSearch(words, lookup);
            indexOf(words, lookup);
            binarySearch(words, lookup);
            System.out.println("Enter a word to search: ");
            lookup = input.nextLine().toLowerCase();
        }

    }
}