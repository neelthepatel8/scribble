import type { GameBoardProps } from "../types/GameBoardProps";
import './GameBoard.css';


function GameBoard({children} : GameBoardProps) {
    return (
        <div className="gameboardContainer">
            {children}
        </div>
    )
}

export default GameBoard;