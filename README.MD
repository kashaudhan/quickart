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


To run app using docker use the following command

```
docker-compose build && docker-compose up
```


To see demo video click [here](https://www.loom.com/share/b6457a61d43649bcaf7fc8de3123bea8?sid=e4431a3f-f24a-4403-b72f-64176b056c89)