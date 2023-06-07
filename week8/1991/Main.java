package week8.1991;

import java.util.*;

public class Main {
    static Node[] nodes;

    static void preorder(Node node) {
        System.out.print(node.data);
        if (node.left != null) preorder(node.left);
        if (node.right != null) preorder(node.right);
    }

    static void inorder(Node node) {
        if (node.left != null) inorder(node.left);
        System.out.print(node.data);
        if (node.right != null) inorder(node.right);
    }

    static void postOrder(Node node) {
        if (node == null) return;
        postOrder(node.left);
        postOrder(node.right);
        System.out.print(node.data);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        nodes = new Node[N];

        for (int i=0; i<N; i++) nodes[i] = new Node((char)('A'+i));

        while(N-- > 0) {
            char data = sc.next().charAt(0);
            char left = sc.next().charAt(0);
            char right = sc.next().charAt(0);

            if (left != '.') nodes[data-'A'].left = nodes[left-'A'];
            if (right != '.') nodes[data-'A'].right = nodes[right-'A'];
        }

        preorder(nodes[0]);
        System.out.println();
        inorder(nodes[0]);
        System.out.println();
        postorder(nodes[0]);
        System.out.println();

        sc.close();

    }
}


class Node {
    private char data;
    Node left, right;

    Node(chat data) {
        this.data = data;
    }
}