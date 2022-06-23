# Problem Link https://leetcode.com/problems/defanging-an-ip-address/

def defang_id_address(address):
    return address.replace('.', '[.]')


print(defang_id_address('255.100.50.0'))
