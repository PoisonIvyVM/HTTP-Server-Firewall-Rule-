# HTTP-Server-Firewall-Rule-
This firewall server was created as part of a Forage job simulation
The script for this firewall was created to provide a basic layer of protection against a specific type of malware attack targeting vulnerabilities in web applications or servers. This attack involves sending crafted HTTP requests with specific headers and body content designed to manipulate the server into executing unauthorized commands, potentially compromising the server's security. The firewall inspects incoming HTTP POST requests for patterns indicative of this exploit, such as unusual headers ("suffix", "c1", "c2") and specific malicious payload patterns within the request body that attempt to exploit class loader vulnerabilities or execute Java code remotely.

By analyzing these request characteristics and blocking those that match the patterns of the exploit, the firewall aims to prevent attackers from exploiting the targeted vulnerabilities, thereby enhancing the security posture of the hosted web application or server environment. The script represents a rudimentary approach to identifying and mitigating a narrow range of attacks and serves as an illustrative example of how basic filtering and blocking mechanisms can be implemented in Python to counter specific security threats.

The repository that the malware code originates from: https://github.com/craig/SpringCore0day

When you run the test_request.py file, after loading your local port http://localhost:8000, you should get a status code response if successful: 200
If the firewall setup is successful, you should get the following response in the web page of port 8000: {"message": "Request allowed."}
Testrequest when run should also show [Errno 61] ConnectionRefusedError

The test_request.py script is from Forage 
