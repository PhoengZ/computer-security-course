from OpenSSL import crypto
import pem

def verify_chain_of_trust(cert_pem, trusted_cert_pems):
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
    # Create and fill a X509Store with trusted certs
    store = crypto.X509Store()
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)
        store.add_cert(trusted_cert)
    # Create a X509StoreContext with the cert and trusted certs
    # and verify the chain of trust
    store_ctx = crypto.X509StoreContext(store, certificate)
    # Returns None if certificate can be validated
    try:
        result = store_ctx.verify_certificate()
        if result is None:
            return True
        else:
            return False
    except crypto.X509StoreContextError as e:
        print(f"Verification error: {e}")
        return False

def verify(target_file, intermediate_files, ca_file='./ca-certificates.crt'):
    with open(target_file, 'r') as cert_file:
        cert = cert_file.read()
    
    # โหลด Root CAs จาก ca-certificates.crt
    pems = pem.parse_file(ca_file)
    trusted_certs = [str(mypem) for mypem in pems]

    # Loop เพิ่ม Intermediate CA ทั้งหมดที่มีเข้าไปใน trusted_certs
    for int_file in intermediate_files:
        with open(int_file, 'r') as f:
            trusted_certs.append(f.read())

    # สั่ง Verify ตรวจสอบสายโซ่ความเชื่อถือ
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print(f"Certificate verified: {target_file}")
    else:
        print(f"Certificate verification failed: {target_file}")
    return verified

if __name__ == '__main__':
    ca_file = './ca-certificates.crt'
    
    sites = [
        {
            "name": "www.chula.ac.th",
            "target": "./server_cer.pem",
            "intermediates": ["./intermediate.pem"]
        },
        {
            "name": "Twitter (x.com)",
            "target": "./x_server_cer.crt",
            "intermediates": ["./intermediate_x.pem", "./intermediate_x1.pem"]
        },
        {
            "name": "Google",
            "target": "./google_server_cer.crt",
            "intermediates": ["./intermediate_google.pem"]
        },
        {
            "name": "classdeedee.cloud.cp.eng.chula.ac.th",
            "target": "./cloud_cp_server_cer.crt",
            "intermediates": ["./intermediate_cloudcp.pem", "./intermediate_cloudcp1.pem"]
        }
    ]

    print("=" * 60)
    print("Starting Certificate Chain Verification for all sites")
    print("=" * 60)

    for site in sites:
        print(f"\n[+] Verifying: {site['name']}")
        is_valid = verify(
            target_file=site["target"],
            intermediate_files=site["intermediates"],
            ca_file=ca_file
        )
        if is_valid:
            print(f"--> Result: {site['name']} is VALID and VERIFIED")
        else:
            print(f"--> Result: {site['name']} FAILED verification")
    
    print("\n" + "=" * 60)
    print("All verifications completed.")
    print("=" * 60)