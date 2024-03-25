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

    public int size = 7;
    private Pair<K, V> map[];
    private Pair<K, V> newMap[];

    public Hashing() {
        map = new Pair[size];
    }

    public void set(K key, V value) {
        int hash = key.hashCode() % size;
        Pair<K, V> pair = map[hash];

        if (pair == null) {
            map[hash] = new Pair<K, V>(key, value);
        }
        else {
            while (pair.next != null) {
                if (pair.getKey() == key) {
                    pair.setValue(value);
                    return;
                }
                pair = pair.next;
            }
            if (pair.getKey() == key) {
                pair.setValue(value);
                return;
            }
            pair.next = new Pair<K, V>(key, value);
        }
    }

    public V get(K key) {
        int hash = key.hashCode() % size;
        Pair<K, V> pair = map[hash];

        if (pair == null) {
            return null;
        }
        while (pair != null) {
            if (pair.getKey() == key) {
                return pair.getValue();
            }
            pair = pair.next;
        }
        return null;
    }

    public void del(K key) {
        int hash = key.hashCode() % size;
        Pair<K, V> pair = map[hash];

        if (pair.getKey() == key) {
            map[hash] = pair.next;
            pair.next = null;
        }
        Pair<K, V> prev = pair;
        while (pair != null) {
            if (pair.getKey() == key) {
                prev.next = pair.next;
                pair.next = null;
            }
            prev = pair;
            pair = pair.next;
        }
    }

    public boolean in(K key) {
        int hash = key.hashCode() % size;
        Pair<K, V> pair = map[hash];

        if (pair == null) {
            return false;
        }
        else if (pair.getKey() != key) {
            return false;
        }
        return true;
    }

    public int sizeOf() {
        int mapSize = 0;
        for (int i = 0; i < size; i++) {
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
        for (int i = 0; i < size; i++) {
            if (map[i] != null) {
                load++;
            }
        }
        return load / size;
    }

    public void resize(int newSize) {
        newMap = new Pair[newSize];
        int hash;
        for (int i = 0; i < size; i++) {
            if (map[i] != null) {
                hash = map[i].getKey().hashCode() % newSize;
                if (newMap[hash] == null) {
                    newMap[hash] = map[i];
                }
                else {
                    Pair<K, V> node = newMap[hash];
                    while (node.next != null) {
                        node = node.next;
                    }
                    node.next = map[i];
                }
            }
        }
        size = newSize;
        map = newMap;
    }
}
