API Reference
=============

This section describes the available API endpoints, request/response formats, and usage examples for Preppy Data.

Base URL
--------
https://preppydata.readthedocs.io/

1. Data Cleaning Endpoint
--------------------------
**Description**  
Cleans the dataset according to user-defined options, including handling missing values, detecting outliers, and removing duplicates.

**Endpoint**  
```
POST /cleaning
```

**Request Format**  
**Headers**  
```
Content-Type: application/json
Authorization: Bearer <your-api-token>
```

**Body (JSON)**  
.. code-block:: json
   :linenos:

   {
     "dataset_url": "https://example.com/mydata.csv",
     "cleaning_options": {
       "handle_missing": "mean", 
       "detect_outliers": true,
       "remove_duplicates": true
     }
   }

**Response Format**  
**Success (200 OK)**  
.. code-block:: json
   :linenos:

   {
     "status": "success",
     "cleaned_dataset_url": "https://preppydata.com/cleaned/mydata_cleaned.csv",
     "summary": {
       "rows_removed": 5,
       "missing_values_handled": true,
       "outliers_detected": 12
     }
   }

**Error (400 Bad Request)**  
.. code-block:: json
   :linenos:

   {
     "status": "error",
     "message": "Dataset URL is invalid or inaccessible."
   }

**Usage Example**  
.. code-block:: bash
   :linenos:

   curl -X POST https://api.preppydata.com/v1/cleaning \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer YOUR_API_TOKEN" \
   -d '{
     "dataset_url": "https://example.com/mydata.csv",
     "cleaning_options": {
       "handle_missing": "mean", 
       "detect_outliers": true,
       "remove_duplicates": true
     }
   }'


2. Feature Selection Endpoint
-------------------------------
**Description**  
Selects the most important features from the dataset using a user-defined algorithm.

**Endpoint**  
```
POST /feature-selection
```

**Request Format**  
**Headers**  
```
Content-Type: application/json
Authorization: Bearer <your-api-token>
```

**Body (JSON)**  
.. code-block:: json
   :linenos:

   {
     "dataset_url": "https://example.com/mydata.csv",
     "selection_method": "random_forest",
     "num_features": 5
   }

**Response Format**  
**Success (200 OK)**  
.. code-block:: json
   :linenos:

   {
     "status": "success",
     "selected_features": ["feature_1", "feature_3", "feature_5", "feature_7", "feature_9"],
     "dataset_url_with_selected_features": "https://preppydata.com/processed/mydata_selected.csv"
   }

**Error (400 Bad Request)**  
.. code-block:: json
   :linenos:

   {
     "status": "error",
     "message": "Selection method is invalid or unsupported."
   }

**Usage Example**  
```
curl -X POST https://api.preppydata.com/v1/feature-selection \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_TOKEN" \
-d '{
  "dataset_url": "https://example.com/mydata.csv",
  "selection_method": "random_forest",
  "num_features": 5
}'
```

3. Encoding Endpoint
---------------------
**Description**  
Converts categorical data into One-hot, Label, or Target encoding.

**Endpoint**  
```
POST /encoding
```

**Request Format**  
**Headers**  
```
Content-Type: application/json
Authorization: Bearer <your-api-token>
```

**Body (JSON)**  
.. code-block:: json
   :linenos:

   {
     "dataset_url": "https://example.com/mydata.csv",
     "encoding_type": "one_hot",
     "columns_to_encode": ["column1", "column2"]
   }

**Response Format**  
**Success (200 OK)**  
.. code-block:: json
   :linenos:

   {
     "status": "success",
     "encoded_dataset_url": "https://preppydata.com/processed/mydata_encoded.csv"
   }

**Error (400 Bad Request)**  
.. code-block:: json
   :linenos:

   {
     "status": "error",
     "message": "Column names are invalid or missing in the dataset."
   }

**Usage Example**  
.. code-block:: bash
   :linenos:

   curl -X POST https://api.preppydata.com/v1/encoding \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer YOUR_API_TOKEN" \
   -d '{
     "dataset_url": "https://example.com/mydata.csv",
     "encoding_type": "one_hot",
     "columns_to_encode": ["column1", "column2"]
   }'

Error Codes
------------
.. list-table:: Error Codes
   :header-rows: 1

   * - Code
     - Message
     - Description
   * - 400
     - Bad Request
     - The request parameters are invalid or missing.
   * - 401
     - Unauthorized
     - The API token is invalid.
   * - 500
     - Internal Server Error
     - An unexpected error occurred on the server.