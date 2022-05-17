import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class TestQuestion1_iib {

    @Test
    public void testAddMatchBonusTries() {
		TeamScore france = new TeamScore("France");
		assertEquals("France", france.name);
		assertEquals(0, france.wins);
		assertEquals(0, france.losses);
		assertEquals(0, france.draws);
		assertEquals(0, france.points);
		assertEquals(0, france.triesScored);
		assertEquals(0, france.pointDiff);

        assertTrue(france.addMatch(new MatchScore("France", "Italy", 37, 10, 5, 1)));
		assertEquals(1, france.wins);
		assertEquals(0, france.losses);
		assertEquals(0, france.draws);
		assertEquals(5, france.points);
		assertEquals(5, france.triesScored);
		assertEquals(27, france.pointDiff);

        assertTrue(france.addMatch(new MatchScore("Scotland", "France", 17, 36, 2, 6)));
		assertEquals(2, france.wins);
		assertEquals(0, france.losses);
		assertEquals(0, france.draws);
		assertEquals(10, france.points);
		assertEquals(11, france.triesScored);
		assertEquals(46, france.pointDiff);

    }

    @Test
    public void testAddMatchBonusLoosing() {
		TeamScore ireland = new TeamScore("Ireland");
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(0, ireland.points);
		assertEquals(0, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);

        assertTrue(ireland.addMatch(new MatchScore("France", "Ireland", 30, 24, 2, 4)));
		assertEquals(0, ireland.wins);
		assertEquals(1, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(2, ireland.points);
		assertEquals(4, ireland.triesScored);
		assertEquals(-6, ireland.pointDiff);

        assertTrue(ireland.addMatch(new MatchScore("Ireland", "Wales", 29, 7, 4, 1)));
		assertEquals(1, ireland.wins);
		assertEquals(1, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(7, ireland.points);
		assertEquals(8, ireland.triesScored);
		assertEquals(16, ireland.pointDiff);
    }

    @Test
    public void testAddMatchDraws() {
		TeamScore ireland = new TeamScore("Ireland");
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(0, ireland.points);
		assertEquals(0, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);

        assertTrue(ireland.addMatch(new MatchScore("Ireland", "Scotland", 29, 29, 4, 5)));
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(1, ireland.draws);
		assertEquals(3, ireland.points);
		assertEquals(4, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);

        assertTrue(ireland.addMatch(new MatchScore("Italy", "Ireland", 9, 9, 0, 0)));
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(2, ireland.draws);
		assertEquals(5, ireland.points);
		assertEquals(4, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);

    }

    @Test
    public void testAddMatchInvalidTeam() {
		TeamScore ireland = new TeamScore("Ireland");
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(0, ireland.points);
		assertEquals(0, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);

        assertFalse(ireland.addMatch(new MatchScore("Wales", "France", 9, 13, 0, 1)));
		assertEquals(0, ireland.wins);
		assertEquals(0, ireland.losses);
		assertEquals(0, ireland.draws);
		assertEquals(0, ireland.points);
		assertEquals(0, ireland.triesScored);
		assertEquals(0, ireland.pointDiff);
    }


}
