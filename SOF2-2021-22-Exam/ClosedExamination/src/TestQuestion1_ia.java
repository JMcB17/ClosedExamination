import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestQuestion1_ia {


	@Test
	public void testConstructor() {
		MatchScore score = new MatchScore("France", "England", 25, 13, 3, 1);
		assertEquals("France", score.homeTeam);
		assertEquals("England", score.awayTeam);
		assertEquals(25, score.homePoints);
		assertEquals(13, score.awayPoints);
		assertEquals(3, score.homeTries);
		assertEquals(1, score.awayTries);
	}


	@Test(expected = IllegalArgumentException.class)
	public void testConstructorInvalidHomePoints() {
		MatchScore score = new MatchScore("France", "England", -1, 13, 3, 1);
	}

	@Test(expected = IllegalArgumentException.class)
	public void testConstructorInvalidAwayPoints() {
		MatchScore score = new MatchScore("France", "England", 25, -1, 3, 1);
	}

	@Test(expected = IllegalArgumentException.class)
	public void testConstructorInvalidHomeTries() {
		MatchScore score = new MatchScore("France", "England", 25, 13, -3, 1);
	}

	@Test(expected = IllegalArgumentException.class)
	public void testConstructorInvalidAwayTriess() {
		MatchScore score = new MatchScore("France", "England", 25, 13, 3, -1);
	}

	@Test(expected = NullPointerException.class)
	public void testConstructorInvalidHomeTeam() {
		MatchScore score = new MatchScore(null, "England", 25, 13, 3, 1);
	}

	@Test(expected = NullPointerException.class)
	public void testConstructorInvalidAwayTeam() {
		MatchScore score = new MatchScore("France", null, 25, 13, 3, 1);
	}

}
