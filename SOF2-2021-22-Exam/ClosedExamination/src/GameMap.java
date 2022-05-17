public class GameMap {
    // Public constant used to simplify the understanding of the code.
    public static final int EMPTY = 0;
    public static final int OBSTACLE = 1;
    public static final int RESOURCE = 2;

    private static final int INF = Integer.MAX_VALUE;

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
    private Position getClosestMatch(
        int[][] boardDistance, boolean[][] boardVisited,
        boolean visited, int tile, boolean match
    ) {
        Position closest = new Position(0, 0, INF);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int currentDistance = boardDistance[x][y];
                if (
                    boardVisited[x][y] == visited
                    && (board[x][y] == tile) == match
                    && currentDistance < closest.distance
                ) {
                    closest.setX(x);
                    closest.setY(y);
                    closest.setDistance(currentDistance);
                }
            }
        }
        return closest;
    }

    private boolean allVisited(boolean[][] boardVisited) {
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                if (!boardVisited[x][y] && board[x][y] != OBSTACLE) {
                    return false;
                }
            }
        }
        return true;
    }

    private Position dijkstra(int x, int y) {
        // Dijkstra's algorithm I guess
        // initialise distance and visited
        int[][] boardDistance = new int[width][height];
        boolean[][] boardVisited = new boolean[width][height];
        for (int y2 = 0; y2 < height; y2++) {
            for (int x2 = 0; x2 < width; x2++) {
                boardVisited[x2][y2] = false;
                boardDistance[x2][y2] = INF;
            }
        }
        boardDistance[x][y] = 0;
        int currentDistance = 1;
        
        // loop
        boolean someUnvisited = true;
        while (someUnvisited) {
            // process neighbours
            for (int xOffset = -1; xOffset <= 1; xOffset++){
                for (int yOffset = -1; yOffset <= 1; yOffset++) {
                    int x2 = x + xOffset;
                    if (!(0 <= x2 && x2 <= width)) {
                        continue;
                    }
                    int y2 = y = yOffset;
                    if (!(0 <= y2 && y2 <= height)) {
                        continue;
                    }
                    if (!boardVisited[x2][y2] && board[x2][y2] != OBSTACLE) {
                        boardDistance[x2][y2] = currentDistance;
                    }
                }
            }

            boardVisited[x][y] = true;
            Position closestUnvisited = getClosestMatch(
                boardDistance, boardVisited, false, OBSTACLE, false
            );
            x = closestUnvisited.getX();
            y = closestUnvisited.getY();
            currentDistance = closestUnvisited.getDistance();
            if (currentDistance == INF || allVisited(boardVisited)) {
                someUnvisited = false;
            }
            currentDistance += 1;
        }

        // return closest
        Position closestResource = getClosestMatch(
            boardDistance, boardVisited, true, RESOURCE, true
        );
        if (closestResource.getDistance() == INF) {
            return null;
        }
        return closestResource;
    }

    public Position getClosestResource(int x, int y) {
        Position closest;

        int startTile = board[x][y];
        if (startTile == OBSTACLE) {
            closest = null;
        } else if (startTile == RESOURCE) {
            closest = new Position(x, y, 0);
        } else {
            closest = dijkstra(x, y);
        }

        return closest;
    }
}
