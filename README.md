# chat-with-pdf
This app enables the user to chat with their own pdf file

This app uses LangChain to perform the prompting and conversation in the backend. In addition, as a frontend platform streamlit is used.

There are to main ways to use this app:

- **With Docker Container (Still in progress)**:

    To build and rnu the docker container, please navigate to the project directory where the ```Dockerfile```  exists, and do the following in the terminal:
    ```py
    docker buuild -t MY_IMAGE .                 # to build the docker container
    docker container run -p 85XX:8501 MY_IMAGE  # to run the docker container, where XX are adjustable to be a valid port
    ```
    Note that the port is adjustable, but make sure to choose an unlocated one.

    Having done this, the app will be running on the specified port, open a browser and type the following:
    ```py
    http://localhost:85XX/          # or
    http://127.0.0.1:85XX/          # Note the port is adjustable
    ```

- **Locally with Virtual Environment**

    Navigate to the project diretory, create a virtual environment using the command:
    ```py
    python -m venv env
    ```
    And activate it, using the command:
    ```py
    - source env/Scripts/activate   # for Windows in the git bash
    - source env/bin/activate       # for Linux and OSX
    ```

    Having done this, run the streamli app using the following command:
    ```py
    streamlit run app.py --server.port=85XX
    ```

## Streamlit Usage
Having done the previous steps, its time to chat. Follow the following steps, please.

1. Enter a valid OPENAI_API_KEY and press enter
2. Upload your file
3. In so being done, you can start chatting.

![Stremalit Frontend](https://github.com/sulaiman-shamasna/chat-with-pdf/blob/main/graphs/streamlit.PNG)
