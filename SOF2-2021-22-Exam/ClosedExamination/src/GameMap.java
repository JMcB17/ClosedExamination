import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class GameMap {
    // Public constant used to simplify the understanding of the code.
    public static final int EMPTY = 0;
    public static final int OBSTACLE = 1;
    public static final int RESOURCE = 2;

    /**
     * The board representation as a 2D array of int. A value of 0 means an
     * empty cell, a value of 1 means that the cell is occupied by an
     * obstacle, and a value of 2 means that a resource is contained within
     * that cell.
     */
    int[][] board;

    /**
     * The dimension fo the board.
     */
    int width, height;

    /**
     * Construct a game board given a 2D array of int. The content of the array
     * is not checked and therefore it could contain negative values. In addition,
     * the constructor does not throw an error if the parameter is null or if the
     * parameter is not a rectangular array, that is all rows have the same number
     * of columns.
     * 
     * @param board The 2D array used to initialise the board.
     */
    public GameMap(int[][] board) {
        this.width = board.length;
        this.height = board[0].length;
        this.board = new int[width][height];

        // BE CAREFULL OF THE REPRESENTATION USED HERE, the ROWS are
        // the Y-COORDINATES and the COLUMNS are the X-COORDINATES.
        // To get the value of the board at position (x=1, y=0) you
        // must make the call board[0][1].
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[r].length; c++) {
                this.board[c][r] = board[r][c];
            }
        }
    }

    /////////////// ADD YOUR CODE BELOW ///////////////

}
