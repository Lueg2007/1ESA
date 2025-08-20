import React from 'react'

function Home() {
  return (
    <>
      <div style={{
        width: '100vw',
        display: 'flex',
        justifyContent: 'center',
      }}>
        <div>
          <div style={{
            width: '80vw',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
            <h2>Seja bem-vindo!!!</h2>
            <p>Expresse aqui seus pensamentos e opiniões</p>
          </div>

          <div style={{
            width: '80vw',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
            <img
              src="https://i.pinimg.com/736x/b9/85/49/b985497307000e027726b7615dbc63d2.jpg"
              alt="Imagem Shaders"
            />
          </div>
        </div>
      </div>
    </>
  )
}

export default Home
