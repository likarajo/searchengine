# Set up

1. [Install Elastic Search](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/brew.html)

2. Start ElasticSearch

  ```sh
  elasticsearch
  ```
  
  It runs on <http://localhost:9200/>

3. [Create React App](https://github.com/facebook/create-react-app)

  ```sh
  npx create-react-app <searchapp>
  cd <searchapp>
  ```

4. Create Flask API code `/api/api.py`

  ```sh
  mkdir api
  cd api
  vi api.py
  ```

5. Create and activate Virtual environment `/api/venv`
  
  ```sh
  python -m venv venv
  source venv/bin/activate
  ```

6. Install necessary python requirements

  ```sh
  pip3 install -r requirements.txt
  ```

7. Create Flask env file `/api/.flaskenv`

  ```sh
  vi .flaskenv
  ```

5. Update project config `/package.json`

  ```json
  {
    ...
    "scripts": {
        "start": "react-scripts start",
        "start-api": "cd api && venv/bin/flask run --no-debugger",
         ...
    }, 
    ...
    "proxy": "http://localhost:5000"
  }
  ```

  * scripts: start => starts React front end on 
  * scripts: start-api => starts Flask back end on <http://localhost:5000/>
	* proxy => The frontend will redirect any requests it does not recognize to the backend

6. Run the React Front End

  ```sh
  yarn start
  ```
  
  React front end runs on <http://localhost:3000/>

7. Run the Flask Back End
  
  ```sh
  yarn start-api
  ```

  Flask back end runs on <http://localhost:5000/>

8. Update required React app code in `src/App.js`