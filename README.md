## Backend README
#### Title: Tree and Property Price Analysis Backend

### Description

This FastAPI-based backend provides an analysis of property prices categorized by the height of trees on their streets. It includes endpoints to fetch average property prices and identify properties on unknown streets.

### Features
* CORS Configuration: Enables secure communication with the React frontend.
* Endpoints:
    * `/average_prices`: Returns the average property prices for streets categorized as short, `tall`, or `unknown`.
    * `/unknown_properties`: Fetches properties that cannot be categorized as `short` or `tall`.
* Data Preprocessing:
    * Cleans property price data by removing currency symbols and converting values to floats.
    * Flattens nested tree data for easy categorization.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   bash cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API:
   * Localhost URL: `http://127.0.0.1:8000`

### Endpoints
1. GET `/`
   <br/> Returns a status message to confirm the server is running.
   <br/> Response:
   ```bash
   {"message": "FastAPI server for tree analysis is running!"}
   ```
