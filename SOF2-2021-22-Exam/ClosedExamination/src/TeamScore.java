class TeamScore implements Comparable {
    String name;
    int wins;
    int losses;
    int draws;
    int points;
    int triesScored;
    int pointDiff;

    public TeamScore(String name) {
        if (name == null) {
            throw new NullPointerException("Team name cannot be null.");
        }

        this.name = name;
        // All int attributes should start as 0, and are left as default.
    }

    // https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html
    public int compareTo(Object object) {
        if (object == null) {
            throw new NullPointerException("Team to compare cannot be null.");
        }
        if (!(object instanceof TeamScore)) {
            throw new ClassCastException("Can only compare to another TeamScore object.")
        }

        TeamScore otherTeam = (TeamScore) object;

        if (otherTeam.points < points) {
            return 1;
        }
        else if (points < otherTeam.points) {
            return -1;
        }
        else if (otherTeam.pointDiff < pointDiff) {
            return 1;
        }
        else if (pointDiff < otherTeam.pointDiff) {
            return -1;
        }
        else if (otherTeam.triesScored < triesScored) {
            return 1;
        }
        else if (pointDiff < otherTeam.pointDiff) {
            return -1;
        }
        else {
            return 0;
        }
    }
}
