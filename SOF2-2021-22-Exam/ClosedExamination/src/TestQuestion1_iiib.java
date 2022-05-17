import static org.junit.Assert.assertTrue;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.junit.Test;

public class TestQuestion1_iiib {

    @Test
    public void testGetRanking() {
        Set<String> teams = new HashSet<>();
        teams.add("New Zealand");
        teams.add("Australia");
        teams.add("South Africa");
        Championship triNations = new Championship(teams);
        triNations.table.clear();
        // The following three statements are equivalent to add the three matches:
        //    triNations.addMatch(new MatchScore("New Zealand", "Australia", 20, 13, 4, 1));
        //    triNations.addMatch(new MatchScore("South Africa", "New Zealand", 12, 10, 1, 1));
        //    triNations.addMatch(new MatchScore("Australia", "South Africa", 3, 14, 0, 2));
        //
        // This is done that way in case you were not able to implement correctly addMatch().
        triNations.table.add(createTeamScore("Australia", 0, 2, 0, 1, 1, -18));
        triNations.table.add(createTeamScore("South Africa", 2, 0, 0, 8, 3, 13));
        triNations.table.add(createTeamScore("New Zealand", 1, 1, 0, 6, 5, 5));

        List<TeamScore> ranking = triNations.getRanking();
        assertTrue(equals(ranking.get(0), createTeamScore("South Africa", 2, 0, 0, 8, 3, 13)));
        assertTrue(equals(ranking.get(1), createTeamScore("New Zealand", 1, 1, 0, 6, 5, 5)));
        assertTrue(equals(ranking.get(2), createTeamScore("Australia", 0, 2, 0, 1, 1, -18)));
    }

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
