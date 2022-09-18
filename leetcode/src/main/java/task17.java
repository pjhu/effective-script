public class task17 {

    static class Node {
        int data;
        Node left, right;
    }

    // Create a new node
    static Node newNode(int k) {
        Node node = new Node();
        node.data = k;
        node.right = null;
        node.left = null;
        return node;
    }

    // Calculate the depth
    static int depth(Node node) {
        int d = 0;
        while (node != null) {
            d++;
            node = node.left;
        }
        return d;
    }

    // Check if the tree is perfect binary tree
    static boolean is_perfect(Node root, int d, int level) {

        // Check if the tree is empty
        if (root == null)
            return true;

        // If for children
        if (root.left == null && root.right == null)
            return (d == level + 1);

        if (root.left == null || root.right == null)
            return false;

        return is_perfect(root.left, d, level + 1) && is_perfect(root.right, d, level + 1);
    }

    // Wrapper function
    static boolean is_Perfect(Node root) {
        int d = depth(root);
        return is_perfect(root, d, 0);
    }

    static int solution(Node root) {
        return 1;
    }

    public static void main(String[] args) {
        // Create tree
        Node root = newNode(1);
        root.left = newNode(2);
        root.right = newNode(3);

        root.left.right = newNode(4);
        root.right.left = newNode(5);
        root.right.right = newNode(6);

        root.right.left.left = newNode(7);
        root.right.left.right = newNode(8);
        root.right.right.left = newNode(9);
        root.right.right.right = newNode(10);
        root.right.right.right.left = newNode(11);

        int h = solution(root);
        System.out.println("Size : " + (Math.pow(2, h) - 1));
    }
}
