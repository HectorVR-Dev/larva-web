import React, { useState, useEffect } from 'react';
import { HiMiniArrowUturnLeft } from "react-icons/hi2";
import { LuMicroscope } from "react-icons/lu";
import { AiOutlineHome } from "react-icons/ai";
import { LuMousePointer2 } from "react-icons/lu";
import { LuContactRound } from "react-icons/lu";

const VerticalNavbar = ({ isVisible, onClose }) => {
    const [isMounted, setIsMounted] = useState(false);

    useEffect(() => {
        if (isVisible) {
            setIsMounted(true); // Activa la animación de entrada
        } else {
            setIsMounted(false); // Desactiva la animación de entrada
        }
    }, [isVisible]);

    // Clases para los efectos hover/active
    const hoverClasses = [
        'text-white/40',           // Color base
        'hover:text-white',         // Hover en desktop
        'active:text-white',        // Active en mobile
        'hover:bg-blue-800',
        'active:bg-blue-800',       // Active en mobile
        'transition-all',
        'transition-transform duration-300',
        'hover:scale-105',
        'active:scale-95',
        'rounded',
        'p-2',
        'block',
    ].join(' ');

    // Si no es visible, no renderiza nada
    if (!isVisible) return null;

    return (
        <nav
            className={`fixed inset-0 h-full w-1/2 p-4 bg-blue-950 text-white/40 sm:relative sm:w-48 md:w-64 sm:h-auto transition-transform duration-300 transform ${
                isMounted ? 'translate-x-0' : '-translate-x-full'
            } sm:translate-x-0`}
        >
            {/* Contenedor del título "Larva" */}
            <div className="w-full flex justify-center items-center p-4">
                <h2 className="text-2xl text-white font-extrabold flex items-center gap-2">
                    <LuMicroscope className="text-3xl" />
                    Larva
                </h2>
            </div>

            {/* Lista de enlaces */}
            <ul className="flex flex-col items-center space-y-4 mt-4">
                <li>
                    <a href="#inicio" className={`${hoverClasses} flex items-center gap-2`}>
                        <AiOutlineHome className="text-2xl" />
                        Inicio
                    </a>
                </li>
                <li>
                    <a href="#nosotros" className={`${hoverClasses} flex items-center gap-2`}>
                        <LuMousePointer2 className="text-2xl" />
                        Nosotros
                    </a>
                </li>
                
                <li>
                    <a href="#contacto" className={`${hoverClasses} flex items-center gap-2`}>
                        <LuContactRound className="text-2xl" />
                        Contacto
                    </a>
                </li>
            </ul>

            {/* Botón de cerrar */}
            <button
                onClick={onClose}
                className="absolute top-4 right-4 bg-blue-950 text-white p-2 rounded-full hover:bg-blue-800 active:bg-blue-800 transition-all duration-300 hover:scale-110 active:scale-110"
            >
                <HiMiniArrowUturnLeft className="text-xl" />
            </button>
        </nav>
    );
};

export default VerticalNavbar;