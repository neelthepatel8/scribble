import React from "react";
import type { SettingsProps } from "../types/SettingsProps";
import './Settings.css';

function Settings({icon} : SettingsProps) {

    return (
        <div className='settingsParent'>
        <img className='iconParent' src={icon}/>
        </div>
    )
}

export default Settings;