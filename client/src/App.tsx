// libraries
import React from 'react';

// custom components
import Chart from './components/Chart';

/**
 * The App component serves as the main entry point for the application,
 * rendering the header with the title and subtitle, and including the Chart component
 * which displays average property prices based on tree height.
 */
const App: React.FC = () => {
    return (
        <div className="container">
            <header>
                <h1>Tree Analysis: Do Taller Trees Mean Higher Prices?</h1>
                <h2>Average Property Prices by Tree Height</h2>
            </header>
            <main>
                <Chart />
            </main>
        </div>
    );
};

export default App;
