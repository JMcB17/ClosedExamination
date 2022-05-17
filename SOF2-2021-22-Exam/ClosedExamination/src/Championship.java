import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class Championship {
    Set<String> teams;
    List<TeamScore> table;
    List<MatchScore> completedMatches;

    /**
     * Construct an instance of Championship given a set of teams' name.
     * 
     * @param teams The set of team taking part in the competition.
     * @throws IllegalArgumentException is the parameter teams is null or is
     *                                  empty set.
     */
    public Championship(Set<String> teams) {
        if (teams == null || teams.isEmpty()) {
            throw new IllegalArgumentException();
        }
        this.teams = teams;
        table = new ArrayList<>();
        completedMatches = new ArrayList<>();

        // Create instance of TeamScore for each team in the competition and
        // adds it to the table. The scores are all initialised to 0.
        for (String team : teams) {
            table.add(new TeamScore(team));
        }
    }

    /**
     * Finds and returns the score of a team. The method returns null if the team
     * does not exist (that is does not take part in the competition).
     * 
     * @param team The name of the team from which we want to retrieve the score
     * @return the TeamScore instance of the team passed in the parameter. Returns
     *         null if the team does not take part in the competition.
     */
    public TeamScore getTeamScore(String team) {
        for (TeamScore score : table) {
            if (score.name.equals(team)) {
                return score;
            }
        }
        return null;
    }

    /////////////// ADD YOUR CODE BELOW ///////////////

}
