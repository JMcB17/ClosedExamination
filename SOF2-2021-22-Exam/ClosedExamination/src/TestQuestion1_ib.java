import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestQuestion1_ib {

    MatchScore score = new MatchScore("Scotland", "France", 17, 36, 2, 6);

    @Test
    public void testGetAwayPoints() {
        assertEquals(36, score.getAwayPoints());
    }

    @Test
    public void testGetAwayTeam() {
		assertEquals("France", score.getAwayTeam());
    }

    @Test
    public void testGetAwayTries() {
        assertEquals(6, score.getAwayTries());
    }

    @Test
    public void testGetHomePoints() {
        assertEquals(17, score.getHomePoints());
    }

    @Test
    public void testGetHomeTeam() {
        assertEquals("Scotland", score.getHomeTeam());
    }

    @Test
    public void testGetHomeTries() {
        assertEquals(2, score.getHomeTries());
    }
}
