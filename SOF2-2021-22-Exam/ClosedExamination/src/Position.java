/**
 * Class used to store the coordinates (x,y) of a point and its relative
 * distance
 * to the player.
 * 
 * Position p = new Position(1,2 5);
 */
public class Position {

    /** The x-coordinate of the cell */
    int x;

    /** The y-coordinate of the cell */
    int y;

    /**
     * The distance of the cell from the player. The distance must be greater
     * or equal to 0.
     */
    int distance;

    /**
     * Construct an instance of Position.
     * 
     * @param x        The x-coordinate of the cell
     * @param y        The y-coordinate of the cell
     * @param distance the distance of the cell from the player.
     * @throws IllegalArgumentException if the distance is negative.
     */
    public Position(int x, int y, int distance) {
        if (distance < 0) {
            throw new IllegalArgumentException();
        }
        this.x = x;
        this.y = y;
        this.distance = distance;
    }

    /**
     * Construct an instance of Position, where the cell is at the position of
     * the player (distance is 0).
     * 
     * @param x The x-coordinate of the cell
     * @param y The y-coordinate of the cell
     */
    public Position(int x, int y) {
        this(x, y, 0);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", d = " + distance + ")";
    }

    /**
     * return the x-coordinate of the cell.
     * 
     * @return the x-coordinate of the cell.
     */
    public int getX() {
        return x;
    }

    /**
     * return the y-coordinate of the cell.
     * 
     * @return the y-coordinate of the cell.
     */
    public int getY() {
        return y;
    }

    /**
     * return the distance of the cell from the player. This is a stored value
     * it is not computed everytime. So the distance may be out of date if the
     * player moves.
     * 
     * @return the x-coordinate of the cell.
     */
    public int getDistance() {
        return distance;
    }

    /**
     * Set x-coordinate of the cell.
     */
    public void setX(int x) {
        this.x = x;
    }

    /**
     * Set y-coordinate of the cell.
     */
    public void setY(int y) {
        this.y = y;
    }

    /**
     * Set distance of the cell from the player. The validity of the value is
     * not checked so be cautious.
     */
    public void setDistance(int distance) {
        if (distance < 0) {
            throw new IllegalArgumentException();
        }
        this.distance = distance;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (!(obj instanceof Position)) {
            return false;
        }
        Position p = (Position) obj;
        return x == p.x && y == p.y && distance == p.distance;
    }
}
