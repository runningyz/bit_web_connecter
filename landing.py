import http.cookiejar
import urllib.request
import urllib.parse


#header information
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36


landing_address = 'http://10.0.0.55:801/srun_portal_pc.php'
user_name = 'your account here'
password = 'your password here'


def load_door_knob(head):
    cookie_jar = http.cookiejar.CookieJar()
    processor = urllib.request.HTTPCookieProcessor(cookie_jar)
    door_knob = urllib.request.build_opener(processor)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    door_knob.addheaders = header
    return door_knob


if __name__ == '__main__':
    web_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    open_the_door = load_door_knob(web_headers)
    post_dict = {
        'username': user_name,
        'password': password,
        'action': 'login',
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'save_me': '1',
        'ajax': '1'
    }
    post_data = urllib.parse.urlencode(post_dict).encode()
    op = open_the_door.open(landing_address, post_data)
    data = op.read()
    print(data.decode('utf8'))