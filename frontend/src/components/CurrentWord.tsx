import type { CurrentWordProps } from "../types/CurrentWordProps";

function currentWord({word, title}: CurrentWordProps) {
    const e = []; 
   
    for (let i = 0; i < word.length; i++) {
        e.push("_");
    }

    return (


        <div className='currentWordParent'>
            {title}
            {word}
        </div>
    )
}

export default currentWord;