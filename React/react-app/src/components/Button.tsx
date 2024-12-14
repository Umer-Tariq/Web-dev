import React, { ReactNode } from 'react'

interface Props {
    children: ReactNode;
    onClick: () => void;
    color?: "primary" | "secondary" | "danger";
}

const Button = ({ children, onClick, color = "primary" } : Props) => {
  return (
    <button className={'btn btn-' + color} onClick={onClick}>{ children }</button>
  )
}

export default Button;