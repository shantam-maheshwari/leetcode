class Solution {
    public int countComponents(int n, int[][] edges) {
        DisjointSet ds = new DisjointSet(n);
        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];
            ds.doUnion(a, b);
        }
        return ds.getNumberOfComponents();
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