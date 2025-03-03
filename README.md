# Gemini-2.0-in-Vertex-AI

## Enabling the API on Google Cloud Platform (GCP)

1.  **Go to the Google Cloud Console:** Navigate to [console.cloud.google.com](https://console.cloud.google.com/).
2.  **Select or Create a Project:** Choose the project where you want to enable the API. If you don't have one, create a new project.
3.  **Navigate to the API Library:** In the navigation menu, go to "APIs & Services" -> "Library".
4.  **Search for the API:** Search for the specific API your project requires ("Vertex AI API").
5.  **Select the API:** Click on the API you want to enable.
6.  **Enable the API:** Click the "Enable" button.
7.  **Create Service Account (if needed):** If your code needs to authenticate, create a service account and download its JSON key file. Go to "APIs & Services" -> "Credentials" -> "Create Credentials" -> "Service account".
8.  Go to service account section
<img width="1435" alt="Screenshot 2025-03-03 at 10 43 44 AM" src="https://github.com/user-attachments/assets/0c582d65-9111-460c-9986-c1b821292e1c" />
- Create service account 
<img width="1431" alt="Screenshot 2025-03-03 at 10 44 10 AM" src="https://github.com/user-attachments/assets/92b442f9-c7b6-40e5-a46a-9f611b858ac7" />
- Add the name
<img width="1440" alt="Screenshot 2025-03-03 at 10 44 47 AM" src="https://github.com/user-attachments/assets/79439f94-86c0-458d-9709-4f701402115c" />
- Selected the newly created service account
<img width="1439" alt="Screenshot 2025-03-03 at 10 47 58 AM" src="https://github.com/user-attachments/assets/177ab973-9b6b-4ec9-81da-21fb9e577ea2" />
- Go to keys section and choose add new key, download JSON file, save this JSON file we will use this further 
<img width="1440" alt="Screenshot 2025-03-03 at 10 48 30 AM" src="https://github.com/user-attachments/assets/ee05e4d5-36b0-4cdf-b622-2b90b0301354" />
- Next, Go to IAM section
<img width="1440" alt="Screenshot 2025-03-03 at 10 45 48 AM" src="https://github.com/user-attachments/assets/e9b749ae-479d-4dfd-9be5-26d68eb74e58" />
- Select Grant access
<img width="1440" alt="Screenshot 2025-03-03 at 10 46 17 AM" src="https://github.com/user-attachments/assets/27208002-fd4d-4eb9-ab77-562378094ddb" />
- Add the name of newly created Service account, also assing the roles to it ("Vertex AI Administrator", "Vertex AI Custom Code Service Agent", "Vertex AI Service Agent", "Vertex AI User")
<img width="1440" alt="Screenshot 2025-03-03 at 10 47 07 AM" src="https://github.com/user-attachments/assets/fad60fa0-5ba5-4b99-ba63-b8a877f7ee9b" />

9.  **Grant Service Account Permissions:** Grant the service account the necessary permissions to use the API.

## Python 3.13 Installation and Setup

### Windows

1.  **Download Python 3.13:** Go to the official Python website ([python.org](https://www.python.org/downloads/windows/)) and download the Windows installer for Python 3.13.
2.  **Run the Installer:** Execute the downloaded installer.
3.  **Check "Add Python 3.13 to PATH":** Ensure that the "Add Python 3.13 to PATH" checkbox is selected during installation. This is crucial for running Python from the command line.
4.  **Complete the Installation:** Follow the on-screen instructions to complete the installation.

### Linux (Ubuntu/Debian)

1.  **Update Package List:** Open a terminal and run:

    ```bash
    sudo apt update
    ```

2.  **Install Dependencies:** Install necessary dependencies:

    ```bash
    sudo apt install software-properties-common
    ```

3.  **Add deadsnakes PPA:** add the deadsnakes PPA to your system.
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```
4.  **Update Package List Again:**

    ```bash
    sudo apt update
    ```

5.  **Install Python 3.13:**

    ```bash
    sudo apt install python3.13
    ```

### macOS

1.  **Download Python 3.13:** Go to the official Python website ([python.org](https://www.python.org/downloads/macos/)) and download the macOS installer for Python 3.13.
2.  **Run the Installer:** Execute the downloaded installer.
3.  **Follow the Instructions:** Follow the on-screen instructions to complete the installation.

## Setting Environment Variables

### Linux/macOS

1.  **Open Terminal:** Open a terminal window.    ```

2.  **Add GCP Service Account Key (Optional):** If you're using a GCP service account from above step, rename your service account JSON file with name `creds.json` and put it inside this repo folder at root level:
3.  set necessary environment variables

    ```bash
    export CRED_PATH="./creds.json"
    export PROJECT_ID="[add-your-project-id]"
    ```

## Running the Python Code

1.  Clone the repo and enable the virtual environment

    ```bash
    git clone https://github.com/harsh4870/Gemini-2.0-in-Vertex-AI.git
    source venv/bin/activate
    ```

2.  Moment of truth

    ```bash
    python3 01-main.py
    ```
