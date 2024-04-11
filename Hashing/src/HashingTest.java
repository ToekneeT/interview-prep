import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

public class HashingTest {

    // Will fill hashmap based on the given size.
    // Running the function again on the same hashmap would replace the values instead of adding to it.
    // Key is number, value is corresponding letter in alphabet % num - 1.
    void fillHashmap(Hashing<Integer, String> map, int size) {
        String[] a_z = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        for (int i = 0; i < size; i++) {
            map.set(i, a_z[i % a_z.length]);
            assertEquals(map.get(i), a_z[i % a_z.length]);
        }
    }

    // Was used to test something short.
    void printMap(Hashing<Integer, String> map)  {
        for (int i = 0; i < map.sizeOf(); i++) {
            System.out.printf("K: %d V: %s\n", i, map.get(i));
        }
    }

    @Test
    void testFillHashmap()  {
        Hashing<Integer, String> map = new Hashing<>();
        // Intentionally filled every bucket by hoping that numbers 0-26 would be enough to fill
        // every bucket with collisions.
        fillHashmap(map, 27);
        assertEquals("a", map.get(0));
        assertEquals("z", map.get(25));
        assertEquals("a", map.get(26));
        assertEquals(27, map.sizeOf());
        assertEquals(1.00, map.load());
    }

    @Test
    void testKeyExists() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        assertTrue(map.keyExists("Foo"));
        assertFalse(map.keyExists("Bar"));
    }

    @Test
    void testSet()  {
        Hashing<Integer, String> map = new Hashing<>();
        map.set(0, "Zero");
        map.set(1, "One");
        assertTrue(map.keyExists(0));
        assertFalse(map.keyExists(3));
        assertEquals("Zero", map.get(0));
        assertEquals("One", map.get(1));
        // Tests the upsert portion.
        map.set(1, "Replaced");
        assertEquals("Replaced", map.get(1));
        map.set(0, "Replaced");
        assertEquals("Replaced", map.get(0));
    }

    @Test
    void testGetAndDel()  {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        map.set("Bar", "Foo");
        assertEquals("Bar", map.get("Foo"));
        assertEquals("Foo", map.get("Bar"));
        map.del("Foo");
        // Key that was just deleted should not exist in the map.
        assertFalse(map.keyExists("Foo"));
        assertEquals("Foo", map.get("Bar"));
        assertFalse(map.keyExists("Doesn't Exists"));
        Hashing<Integer, String> mapTwo = new Hashing<>();
        fillHashmap(mapTwo, 26);
        assertEquals("z", mapTwo.get(25));
        assertEquals("o", mapTwo.get(14));
        mapTwo.del(15);
        mapTwo = mapTwo.resize(2);
        assertEquals("z", mapTwo.get(25));
        assertEquals("o", mapTwo.get(14));
        mapTwo.del(14);
        assertEquals("z", mapTwo.get(25));
        assertEquals("b", mapTwo.get(1));
        // Checks to make sure the keys don't exist after deletion.
        // Key 15 was deleted before the map resize.
        assertFalse(mapTwo.keyExists(14));
        assertFalse(mapTwo.keyExists(15));
    }

    @Test
    void testNonExistingKey() {
        Hashing<Integer, String> map = new Hashing<>();
        map.set(1, "One");
        assertEquals("One", map.get(1));
        Throwable exception = assertThrows(KeyError.class, () -> {
                map.get(2);
            }
        );
        assertEquals("Key doesn't exist in map.", exception.getMessage());
    }

    @Test
    void testSizeOf() {
        Hashing<String, String> map = new Hashing<String, String>();
        assertEquals(0, map.sizeOf());
        map.set("Foo", "Bar");
        assertEquals(1, map.sizeOf());
        map.set("Bar", "Foo");
        assertEquals(2, map.sizeOf());
        map.set("A", "B");
        map.set("C", "D");
        map.set("E", "F");
        map.set("G", "H");
        assertEquals(6, map.sizeOf());
        map.set("I", "J");
        map.set("K", "L");
        map.set("M", "N");
        map.set("O", "P");
        assertEquals(10, map.sizeOf());
    }

    @Test
    void testResize() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        assertEquals(1.0 / 7, map.load());
        assertEquals(1, map.sizeOf());
        map.set("Bar", "Foo");
        assertEquals(2, map.sizeOf());
        map.set("A", "B");
        map.set("C", "D");
        map.set("E", "F");
        map.set("G", "H");
        assertEquals(6, map.sizeOf());
        map.set("I", "J");
        map.set("K", "L");
        map.set("M", "N");
        map.set("O", "P");
        assertEquals(10, map.sizeOf());
        map = map.resize(5);
        assertEquals(10, map.sizeOf());
    }

    @Test
    void testSizeOne()  {
        Hashing<String, String> map = new Hashing<String, String>();
        map = map.resize(1);
        map.set("A", "B");
        map.set("C", "D");
        map.set("E", "F");
        assertEquals("D", map.get("C"));
        assertEquals(3, map.sizeOf());
        map.del("A");
        assertFalse(map.keyExists("A"));
        assertEquals("D", map.get("C"));
        assertEquals("F", map.get("E"));
        assertEquals(1.0 / map.buckets, map.load());
        assertEquals(2, map.sizeOf());
    }

    @Test
    void testKeyExistsWithSize1() {
        Hashing<String, String> map = new Hashing<String, String>();
        map = map.resize(1);
        map.set("A", "B");
        assertTrue(map.keyExists("A"));
        map.set("C", "D");
        assertTrue(map.keyExists("C"));
        Hashing<Integer, String> mapTwo = new Hashing<>();
        fillHashmap(mapTwo, 26);
        // Checks if key 25, last element in map exist before and after resizing.
        assertTrue(mapTwo.keyExists(25));
        mapTwo = mapTwo.resize(1);
        assertTrue(mapTwo.keyExists(25));
    }

    @Test
    void testIntegrityOfMapResize() {
        Hashing<Integer, String> map = new Hashing<>();
        fillHashmap(map, 26);
        assertEquals(7.0 / map.buckets, map.load());
        assertEquals(26, map.sizeOf());
        assertEquals("z", map.get(25));
        assertTrue(map.keyExists(25));
        map = map.resize(2);
        assertEquals(2.0 / map.buckets, map.load());
        assertEquals(26, map.sizeOf());
        assertTrue(map.keyExists(25));
        assertEquals("z", map.get(25));
    }

    @Test
    void testIntegrityOfMapResizeOutput() {
        Hashing<Integer, String> map = new Hashing<>();
        fillHashmap(map, 7);
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "K: 0 V: a\n" + "K: 1 V: b\n" + "K: 2 V: c\n" + "K: 3 V: d\n" + "K: 4 V: e\n" +
                "K: 5 V: f\n" + "K: 6 V: g\n";
        printMap(map);
        assertEquals(expectedOutput, outContent.toString());
        map = map.resize(2);
        outContent.reset();
        printMap(map);
        assertEquals(expectedOutput, outContent.toString());
        map = map.resize(10);
        outContent.reset();
        printMap(map);
        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    void testKeys() {
        // Set bucket size to 1 so that filling up the map would result in ascending order based on the implementation
        // of the fillHashmap function. That way testing if the keys match with a for loop is easier.
        Hashing<Integer, String> map = new Hashing<>(1);
        fillHashmap(map, 26);
        ArrayList<Object> k = map.keys();
        for (int i = 0; i < k.size(); i++) {
            assertEquals(i, k.get(i));
        }
    }

    @Test
    void testValues() {
        // Set bucket size to 1 so that filling up the map would result in ascending order based on the implementation
        // of the fillHashmap function. That way testing if the keys match with a for loop is easier.
        Hashing<Integer, String> map = new Hashing<>(1);
        fillHashmap(map, 26);
        ArrayList<Object> v = map.values();
        for (int i = 0; i < v.size(); i++) {
            assertEquals(map.get(i), v.get(i));
        }
    }

//    @Test
//    void printForMe()  {
//        Hashing<Integer, String> map = new Hashing<>();
//        fillHashmap(map, 7);
//        map.printMap();
//    }

    @Test
    void testLoad()  {
        Hashing<Integer, String> map = new Hashing<Integer, String>();
        assertEquals(0.0 / map.buckets, map.load());
        map.set(0, "Bar");
        assertEquals("Bar", map.get(0));
        assertEquals(1.0 / map.buckets, map.load());
        // Should fill up all the buckets with collisions.
        fillHashmap(map, 26);
        // Makes sure that the value gets upserted, so that value 0 should no longer be "Bar"
        assertEquals("a", map.get(0));
        assertEquals(1, map.load());
        Hashing<Integer, String> mapTwo = new Hashing<>(2);
        assertEquals(0.0 / mapTwo.buckets, mapTwo.load());
        mapTwo.set(1, "One");
        assertEquals(1.0 / mapTwo.buckets, mapTwo.load());
    }

    @Test
    void testInit5() {
        Hashing<Integer, String> map = new Hashing<Integer, String>(5);
        map.set(1, "One");
        map.set(2, "Two");
        assertEquals(2, map.sizeOf());
        assertEquals(2.0 / map.buckets, map.load());
    }
}
