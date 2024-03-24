This is an e-commerce application developed using Django.

Follow the steps to run the application:

1. Clone app
   
    ```
      git clone https://github.com/kashaudhan/quickart.git
    ```
1. Create virtual env
   
    ```
    python -m venv .venv
    ```
2. start virtual env
  
    ```
    source .venv/bin/activate
    ```
    
3. install dependencies
   
    ```
    pip install -r requirements.txt
    ```


4. Run migrations
  
    ```
    python manage.py makemigrations
    ```

    ```
    python manage.py migrate
    ```
5. Start server

    ```
    python manage.py runserver
    ```
6. Visit URL

    `http://127.0.0.1:8000/`