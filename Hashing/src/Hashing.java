<<<<<<< HEAD
import java.util.AbstractMap;
import java.util.ArrayList;

=======
import java.util.ArrayList;
>>>>>>> 3dd4f8a2ed6fdcd269276f7601a615920790c87d
class KeyError extends RuntimeException {
    public KeyError(String errorMessage) {
        super(errorMessage);
    }
}

public class Hashing<K, V> {

    private class Pair<K, V> {
        private K key;
        private V value;
        private Pair<K, V> next;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return this.key;
        }

        public V getValue() {
            return this.value;
        }

        public void setValue(V value) {
            this.value = value;
        }
    }

    // The amount of buckets created.
    public int buckets;
    private Pair<K, V> map[];
    private Pair<K, V> newMap[];

    // If no buckets is specified, defaults to 7.
    public Hashing() {
        map = new Pair[7];
        buckets = 7;
    }

    public Hashing(int buckets) {
        this.buckets = buckets;
        map = new Pair[buckets];
    }

    // Turns the key into a hash and then mods it by the bucket size.
    private int hashToBucket(K key, int bucketSize) {
        return key.hashCode() % bucketSize;
    }

    // More of an upsert than a set, but set is a nicer name.
    public void set(K key, V value) {
        int hash = hashToBucket(key, buckets);
        Pair<K, V> bucketCursor = map[hash];

        if (bucketCursor == null) {
            map[hash] = new Pair<K, V>(key, value);
            return;
        }
        // If key exists already, replace the value.
        if (bucketCursor.getKey() == key) {
            bucketCursor.setValue(value);
            return;
        }
        while (bucketCursor.next != null) {
            bucketCursor = bucketCursor.next;
        }
        bucketCursor.next = new Pair<K, V>(key, value);
    }

    public V get(K key) {
        int hash = hashToBucket(key, buckets);
        Pair<K, V> bucketCursor = map[hash];

        if (bucketCursor == null) {
            throw new KeyError("Key doesn't exist in map.");
        }
        while (bucketCursor != null) {
            if (bucketCursor.getKey() == key) {
                return bucketCursor.getValue();
            }
            bucketCursor = bucketCursor.next;
        }
        throw new KeyError("Key doesn't exist in map.");
    }

    public boolean keyExists(K key) {
        int hash = hashToBucket(key, buckets);
        Pair<K, V> bucketCursor = map[hash];

        if (bucketCursor == null) {
            return false;
        }
        while (bucketCursor != null) {
            if (bucketCursor.getKey() == key) {
                return true;
            }
            bucketCursor = bucketCursor.next;
        }
        return false;
    }

    public void del(K key) {
        int hash = hashToBucket(key, buckets);
        Pair<K, V> bucketCursor = map[hash];

        if (bucketCursor.getKey() == key) {
            map[hash] = bucketCursor.next;
            bucketCursor.next = null;
            return;
        }
        Pair<K, V> prev = bucketCursor;
        while (bucketCursor != null) {
            if (bucketCursor.getKey() == key) {
                prev.next = bucketCursor.next;
                bucketCursor.next = null;
            }
            prev = bucketCursor;
            bucketCursor = bucketCursor.next;
        }
    }

    public int sizeOf() {
        int mapSize = 0;
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                nextNode = nextNode.next;
                mapSize++;
            }
        }
        return mapSize;
    }

    public double load() {
        double load = 0;
        for (int i = 0; i < buckets; i++) {
            if (map[i] != null) {
                load++;
            }
        }
        return load / buckets;
    }

    // Resize returns a new map.
    public Hashing<K, V> resize(int newBucSize) {
        Hashing<K, V> newMap = new Hashing<>(newBucSize);
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                newMap.set(nextNode.getKey(), nextNode.getValue());
                nextNode = nextNode.next;
            }
        }
        return newMap;
    }

    public ArrayList<Object> keys() {
        ArrayList<Object> keys = new ArrayList<>();
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                keys.add(nextNode.getKey());
                nextNode = nextNode.next;
            }
        }
        return keys;
    }

    public ArrayList<Object> values() {
        ArrayList<Object> values = new ArrayList<>();
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                values.add(nextNode.getValue());
                nextNode = nextNode.next;
            }
        }
        return values;
    }

    public ArrayList<AbstractMap.SimpleEntry<K, V>> items() {
        ArrayList<AbstractMap.SimpleEntry<K,V>> items = new ArrayList<>();
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                items.add(new AbstractMap.SimpleEntry<K, V>(nextNode.getKey(), nextNode.getValue()));
                nextNode = nextNode.next;
            }
        }
        return items;
    }

    public void printMap() {
        for (int i = 0; i < buckets; i++) {
            Pair<K, V> nextNode = map[i];
            while (nextNode != null) {
                System.out.printf("K: %d V: %s\n", nextNode.getKey(), nextNode.getValue());
                nextNode = nextNode.next;
            }
        }
    }
}
