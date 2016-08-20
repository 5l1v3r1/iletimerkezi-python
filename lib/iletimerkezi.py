import requests
string = """
		<request>
        	<authentication>
                <username></username>
                <password></password>
        	</authentication>
        	<order>
	        	<sender>ILETI MRKZI</sender>
	        	<sendDateTime></sendDateTime>
	        	<message>
	        		<text><![CDATA[Test mesaj metni]]></text>
	        		<receipents>
	        			<number></number>
	        			<number></number>
	        		</receipents>
	        	</message>
        	</order>
        </request>""";

r = requests.post("http://api.iletimerkezi.com/v1/send-sms", data={'data': string})

print(r.status_code, r.reason)