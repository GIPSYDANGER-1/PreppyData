1. Data Cleaning Endpoint
--------------------------

**Description**  
Cleans the dataset according to user-defined options, including handling missing values, detecting outliers, and removing duplicates.

**Endpoint**  
``POST /cleaning``

**Request Format**  

.. admonition:: Request Headers
   :class: important

Content-Type: application/json Authorization: Bearer <your-api-token>

.. admonition:: Request Body (JSON)
   :class: important

.. container:: boxed

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

.. admonition:: Success (200 OK)
   :class: success

.. container:: boxed

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

.. admonition:: Error (400 Bad Request)
   :class: error

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "status": "error",
         "message": "Dataset URL is invalid or inaccessible."
      }

**Usage Example**  

.. admonition:: cURL Example
   :class: tip

.. container:: boxed

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
-----------------------------

**Description**  
Selects the most important features from the dataset using a user-defined algorithm.

**Endpoint**  
``POST /feature-selection``

**Request Format**  

.. admonition:: Request Headers
   :class: important

Content-Type: application/json Authorization: Bearer <your-api-token>

.. admonition:: Request Body (JSON)
   :class: important

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "dataset_url": "https://example.com/mydata.csv",
         "selection_method": "random_forest",
         "num_features": 5
      }

**Response Format**  

.. admonition:: Success (200 OK)
   :class: success

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "status": "success",
         "selected_features": ["feature_1", "feature_3", "feature_5", "feature_7", "feature_9"],
         "dataset_url_with_selected_features": "https://preppydata.com/processed/mydata_selected.csv"
      }

.. admonition:: Error (400 Bad Request)
   :class: error

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "status": "error",
         "message": "Selection method is invalid or unsupported."
      }

**Usage Example**  

.. admonition:: cURL Example
   :class: tip

.. container:: boxed

   .. code-block:: bash
      :linenos:

      curl -X POST https://api.preppydata.com/v1/feature-selection \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -d '{
         "dataset_url": "https://example.com/mydata.csv",
         "selection_method": "random_forest",
         "num_features": 5
      }'


3. Encoding Endpoint
---------------------

**Description**  
Converts categorical data into One-hot, Label, or Target encoding.

**Endpoint**  
``POST /encoding``

**Request Format**  

.. admonition:: Request Headers
   :class: important

Content-Type: application/json Authorization: Bearer <your-api-token>

.. admonition:: Request Body (JSON)
   :class: important

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "dataset_url": "https://example.com/mydata.csv",
         "encoding_type": "one_hot",
         "columns_to_encode": ["column1", "column2"]
      }

**Response Format**  

.. admonition:: Success (200 OK)
   :class: success

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "status": "success",
         "encoded_dataset_url": "https://preppydata.com/processed/mydata_encoded.csv"
      }

.. admonition:: Error (400 Bad Request)
   :class: error

.. container:: boxed

   .. code-block:: json
      :linenos:

      {
         "status": "error",
         "message": "Column names are invalid or missing in the dataset."
      }

**Usage Example**  

.. admonition:: cURL Example
   :class: tip

.. container:: boxed

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
-----------
.. admonition:: Error Codes Table
   :class: note

.. list-table::
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
