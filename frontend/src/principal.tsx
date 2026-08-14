import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import { Aplicacao } from './aplicacao'
import './estilos.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Aplicacao />
  </StrictMode>,
)
