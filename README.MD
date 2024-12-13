# Install Python Version 3.9
## use conda to create venv and install python 3.9
```bash
    conda create -p ./env python=3.9 -y
    conda activate ./env
```
## Install Required Libraries
```bash
    pip install -r requirements.txt
```

## Follow below setps for setup Rasa

1. Install Required Python Packages
2. Init Rasa by running the following command: `rasa init`
3. For inital setup say Y to all the options
4. Train the Rasa model by running the following command: `rasa train`
5. Start the Rasa server by running the following command: `rasa run`
6. Start the Rasa action server by running the following command: `rasa run actions`
7. Start the Rasa interactive learning session by running the following command: `rasa interactive`
8. Start the Rasa shell by running the following command: `rasa shell`
9. Start the Rasa server and action server by running the following command: `rasa run -m models --enable-api --cors "*" --debug`

