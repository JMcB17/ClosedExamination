import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.HashSet;
import java.util.Set;

import org.junit.Test;

public class TestQuestion1_iiia {

    @Test
    public void testAddValidMatch() {
        Set<String> teams = new HashSet<>();
        teams.add("New Zealand");
        teams.add("Australia");
        teams.add("South Africa");
        Championship triNations = new Championship(teams);
        assertTrue(triNations.addMatch(new MatchScore("New Zealand", "Australia", 20, 13, 4, 1)));
        assertTrue(triNations.addMatch(new MatchScore("South Africa", "New Zealand", 12, 10, 1, 1)));
        assertTrue(triNations.addMatch(new MatchScore("Australia", "South Africa", 3, 14, 0, 2)));

        assertTrue(equals(triNations.getTeamScore("South Africa"),
                createTeamScore("South Africa", 2, 0, 0, 8, 3, 13)));
        assertTrue(equals(triNations.getTeamScore("New Zealand"),
                createTeamScore("New Zealand", 1, 1, 0, 6, 5, 5)));
        assertTrue(equals(triNations.getTeamScore("Australia"),
                createTeamScore("Australia", 0, 2, 0, 1, 1, -18)));
    }

    @Test
    public void testAddValidTwoLegsMatches() {
        Set<String> teams = new HashSet<>();
        teams.add("New Zealand");
        teams.add("Australia");
        teams.add("South Africa");
        Championship triNations = new Championship(teams);
        // adds first leg match
        assertTrue(triNations.addMatch(new MatchScore("New Zealand", "Australia", 20, 13, 4, 1)));

        // adds second leg match
        assertTrue(triNations.addMatch(new MatchScore("Australia", "New Zealand", 12, 10, 1, 1)));

        assertTrue(equals(triNations.getTeamScore("South Africa"),
                createTeamScore("South Africa", 0, 0, 0, 0, 0, 0)));
        assertTrue(equals(triNations.getTeamScore("New Zealand"),
                createTeamScore("New Zealand", 1, 1, 0, 6, 5, 5)));
        assertTrue(equals(triNations.getTeamScore("Australia"),
                createTeamScore("Australia", 1, 1, 0, 5, 2, -5)));
    }

    @Test
    public void testAddInvalidMatch() {
        Set<String> teams = new HashSet<>();
        teams.add("New Zealand");
        teams.add("Australia");
        teams.add("South Africa");
        Championship triNations = new Championship(teams);
        assertTrue(triNations.addMatch(new MatchScore("New Zealand", "Australia", 20, 13, 4, 1)));
        assertTrue(triNations.addMatch(new MatchScore("South Africa", "New Zealand", 12, 10, 1, 1)));
        assertTrue(triNations.addMatch(new MatchScore("Australia", "South Africa", 3, 14, 0, 2)));

        assertFalse(triNations.addMatch(new MatchScore("New Zealand", "Australia", 15, 3, 0, 0)));
        assertFalse(triNations.addMatch(new MatchScore("New Zealand", "France", 15, 23, 2, 4)));
        assertFalse(triNations.addMatch(new MatchScore("France", "Australia", 18, 3, 3, 0)));

        assertTrue(equals(triNations.getTeamScore("South Africa"),
                createTeamScore("South Africa", 2, 0, 0, 8, 3, 13)));
        assertTrue(equals(triNations.getTeamScore("New Zealand"),
                createTeamScore("New Zealand", 1, 1, 0, 6, 5, 5)));
        assertTrue(equals(triNations.getTeamScore("Australia"),
                createTeamScore("Australia", 0, 2, 0, 1, 1, -18)));
    }

    // Convenience methods used to facilitate testing. DO NOT MODIFY

    /**
     * Convenience method to check that too TeamScore instances are equals. Used to
     * simplify the code.
     * 
     * @param a
     * @param b
     * @return
     */
    private boolean equals(TeamScore a, TeamScore b) {
        return (a.name.equals(b.name) && a.wins == b.wins && a.losses == b.losses
                && a.draws == b.draws && a.points == b.points
                && a.triesScored == b.triesScored && a.pointDiff == b.pointDiff);
    }

    /**
     * Convenience method to create a new instance of TeamScore and initialise 
     * the attributes with specific values.
     *  
     * @param name
     * @param wins
     * @param losses
     * @param draws
     * @param points
     * @param triesScored
     * @param pointDiff
     * @return
     */
    private TeamScore createTeamScore(String name,
            int wins,
            int losses,
            int draws,
            int points,
            int triesScored,
            int pointDiff) {
        TeamScore score = new TeamScore(name);
        score.wins = wins;
        score.losses = losses;
        score.draws = draws;
        score.points = points;
        score.pointDiff = pointDiff;
        score.triesScored = triesScored;
        return score;
    }

}
