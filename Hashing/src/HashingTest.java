import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
public class HashingTest {
    @Test
    void testGet() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        assertEquals("Bar", map.get("Foo"));
    }

    @Test
    void testDel() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        map.set("Bar", "Foo");
        assertEquals("Bar", map.get("Foo"));
        map.del("Foo");
        assertEquals(null, map.get("Foo"));
        assertEquals("Foo", map.get("Bar"));
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
    void testIn() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        assertEquals(true, map.in("Foo"));
        assertEquals(false, map.in("Bar"));
    }

    @Test
    void testLoad() {
        Hashing<String, String> map = new Hashing<String, String>();
        map.set("Foo", "Bar");
        assertEquals(1.0 / 7, map.load());
        map.set("Bar", "Foo");
        assertEquals(2.0 / 7, map.load());
        map.set("A", "B");
        assertEquals(3.0 / 7, map.load());
        map.set("C", "D");
        assertEquals(4.0 / 7, map.load());
        map.set("E", "F");
        assertEquals(5.0 / 7, map.load());
        map.set("G", "H");
        assertEquals(6.0 / 7, map.load());
        map.set("M", "N");
        assertEquals(7.0 / 7, map.load());
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
        map.resize(5);
        assertEquals(10, map.sizeOf());
        //assertEquals(1.0 / 5, map.load());
    }
}
