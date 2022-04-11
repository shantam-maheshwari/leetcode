import java.util.Map;

class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n = s.length();

        DisjointSet ds = new DisjointSet(n);
        for (List<Integer> pair : pairs) {
            int a = pair.get(0);
            int b = pair.get(1);
            ds.doUnion(a, b);
        }

        HashMap<Integer, PriorityQueue<Character>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            int root = ds.findRoot(i);
            map.putIfAbsent(root, new PriorityQueue<Character>());
            map.get(root).add(c);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int root = ds.findRoot(i);
            char c = map.get(root).remove();
            sb.append(c);
        }

        return sb.toString();
    }
}

class DisjointSet {
    private int[] root;
    private int[] rank;
    private int numberOfComponents;

    public DisjointSet(int size) {
        root = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++) {
            root[i] = i;
            rank[i] = 1;
        }
        numberOfComponents = size;
    }

    public int findRoot(int x) {
        while (x != root[x]) {
            root[x] = root[root[x]];
            x = root[x];
        }
        return x;
    }

    public void doUnion(int x, int y) {
        int rootX = findRoot(x);
        int rootY = findRoot(y);

        if (rootX == rootY) {
            return;
        }

        if (rank[rootX] > rank[rootY]) {
            root[rootY] = rootX;
        } else if (rank[rootX] < rank[rootX]) {
            root[rootX] = rootY;
        } else {
            root[rootY] = rootX;
            rank[rootX]++;
        }
        numberOfComponents--;
    }

    public int getNumberOfComponents() {
        return numberOfComponents;
    }
}