import socket

def get_ipv4_address():
    """Retrieves the local IPv4 address.

    Returns:
        str: The local IPv4 address if successful, None otherwise.
    """

    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to a remote server (doesn't actually send any data)
        s.connect(("8.8.8.8", 80))

        # Get the local IP address
        ipv4_address = s.getsockname()[0]

        return ipv4_address

    except (socket.error, OSError) as e:
        if isinstance(e, OSError) and e.errno == 98:  # Address in use
            print(f"Warning: Error occurred (address in use): {e}")
            return None  # Indicate non-fatal error
        else:
            print(f"Error occurred: {e}")
            return None

    finally:
        # Close the socket to release resources
        s.close()

if __name__ == "__main__":
    ip_address = get_ipv4_address()
    if ip_address:
        print(f"Your local IPv4 address is: {ip_address}")
    else:
        print("Unable to determine your local IPv4 address.")
