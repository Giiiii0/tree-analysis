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
```bash git clone <repository-url>```
```bash cd backend```
