import React from 'react';
import { FaBars, FaTimes } from 'react-icons/fa';

const ToggleNavbarButton = ({ isNavbarVisible, onToggle, isHorizontal }) => {
    return (
        <button
            onClick={onToggle}
            className={`bg-blue-950 text-white p-2 rounded-full hover:bg-blue-800 transition duration-300 ${
                isHorizontal ? 'fixed top-4 left-4 z-50' : 'fixed bottom-4 left-4'
            }`}
        >
            {isHorizontal ? <FaBars className="text-xl" /> : <FaTimes className="text-xl" />}
        </button>
    );
};

export default ToggleNavbarButton;