import React from "react";
import type { LeaderboardProps } from "../types/LeaderboardProps";
import './Leaderboard.css';

function Leaderboard({children} : LeaderboardProps) {
    return (
        <div className="leaderboardContainer">
            {children}
        </div>
    )
}

export default Leaderboard;