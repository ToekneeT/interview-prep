import java.io.IOException;
import java.nio.file.*;
import java.util.Scanner;
import java.util.Stack;

public class TraverseDirectory {
    // Pass it an absolute path in string format.
    // Will recursively call itself if there are subdirectories.
    public static int countFilesInDirs(String dir) throws IOException {
        int numOfFiles = 0;
        // Paths.get() will convert a string into a Path object.
        DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get(dir));
        for (Path path : stream) {
            // Doesn't count directories as a file itself, but will run the function again
            // if it finds a directory to count the files within it.
            if (!Files.isDirectory(path)) {
                numOfFiles++;
            } else {
                // Since the function is passed a String directory, the Path object needs
                // to be converted back into a string.
                numOfFiles += countFilesInDirs(path.toString());
            }
        }
        return numOfFiles;
    }

    // Originally, the plan was to do a for loop for the top directory, and place any subdirectories
    // in the stack called directories. While coding that, I realized that it was repeated code and that
    // it was possible to do with a single while loop.
    // But the while loop conditional was if the stack wasn't empty, but the stack should've started
    // empty, in my mind, at least. So I decided to use a do...while loop.
    // But, it was the stream variable line that I realized I shouldn't use the passed parameter since
    // it was a different name from the stack.
    // Which resulted in me first pushing the passed parameter, and then popping it out.
    // So, the crux of the story, I didn't actually need a do...while.
    public static int amtOfFilesInDirs(String dir) throws IOException {
        // A stack representing all of the directories, including the top level.
        Stack<String> directories = new Stack<String>();
        // Pushes the initial passed directory into the stack. This is because the stream variable
        // reads only from the directories stack. If we read directly from the passed parameter,
        // there would need to be another variable to handle the passed parameter and then the stack.
        directories.push(dir);
        int numOfFiles = 0;
        do {
            // Takes a path out of the stack, there will always be at least one path in the stack initially as long
            // as the passed parameter is a valid path.
            DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get(directories.pop()));
            for (Path path : stream) {
                if (!Files.isDirectory(path)) {
                    numOfFiles++;
                } else {
                    // Pushes the directory into the stack. We don't want to go into the new directory just yet,
                    // we want to count the rest of the files in the current directory first.
                    // Turns the path object into a string as the stream variable takes a string and turns it into a
                    // path object.
                    directories.push(path.toString());
                }
            }
        // Repeats until the stack contains no other directories, meaning we've reached the root of the folders.
        } while (!directories.empty());
        return numOfFiles;
    }
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        System.out.println("Input an absolute path: ");
        String dir = input.nextLine();
        System.out.println(countFilesInDirs(dir));
        System.out.println(amtOfFilesInDirs(dir));
    }
}