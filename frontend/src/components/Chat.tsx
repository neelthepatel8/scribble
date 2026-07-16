import type { ChatProps } from "../types/ChatProps";
import './Chat.css';
import Input from "./Input";
import React, { useState} from "react";


function Chat({ children }: ChatProps) {
    const [message, setMessage] = useState("");

    return (
        <div className='chatContainer'>
            {children}
            <Input 
            placeholder="Type your guess here.."
            value={message}
            onChange={setMessage}
            />
        </div>
    )
}

export default Chat;