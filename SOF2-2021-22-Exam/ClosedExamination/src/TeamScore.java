class TeamScore implements Comparable<TeamScore> {
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
    @Override
    public int compareTo(TeamScore other) {
        int[] ours = {points, pointDiff, triesScored};
        int[] theirs = {other.points, other.pointDiff, other.triesScored};
        for (int i = 0; i < 2; i++){
            if (ours[i] == theirs[i]) {
                continue;
            } else {
                return ours[i] < theirs[i] ? -1 : 1;
            }
        }
        return 0;
    }

    private boolean addMatchValues(int matchPoints, int matchTries, int otherPoints) {
        triesScored += matchTries;

        int matchPointDiff = matchPoints - otherPoints;
        pointDiff += matchPointDiff;

        if (otherPoints < matchPoints) {
            // win
            wins += 1;
            points += 4;
        } else if (matchPoints < otherPoints) {
            // loss
            // |  ||
            // || |_
            losses += 1;
            if (-7 <= matchPointDiff) {
                points += 1;
            }
        } else {
            // draw
            draws += 1;
            points += 2;
        }
        if (4 <= matchTries) {
            // you tried
            points += 1;
        }

        return true;
    }

    public boolean addMatch(MatchScore match) {
        if (match.homeTeam == name) {
            return addMatchValues(match.homePoints, match.homeTries, match.awayPoints);
        } else if (match.awayTeam == name) {
            return addMatchValues(match.awayPoints, match.awayTries, match.homePoints);
        } else {
            return false;
        }
    }
}
