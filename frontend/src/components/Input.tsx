import type { InputProps } from "../types/InputProps";
import './Input.css';



function Input({placeholder, value, onChange}: InputProps) {

  const handleSubmit = (event: React.SubmitEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!value.trim()) {
      return;
    }
    onChange("");

  }
  
  return (
    <div className="inputParent">
      <form onSubmit={handleSubmit}>
        <input 
          className='inputContainer' 
          type='text' 
          placeholder={placeholder}
          value={value}
          onChange={(event) => onChange(event.target.value)}
        />
    </form>
    </div>
    )
}

export default Input;
