import React from 'react';
import VerticalNavbar from '../components/verticalNavbar/VerticalNavbar';

const AppLayout = ({ children, isNavbarVisible, onToggleNavbar }) => {
    return (
        <div className="flex flex-col h-screen">
            <div className="flex flex-1 overflow-hidden">
                {/* Navbar vertical */}
                <VerticalNavbar isVisible={isNavbarVisible} onClose={onToggleNavbar} />

                {/* Contenido principal */}
                <main className={`flex-1 bg-gray-300 transition-all duration-300 ${isNavbarVisible ? 'ml-0' : 'ml-0'} overflow-y-auto`}>
                    {/* Contenido principal */}
                    <div className="p-4">
                        {children}
                    </div>
                </main>
            </div>
        </div>
    );
};

export default AppLayout;