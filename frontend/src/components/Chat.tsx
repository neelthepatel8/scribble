import type { ChatProps } from "../types/ChatProps";
import './Chat.css';
import Input from "./Input";

function Chat({ children }: ChatProps) {
    return (
        <div className='chatContainer'>
            {children}
            <Input placeholder="Type your guess here.."/>
        </div>
    )
}

export default Chat;