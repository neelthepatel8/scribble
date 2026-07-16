import React from "react";
import "./App.css";
import Title from "./components/Title";
import GuessBar from "./components/GuessBar";
import Chat from "./components/Chat";
import GameBoard from "./components/GameBoard";
import Leaderboard from "./components/Leaderboard";

function App() {
  return (
    <div className="appContainer">
      <Title icon="src/assets/logo.gif"/>

      <div className="gameContainer">
        <GuessBar children="" />
        
        <div className="gridContainer">
        <Leaderboard children=""/>
        <GameBoard children=""/>
        <div className="chatParent">
          <Chat children="" />
        </div>
        </div>
      </div>
    </div>
  );
}

export default App;
