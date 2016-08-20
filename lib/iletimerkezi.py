import requests
string = """
		<request>
        	<authentication>
                <username>5057023101</username>
                <password>654321</password>
        	</authentication>
        	<order>
	        	<sender>ILETI MRKZI</sender>
	        	<sendDateTime></sendDateTime>
	        	<message>
	        		<text><![CDATA[Hop ki uc bes]]></text>
	        		<receipents>
	        			<number>5057023100</number>
	        			<number>5354104818</number>
	        		</receipents>
	        	</message>
        	</order>
        </request>""";

r = requests.post("http://api.iletimerkezi.com/v1/send-sms", data={'data': string})

print(r.status_code, r.reason)