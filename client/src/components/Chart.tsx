// libraries
import React, { useEffect, useState } from "react";
import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";
import axios from "axios";

// Label: Tree Data Interface
/**
 * Represents the structure of data used for tree categorization in the pie chart.
 * - `name`: The category of trees (e.g., Short Trees, Tall Trees, Unknown).
 * - `value`: The average property price for the corresponding category.
 */
interface TreeData {
    name: string;
    value: number;
}

// Label: Property Data Interface
/**
 * Represents the structure of individual property data.
 * - `Address`: The full address of the property.
 * - `Street Name`: The name of the street where the property is located.
 * - `Price`: The price of the property in euros.
 */
interface PropertyData {
    Address: string;
    "Street Name": string;
    Price: number;
}

// Label: Chart Component
/**
 * The `Chart` component fetches and visualizes property price data
 * categorized by tree heights (`short`, `tall`, `unknown`) in a pie chart.
 * It also fetches and optionally displays properties categorized as `unknown`.
 */
const Chart: React.FC = () => {
    const [data, setData] = useState<TreeData[]>([]);
    const [unknownProperties, setUnknownProperties] = useState<PropertyData[]>([]);
    const COLORS = ["#8884d8", "#82ca9d", "#ffc658"]; // Colors for pie chart slices

    // Label: Fetch Chart Data
    /**
     * Fetches average property prices for streets with short, tall, and unknown trees.
     * Transforms the API response into a format compatible with the Recharts library.
     */
    useEffect(() => {
        const fetchChartData = async () => {
            try {
                const response = await axios.get("http://localhost:8000/average_prices");
                const formattedData: TreeData[] = Object.entries(response.data).map(([key, value]) => ({
                    name: key === "short" ? "Short Trees" : key === "tall" ? "Tall Trees" : "Unknown",
                    value: Number(value), // Ensure the value is numeric
                }));
                setData(formattedData);
            } catch (error) {
                console.error("Error fetching chart data:", error);
            }
        };

        // Label: Fetch Unknown Properties
        /**
         * Fetches properties categorized as `unknown` by the backend.
         * These properties are displayed separately for further analysis.
         */
        const fetchUnknownProperties = async () => {
            try {
                const response = await axios.get("http://localhost:8000/unknown_properties");
                setUnknownProperties(response.data);
            } catch (error) {
                console.error("Error fetching unknown properties:", error);
            }
        };

        fetchChartData();
        fetchUnknownProperties();
    }, []);

    return (
        <div style={{ padding: "20px" }}>
            {/* Label: Pie Chart Visualization */}
            {/**
             * Renders a pie chart using Recharts to display average property prices.
             * Each slice represents streets categorized by tree height (`short`, `tall`, `unknown`).
            */}
            {data.length > 0 ? (
                <PieChart width={800} height={400}>
                    <Pie
                        data={data}
                        dataKey="value"
                        nameKey="name"
                        cx="50%"
                        cy="50%"
                        outerRadius={120}
                        fill="#8884d8"
                        label={({ name, value }) => `${name}: €${value.toLocaleString()}`}
                    >
                        {data.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                    </Pie>
                    <Tooltip formatter={(value: number) => `€${value.toLocaleString()}`} />
                    <Legend />
                </PieChart>
            ) : (
                <p>Loading data...</p> // Display a loading message while fetching data
            )}
        </div>
    );
};

export default Chart;