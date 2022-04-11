class Solution {
    public int earliestAcq(int[][] logs, int n) {
        Arrays.sort(logs, (a, b) -> Integer.compare(a[0], b[0]));

        DisjointSet ds = new DisjointSet(n);
        for (int[] log : logs) {
            int time = log[0];
            int a = log[1];
            int b = log[2];
            ds.doUnion(a, b);
            if (ds.getNumberOfComponents() == 1) {
                return time;
            }
        }
        return -1;
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