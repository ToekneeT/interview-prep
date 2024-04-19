import java.io.IOException;
import java.nio.file.*;
import java.util.Scanner;

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

    // The following two functions are almost identical functions.
    // They will call the other in the event there's a subdirectory.
    // I'm not sure this is correct. It *basically* feels like recursion,
    // but harder to read, and obviously repeated code since they're effectively identical.
    // The only difference is that I left the countFilesInSubDir to take a Path object
    // instead of passing it a string.
    // Easily changeable by doing countFilesInSubDir(path.toString()) if I wanted.
    public static int countFilesInSubDir(Path p) throws IOException{
        int numOfFiles = 0;
        DirectoryStream<Path> stream = Files.newDirectoryStream((p));
        for (Path path : stream) {
            if (!Files.isDirectory(path)) {
                numOfFiles++;
            } else {
                // Calls the other function if it finds a subdirectory.
                numOfFiles += amtOfFilesInDirs(path.toString());
            }
        }
        return numOfFiles;
    }

    public static int amtOfFilesInDirs(String dir) throws IOException {
        int numOfFiles = 0;
        DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get(dir));
        for (Path path : stream) {
            if (!Files.isDirectory(path)) {
                numOfFiles++;
            } else {
                // Calls the other function if it finds a subdirectory.
                numOfFiles += countFilesInSubDir(path);
            }
        }
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