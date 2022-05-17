import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

import org.junit.Test;

public class TestQuestion2 {

    @Test
    public void testGetClosestResourceRequirementA() {
        int[][] map = {{0,2,1,0,0,0},
                       {0,1,1,0,0,0},
                       {0,0,0,0,0,0},
                       {1,1,0,0,1,1},
                       {0,1,0,0,0,0},
                       {0,1,0,0,0,2}};

        GameMap board = new GameMap(map);
        assertEquals(new Position(5,5,7), board.getClosestResource(3, 0));
        assertEquals(new Position(1,0,5), board.getClosestResource(2, 2));
    }

    @Test
    public void testGetClosestResourceRequirementB() {
        int[][] map = {{0,2,1,0,0,0},
                       {0,1,1,0,0,0},
                       {0,0,0,0,0,0},
                       {1,1,0,0,1,1},
                       {0,1,0,0,0,0},
                       {0,1,0,0,0,2}};

        GameMap board = new GameMap(map);
        assertEquals(new Position(1,0,0), board.getClosestResource(1, 0));
        assertEquals(new Position(5,5,0), board.getClosestResource(5, 5));
    }

    @Test
    public void testGetClosestResourceRequirementC() {
        int[][] map = {{0,2,1,0,0,0},
                       {0,1,1,0,0,0},
                       {0,0,0,0,0,0},
                       {1,1,0,0,1,1},
                       {0,1,0,0,0,0},
                       {0,1,0,0,0,2}};

        GameMap board = new GameMap(map);
        assertNull(board.getClosestResource(2, 0));
        assertNull(board.getClosestResource(5, 3));
        assertNull(board.getClosestResource(1, 4));
    }

    @Test
    public void testGetClosestResourceRequirementD() {
        int[][] map = {{0,2,1,0,0,0},
                       {0,1,1,0,0,0},
                       {0,0,0,0,0,0},
                       {1,1,0,0,1,1},
                       {0,1,0,0,0,0},
                       {0,1,0,0,0,2}};

        GameMap board = new GameMap(map);
        assertNull(board.getClosestResource(0, 4));
        assertNull(board.getClosestResource(0, 5));
    }
}
