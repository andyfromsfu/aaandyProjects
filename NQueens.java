// solutions
public class NQueens {

    public static void main(String[] args) {
        int n = 8;
        nQueens(n);

    }

    private static void nQueens(int noOfQueens) {
        int[] board = new int[noOfQueens];
        placeQueen(board, 0, noOfQueens);
    }

    // static int count = 0;

    private static void placeQueen(int[] board, int current, int noOfQueens) {
        if (current == noOfQueens) {// print board
            displayQueens(board);
            // count++;
            return;
        }

        for (int i = 0; i < noOfQueens; i++) {// HERE
            board[current] = i;
            if (noKill(board, current)) {
                placeQueen(board, current + 1, noOfQueens);
            }
        }
    }

    // no kill - checking
    private static boolean noKill(int[] board, int currentColumnOfQueen) {

        for (int i = 0; i < currentColumnOfQueen; i++) {
            // same row
            if (board[i] == board[currentColumnOfQueen])
                return false;

            // Diagonal
            if ((currentColumnOfQueen - i) == Math.abs(board[currentColumnOfQueen] -
                    board[i])) {
                return false;
            }
        }
        return true;
    }

    private static void displayQueens(int[] board) {
        System.out.print("\n");

        for (int value : board)
            System.out.printf(value + "%3s", " ");

        System.out.print("\n\n");

        int n = board.length;

        for (int i = 0; i < n; i++) {
            for (int value : board) {
                if (value == i)
                    System.out.print("Q\t");
                else
                    System.out.print("*\t");
            }
            System.out.print("\n");
        }
    }
}