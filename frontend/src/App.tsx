import React from 'react'
import './App.css'
import bgImage from'./assets/scribble-bg.png'
import Title from './components/Title'

function App() {

  return (
    <div 
      className='appContainer'
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        width: '100%',
      }}
    >
      
        <Title icon="src/assets/skribble-title.png"/>
      <div 
        className='gameContainer'
      >
        {/* <Title icon="src/assets/skribble-title.png"/> */}
      </div>
      
      
    </div>
  )
}

export default App
