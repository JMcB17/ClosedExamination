public class MatchScore {
    String homeTeam;
    String awayTeam;
    int homePoints;
    int awayPoints;
    int homeTries;
    int awayTries;

    public MatchScore(
        String homeTeam,
        String awayTeam,
        int homePoints,
        int awayPoints,
        int homeTries,
        int awayTries
    ) {
        String[] teams = {homeTeam, awayTeam};
        for (String t : teams) {
            if (t == null) {
                throw new NullPointerException("Team names cannot be null.");
            }
        }
        int[] nums = {homePoints, awayPoints, homeTries, awayTries};
        for (int n: nums) {
            if (n < 0) {
                throw new IllegalArgumentException("Points and tries cannot be negative.");
            }
        }

        this.homeTeam = homeTeam;
        this.awayTeam = awayTeam;
        this.homePoints = homePoints;
        this.awayPoints = awayPoints;
        this.homeTries = homeTries;
        this.awayTries = awayTries;
    }


    
    /** Get the name of the home team as a String. */
    public String getHomeTeam() {
        return homeTeam;
    }
    /** Get the name of the away team as a String. */
    public String getAwayTeam() {
        return awayTeam;
    }
    /** Get the points scored by the home team as an int. */
    public int getHomePoints() {
        return homePoints;
    }
    /** Get the points scored by the away team as an int. */
    public int getAwayPoints() {
        return awayPoints;
    }
    /** Get the tries scored by the home team as an int. */
    public int getHomeTries() {
        return homeTries;
    }
    /** Get the tries scored by the away team as an int. */
    public int getAwayTries() {
        return awayTries;
    }
}
