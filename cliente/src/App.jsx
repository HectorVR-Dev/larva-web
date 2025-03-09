import React, { useState } from "react";
import AppLayout from './components/AppLayout';
import HorizontalNavbar from './components/horizontalNavbar/HorizontalNavbar';


import WebRTCComponent from "./components/Webrtc/WebRTCComponent";


function App() {
    const [isNavbarVisible, setIsNavbarVisible] = useState(true);

    const handleToggleNavbar = () => {
        setIsNavbarVisible(!isNavbarVisible);
    };

    return (
        <AppLayout 
            isNavbarVisible={isNavbarVisible} 
            onToggleNavbar={handleToggleNavbar}
        >
            {/* Navbar horizontal (fijo en la parte superior) */}
            <HorizontalNavbar onToggle={handleToggleNavbar} />
            
            {/* Contenedor principal del contenido */}
            <div >
                {/* Componente de transmisión WebRTC  <VideoStream />*/}
                
                {/*<VideoStream />*/}
                <WebRTCComponent />
               
                
            </div>
        </AppLayout>
    );
}

export default App;