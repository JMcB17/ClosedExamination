import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class TestQuestion1_iia {

	@Test
	public void testConstructor() {
		TeamScore score = new TeamScore("France");
		assertEquals("France", score.name);
		assertEquals(0, score.wins);
		assertEquals(0, score.losses);
		assertEquals(0, score.draws);
		assertEquals(0, score.points);
		assertEquals(0, score.triesScored);
		assertEquals(0, score.pointDiff);
	}

	@Test(expected = NullPointerException.class)
	public void testConstructorInvalidTeamName() {
		TeamScore score = new TeamScore(null);
	}

	@Test
	public void testCompareToByPoints() {
		TeamScore france = new TeamScore("France");
		TeamScore england = new TeamScore("England");
		TeamScore scotland = new TeamScore("Scotland");
		setupScore(france, 5, 0, 0, 25, 17, 68);
		setupScore(england, 2, 3, 0, 10, 8, 5);
		setupScore(scotland, 3, 2, 0, 9, 9, 6);
		assertTrue(france.compareTo(england) > 0);
		assertTrue(england.compareTo(france) < 0);
		assertTrue(france.compareTo(france) == 0);
		assertTrue(scotland.compareTo(england) < 0);
		assertTrue(england.compareTo(scotland) > 0);
	}

	@Test
	public void testCompareToByPointsDifference() {
		TeamScore england = new TeamScore("England");
		TeamScore scotland = new TeamScore("Scotland");
		setupScore(england, 2, 3, 0, 10, 8, 5);
		setupScore(scotland, 2, 3, 0, 10, 11, -29);
		assertTrue(scotland.compareTo(england) < 0);
		assertTrue(england.compareTo(scotland) > 0);
	}


	@Test
	public void testCompareToByTries() {
		TeamScore england = new TeamScore("England");
		TeamScore scotland = new TeamScore("Scotland");
		setupScore(england, 2, 3, 0, 10, 8, 5);
		setupScore(scotland, 2, 3, 0, 10, 11, 5);
		assertTrue(scotland.compareTo(england) > 0);
		assertTrue(england.compareTo(scotland) < 0);
	}

	@Test
	public void testCompareToEquals() {
		TeamScore england = new TeamScore("England");
		TeamScore scotland = new TeamScore("Scotland");
		setupScore(england, 2, 3, 0, 10, 8, 5);
		setupScore(scotland, 1, 3, 1, 10, 8, 5);
		assertTrue(scotland.compareTo(england) == 0);
		assertTrue(england.compareTo(scotland) == 0);
	}


	/**
	 * Convenience method to setupt quickly a team score object to be used for comparison.
	 * This allows the setup of a TeamScore without the use of addMatch in case it is not
	 * implemented correctly by the student.
	 * 
	 * @param score
	 * @param wins
	 * @param losses
	 * @param draws
	 * @param points
	 * @param triesScored
	 * @param pointDiff
	 */

	private void setupScore(TeamScore score,
			int wins,
			int losses,
			int draws,
			int points,
			int triesScored,
			int pointDiff) {
		score.wins = wins;
		score.losses = losses;
		score.draws = draws;
		score.points = points;
		score.pointDiff = pointDiff;
		score.triesScored = triesScored;
	}

}
