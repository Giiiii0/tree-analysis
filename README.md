# Backend README
#### Title: Tree and Property Price Analysis Backend

### Description

This FastAPI-based backend provides an analysis of property prices categorized by the height of trees on their streets. It includes endpoints to fetch average property prices.

### Features
* CORS Configuration: Enables secure communication with the React frontend.
* Endpoints:
    * `/average_prices`: Returns the average property prices for streets categorized as `short` or `tall`.
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
   uvicorn server:app --reload
   ```
4. Access the API:
   * Localhost URL: `http://localhost:8000`

### Endpoints
1. GET `/`
   <br/> Returns a status message to confirm the server is running.
   <br/> Response:
   ```bash
   {"message": "FastAPI server for tree analysis is running!"}
   ```

2. GET `/average_prices`
   <br/> Fetches the average property prices for streets categorized as `short` or `tall`.
   <br/> Response:
   ```bash
      {
         "short":488981.6592828445,
         "tall":587800.3856725664
      }
   ```
   
# Frontend README
#### Title: Tree and Property Price Analysis Frontend

### Description

A React-based frontend visualizing property price data based on tree heights. It includes an interactive pie chart.

### Features
* Pie Chart Visualization:
   * Displays average property prices for `short` and `tall` tree categories.
* Responsive and Interactive Design:
   * Uses Recharts for dynamic data visualization.
 
### Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
4. Access the app:
   * Localhost URL: `http://localhost:3000`
  
### Key Components
1. Chart Component:
   * Fetches data from the backend `/average_prices`
   * Displays property price data in an interactive pie chart.
2. Axios Integration:
   * Communicates with the backend API to fetch and display data dynamically.
3. Error Handling:
   * Logs errors for failed API requests.

# GitHub Repository Structure
```bash
root/
├── mongoDB/
├── client/
│   ├── public/
│   ├── src/
│   ├── .env
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── tailwind.config.js
├── server/
│   ├── configs/
│   ├── controllers/
│   ├── functions/
│   ├── middlewares/
│   ├── models/
│   ├── routes/
│   ├── .env
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
│── .dockerignore
│── docker-compose.yaml
└── README.md
```
