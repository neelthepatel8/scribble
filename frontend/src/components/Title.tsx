import React from "react";
import type { TitleProps } from "../types/TitleProps";
import './Title.css';

function Title({icon}: TitleProps) {
    return (
        <div className='titleContainer'>
        <img src={icon}/>
        </div>
    )
}

export default Title;