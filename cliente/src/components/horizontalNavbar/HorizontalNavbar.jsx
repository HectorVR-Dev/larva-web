import React from 'react';
import { FaBars } from 'react-icons/fa';
import { MdOutlineSpaceDashboard } from "react-icons/md";
import { MdOutlineSettings } from "react-icons/md";
import { LuUserRound } from "react-icons/lu";
const HorizontalNavbar = ({ onToggle }) => {
    const hoverClasses = [
        'hover:text-white',
        'hover:bg-blue-800',
        'hover:shadow-lg',
        'transition-transform duration-200 ease-in-out',
        'hover:scale-105',
        'active:scale-95',
        'rounded',
        'p-2',
        'block',
    ].join(' ');

    return (
        <nav className="h-20 w-auto bg-white rounded-3xl text-black/40 p-4">
            <div className=" ml-1 container mx-auto flex justify-between items-center">
                {/* Botón de tres rayas (FaBars) */}
                <button
                    onClick={onToggle}
                    className="bg-blue-950 text-white p-2 rounded-full hover:bg-blue-800 transition-transform duration-200 ease-in-out hover:scale-110 active:scale-95"
                >
                    <FaBars className="text-xl" />
                </button>

                {/* Enlaces */}
                <ul className="flex space-x-2 sm:space-x-4">
                    <li>
                        <a href="#dashboard" className={`${hoverClasses} group flex items-center gap-0.5 sm:gap-1`}>
                            <MdOutlineSpaceDashboard className="text-gray-700 text-lg sm:text-2xl group-hover:text-white" />
                            Dashboard
                        </a>
                    </li>
                    <li>
                        <a href="#users" className={`${hoverClasses} group flex items-center gap-0.5 sm:gap-1`}>
                            <LuUserRound className="text-gray-700 text-lg sm:text-2xl group-hover:text-white" />
                            Users
                        </a>
                    </li>
                    <li>
                        <a href="#settings" className={`${hoverClasses} group flex items-center gap-0.5 sm:gap-1`}>
                            <MdOutlineSettings className="text-gray-700 text-lg sm:text-2xl group-hover:text-white" />
                            Settings
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default HorizontalNavbar;