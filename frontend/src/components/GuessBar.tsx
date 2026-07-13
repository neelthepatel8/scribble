import type { GuessBarProps } from "../types/GuessBarProps";
import './GuessBar.css';

function GuessBar({ children } : GuessBarProps ) {
    return (
        <div className='guessBarContainer'>
            {children}
        </div>
    )
}

export default GuessBar;