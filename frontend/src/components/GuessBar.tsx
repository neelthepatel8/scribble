import type { GuessBarProps } from "../types/GuessBarProps";
import './GuessBar.css';
import RoundTracker from "./RoundTracker";
import Settings from "./Settings";

function GuessBar({ children } : GuessBarProps ) {
    return (
        <div className='guessBarContainer'>
            {children}
            <RoundTracker 
                icon="src/assets/empty-clock.gif"
                round={1}
                />
            <Settings icon="src/assets/settings.gif"/>
        </div>
    )
}

export default GuessBar;