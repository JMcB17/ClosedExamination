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

        int[] ours = {points, pointDiff, triesScored};
        int[] theirs = {otherTeam.points, otherTeam.pointDiff, otherTeam.triesScored};
        for (int i = 0; i < 2; i++){
            if (ours[i] == theirs[i]) {
                continue;
            } else {
                return ours[i] < theirs[i] ? -1 : 1;
            }
        }
        return 0;
    }
}
