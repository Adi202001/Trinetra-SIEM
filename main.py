import subprocess
import os

def initiate_receiver():
    server_folder = os.path.join(os.path.dirname(__file__), 'server')
    receiver_script = os.path.join(server_folder, 'receiver.py')

    try:
        subprocess.run(['python', receiver_script], cwd=server_folder, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while initiating receiver.py: {e}")

if __name__ == '__main__':
    initiate_receiver()
