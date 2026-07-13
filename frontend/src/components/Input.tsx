import type { InputProps } from "../types/InputProps";
import './Input.css';



function Input({placeholder}: InputProps) {
  return (
    <div className="inputParent">
        <input className='inputContainer' type='text' placeholder={placeholder}></input>
    </div>
    )
}

export default Input;
