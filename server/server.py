# librearies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import json
from typing import Dict

# Label: FastAPI App
"""
* Initializes the FastAPI application.
"""
app = FastAPI()

# Label: Middleware for CORS Configuration
"""
* Enables Cross-Origin Resource Sharing (CORS) to allow communication between
* the FastAPI backend and the React frontend running on a different origin.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Label: Load Tree Data
"""
* Reads the `city-trees.json` file and returns its contents as a dictionary.
"""
def load_tree_data() -> Dict:
    with open("city-trees.json", "r") as f:
        return json.load(f)

# Label: Load Property Data
"""
* Reads the `property-data.csv` file and preprocesses the data:
    - Removes non-ASCII characters from the 'Price' column.
    - Strips out currency symbols and commas, converting the column to floats.
"""
def load_property_data() -> pd.DataFrame:
    df = pd.read_csv("property-data.csv", encoding="ISO-8859-1")
    df["Price"] = df["Price"].str.replace(r"[^\x00-\x7F]", "", regex=True)  # Remove non-ASCII characters
    df["Price"] = df["Price"].str.replace(r"[€,]", "", regex=True).astype(float)  # Convert to float
    return df

# Label: Flatten Tree Data
"""
* Extracts street names from the nested structure of `city-trees.json`.
* Categorizes streets into `short` and `tall` based on tree height.
* Handles recursive extraction of street names from nested dictionaries.
"""
def flatten_tree_data(tree_data: Dict) -> Dict[str, list]:
    def extract_streets(data):
        streets = []
        for key, value in data.items():
            if isinstance(value, dict):
                streets.extend(extract_streets(value))  # Recursive extraction
            else:
                streets.append(key.lower())  # Add street name to the list
        return streets

    return {
        "short": extract_streets(tree_data.get("short", {})),
        "tall": extract_streets(tree_data.get("tall", {})),
    }

# Label: Normalize Street Name
"""
* Strips and converts street names to lowercase to ensure consistent comparison.
"""
def normalize_street_name(street_name: str) -> str:
    return street_name.strip().lower()

# Label: Categorize Street Name
"""
* Categorizes a street name into `short`, `tall`, or `unknown`:
    - Matches the normalized name against the lists of short and tall streets.
    - Logs street names that don't belong to either category.
"""
def categorize_street(street_name: str, short_streets: list, tall_streets: list) -> str:
    # Normalize street names
    normalized_short_streets = [s.lower().strip() for s in short_streets]
    normalized_tall_streets = [s.lower().strip() for s in tall_streets]

    normalized_street_name = street_name.lower().strip()

    if normalized_street_name in normalized_short_streets:
        return "short"
    elif normalized_street_name in normalized_tall_streets:
        return "tall"
    else:
        print(f"Unknown street detected: {street_name}")  # Log unknown streets
        return "unknown"

# Label: Home Endpoint
"""
* Provides a simple message to confirm the FastAPI server is running.
"""
@app.get("/")
def home():
    return {"message": "FastAPI server for tree analysis is running!"}

# Label: Average Prices Endpoint
"""
* Calculates the average property prices for streets categorized by tree height:
    - Loads and preprocesses tree and property data.
    - Categorizes streets into `short`, `tall`, or `unknown`.
    - Computes the mean price for each category and returns the results as JSON.
"""
@app.get("/average_prices")
def get_average_prices():
    tree_data = load_tree_data()
    property_data = load_property_data()
    flattened_tree_data = flatten_tree_data(tree_data)

    # Extract short and tall streets
    short_streets = flattened_tree_data["short"]
    tall_streets = flattened_tree_data["tall"]

    # Add 'Tree Category' column to property data
    property_data["Tree Category"] = property_data["Street Name"].apply(
        lambda x: categorize_street(x, short_streets, tall_streets)
    )

    # Calculate average prices
    average_prices = property_data.groupby("Tree Category")["Price"].mean().to_dict()

    return JSONResponse(content=average_prices)

# Label: Unknown Properties Endpoint
"""
* Identifies properties on streets that couldn't be categorized as `short` or `tall`:
    - Filters the property data to include only rows labeled as `unknown`.
    - Returns a JSON response with details of these properties.
"""
@app.get("/unknown_properties")
def get_unknown_properties():
    tree_data = load_tree_data()
    property_data = load_property_data()
    flattened_tree_data = flatten_tree_data(tree_data)

    # Extract short and tall streets
    short_streets = flattened_tree_data["short"]
    tall_streets = flattened_tree_data["tall"]

    # Add 'Tree Category' column to property data
    property_data["Tree Category"] = property_data["Street Name"].apply(
        lambda x: categorize_street(x, short_streets, tall_streets)
    )

    # Filter unknown properties
    unknown_properties = property_data[property_data["Tree Category"] == "unknown"]

    return JSONResponse(content=unknown_properties.to_dict(orient="records"))
