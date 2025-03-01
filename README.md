# Gemini-2.0-in-Vertex-AI

## Enabling the API on Google Cloud Platform (GCP)

1.  **Go to the Google Cloud Console:** Navigate to [console.cloud.google.com](https://console.cloud.google.com/).
2.  **Select or Create a Project:** Choose the project where you want to enable the API. If you don't have one, create a new project.
3.  **Navigate to the API Library:** In the navigation menu, go to "APIs & Services" -> "Library".
4.  **Search for the API:** Search for the specific API your project requires (e.g., "Cloud Vision API", "Cloud Natural Language API").
5.  **Select the API:** Click on the API you want to enable.
6.  **Enable the API:** Click the "Enable" button.
7.  **Create Service Account (if needed):** If your code needs to authenticate, create a service account and download its JSON key file. Go to "APIs & Services" -> "Credentials" -> "Create Credentials" -> "Service account".
8.  **Grant Service Account Permissions:** Grant the service account the necessary permissions to use the API.

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

2.  **Add GCP Service Account Key (Optional):** If you're using a GCP service account, add the following line, replacing `/path/to/your/service-account-key.json` with the actual path to your key file:

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
