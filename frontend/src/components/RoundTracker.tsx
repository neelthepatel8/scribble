import React from "react";
import type { RoundTrackerProps } from "../types/RoundTrackerProps";
import './RoundTracker.css';

function RoundTracker({ icon, round}: RoundTrackerProps) {
  return (
    <div className="roundTrackerParent">
        
      <img className='iconParent' src={icon}/>

      <div className='textParent'>
      Round {round} of 3
      </div>
    </div>
  );
}

export default RoundTracker;
