
# DeviceIOT
## About The Project
DeviceIOT is used to add IOT devices it's associated sensors and push events to the sensors

### Prerequisites
Python 3.8

# Run Locally

### Installation steps
1. Checkout below mentioned repo on local.

   https://github.com/bedagkarabhijeet/device-iot.git


2. Update the config.json. If you are working on new DB use SQL script from Utilities\DBScripts\1642582742.sql to create table schema

4. Navigate to checkout location and from command prompt create and activate virtual environment using below command

    ##### python -m venv venv
    
    ##### venv\Scripts\activate

3. Open command prompt, navigate to checkout folder and run below command

    ##### pip install -r requirements.txt
4. Open command prompt,  navigate to checkout folder and run below command. This runs the app

    ##### uvicorn startup:app

# API documentation

Open browser and hit below url to open API documentation
    http://localhost:8000/docs
