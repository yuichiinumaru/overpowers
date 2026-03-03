import ssl
import socket
import datetime
import sys

def get_cert_expiry(hostname, port=443):
    context = ssl.create_default_context()
    # Disable certificate validation if needed for internal services, 
    # but for expiry check it's better to keep it default or allow self-signed if specified.
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    with socket.create_connection((hostname, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert(binary_form=True)
            x509 = ssl.DER_cert_to_PEM_cert(cert)
            
            # Since getpeercert() with binary_form=True returns DER, 
            # and we need to parse it. 
            # Alternatively, use getpeercert() without binary_form if verify_mode is not CERT_NONE.
            
    # Redoing with validation enabled to get structured dict if possible, 
    # or just use OpenSSL-like parsing.
    
    context = ssl.create_default_context()
    # If it's an internal mTLS service, we might need to load CA or ignore verification
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE 

    with socket.create_connection((hostname, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # We get binary cert and parse it manually if verify_mode is NONE
            cert_der = ssock.getpeercert(binary_form=True)
            # For simplicity in this script, we'll try to get the dict by enabling validation 
            # or use a more robust parsing.
            
    # Actually, simpler way to get expiry without full validation:
    import OpenSSL
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_der)
    expiry_bytes = cert.get_notAfter()
    expiry_str = expiry_bytes.decode('ascii')
    # Format: YYYYMMDDhhmmssZ
    expiry_date = datetime.datetime.strptime(expiry_str, '%Y%m%d%H%M%SZ')
    return expiry_date

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_cert_expiry.py <hostname> [port]")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
        try:
            # Check if pyOpenSSL is installed
            try:
                import OpenSSL
            except ImportError:
                print("Error: pyOpenSSL is required. Install with 'pip install pyOpenSSL'")
                sys.exit(1)
                
            expiry = get_cert_expiry(host, port)
            now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
            days_left = (expiry - now).days
            print(f"Certificate for {host}:{port} expires on {expiry} UTC")
            print(f"Days left: {days_left}")
            if days_left < 30:
                print("WARNING: Certificate expires in less than 30 days!")
        except Exception as e:
            print(f"Error: {e}")
