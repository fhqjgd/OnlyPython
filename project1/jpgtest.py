import httplib, ssl, urllib2, socket,re,urllib,time_myself
from multiprocessing import Pool
class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)
        except ssl.SSLError, e:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)


class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)

if __name__ == '__main__':
    a = ['http://cl.fatt.pw/htm_data/16/1402/2268779.html', 'http://cl.fatt.pw/htm_data/16/1402/2268779.html', 'http://cl.fatt.pw/htm_data/16/1110/622028.html', 'http://cl.fatt.pw/htm_data/16/1110/622028.html', 'http://cl.fatt.pw/htm_data/16/1109/594741.html', 'http://cl.fatt.pw/htm_data/16/1109/594741.html', 'http://cl.fatt.pw/htm_data/16/1106/524942.html', 'http://cl.fatt.pw/htm_data/16/1106/524942.html', 'http://cl.fatt.pw/htm_data/16/0907/344501.html', 'http://cl.fatt.pw/htm_data/16/0907/344501.html', 'http://cl.fatt.pw/htm_data/16/0805/136474.html', 'http://cl.fatt.pw/htm_data/16/0805/136474.html', 'http://cl.fatt.pw/htm_data/16/1704/2165945.html', 'http://cl.fatt.pw/htm_data/16/1704/2165945.html', 'http://cl.fatt.pw/htm_data/16/1704/1608357.html', 'http://cl.fatt.pw/htm_data/16/1704/1608357.html', 'http://cl.fatt.pw/htm_data/16/1703/2284010.html', 'http://cl.fatt.pw/htm_data/16/1703/2284010.html', 'http://cl.fatt.pw/htm_data/16/1703/2274814.html', 'http://cl.fatt.pw/htm_data/16/1703/2274814.html', 'http://cl.fatt.pw/htm_data/16/1703/2274133.html', 'http://cl.fatt.pw/htm_data/16/1703/2274133.html', 'http://cl.fatt.pw/htm_data/16/1703/2273749.html', 'http://cl.fatt.pw/htm_data/16/1703/2273749.html', 'http://cl.fatt.pw/htm_data/16/1703/2273092.html', 'http://cl.fatt.pw/htm_data/16/1703/2273092.html', 'http://cl.fatt.pw/htm_data/16/1703/2272757.html', 'http://cl.fatt.pw/htm_data/16/1703/2272757.html', 'http://cl.fatt.pw/htm_data/16/1703/2272549.html', 'http://cl.fatt.pw/htm_data/16/1703/2272549.html', 'http://cl.fatt.pw/htm_data/16/1703/2271828.html', 'http://cl.fatt.pw/htm_data/16/1703/2271828.html', 'http://cl.fatt.pw/htm_data/16/1703/2271579.html', 'http://cl.fatt.pw/htm_data/16/1703/2271579.html', 'http://cl.fatt.pw/htm_data/16/1703/2271577.html', 'http://cl.fatt.pw/htm_data/16/1703/2271577.html', 'http://cl.fatt.pw/htm_data/16/1703/2271576.html', 'http://cl.fatt.pw/htm_data/16/1703/2271576.html', 'http://cl.fatt.pw/htm_data/16/1703/2271254.html', 'http://cl.fatt.pw/htm_data/16/1703/2271254.html', 'http://cl.fatt.pw/htm_data/16/1703/2271055.html', 'http://cl.fatt.pw/htm_data/16/1703/2271055.html', 'http://cl.fatt.pw/htm_data/16/1703/2271039.html', 'http://cl.fatt.pw/htm_data/16/1703/2271039.html', 'http://cl.fatt.pw/htm_data/16/1703/2270851.html', 'http://cl.fatt.pw/htm_data/16/1703/2270851.html', 'http://cl.fatt.pw/htm_data/16/1703/2270806.html', 'http://cl.fatt.pw/htm_data/16/1703/2270806.html', 'http://cl.fatt.pw/htm_data/16/1703/2270202.html', 'http://cl.fatt.pw/htm_data/16/1703/2270202.html', 'http://cl.fatt.pw/htm_data/16/1703/2269773.html', 'http://cl.fatt.pw/htm_data/16/1703/2269773.html', 'http://cl.fatt.pw/htm_data/16/1703/2269536.html', 'http://cl.fatt.pw/htm_data/16/1703/2269536.html', 'http://cl.fatt.pw/htm_data/16/1703/2283919.html', 'http://cl.fatt.pw/htm_data/16/1703/2283919.html', 'http://cl.fatt.pw/htm_data/16/1703/2265766.html', 'http://cl.fatt.pw/htm_data/16/1703/2265766.html', 'http://cl.fatt.pw/htm_data/16/1703/2263773.html', 'http://cl.fatt.pw/htm_data/16/1703/2263773.html', 'http://cl.fatt.pw/htm_data/16/1703/2263388.html', 'http://cl.fatt.pw/htm_data/16/1703/2263388.html', 'http://cl.fatt.pw/htm_data/16/1703/2263295.html', 'http://cl.fatt.pw/htm_data/16/1703/2263295.html', 'http://cl.fatt.pw/htm_data/16/1703/2263219.html', 'http://cl.fatt.pw/htm_data/16/1703/2263219.html', 'http://cl.fatt.pw/htm_data/16/1703/2263096.html', 'http://cl.fatt.pw/htm_data/16/1703/2263096.html', 'http://cl.fatt.pw/htm_data/16/1703/2263080.html', 'http://cl.fatt.pw/htm_data/16/1703/2263080.html', 'http://cl.fatt.pw/htm_data/16/1703/2262819.html', 'http://cl.fatt.pw/htm_data/16/1703/2262819.html', 'http://cl.fatt.pw/htm_data/16/1703/2267142.html', 'http://cl.fatt.pw/htm_data/16/1703/2267142.html', 'http://cl.fatt.pw/htm_data/16/1703/2266969.html', 'http://cl.fatt.pw/htm_data/16/1703/2266969.html', 'http://cl.fatt.pw/htm_data/16/1703/2266967.html', 'http://cl.fatt.pw/htm_data/16/1703/2266967.html', 'http://cl.fatt.pw/htm_data/16/1703/2266963.html', 'http://cl.fatt.pw/htm_data/16/1703/2266963.html', 'http://cl.fatt.pw/htm_data/16/1703/2266020.html', 'http://cl.fatt.pw/htm_data/16/1703/2266020.html', 'http://cl.fatt.pw/htm_data/16/1703/2273658.html', 'http://cl.fatt.pw/htm_data/16/1703/2273658.html', 'http://cl.fatt.pw/htm_data/16/1703/2274092.html', 'http://cl.fatt.pw/htm_data/16/1703/2274092.html', 'http://cl.fatt.pw/htm_data/16/1703/2284793.html', 'http://cl.fatt.pw/htm_data/16/1703/2284793.html', 'http://cl.fatt.pw/htm_data/16/1703/2284567.html', 'http://cl.fatt.pw/htm_data/16/1703/2284567.html', 'http://cl.fatt.pw/htm_data/16/1703/2284565.html', 'http://cl.fatt.pw/htm_data/16/1703/2284565.html', 'http://cl.fatt.pw/htm_data/16/1703/2284381.html', 'http://cl.fatt.pw/htm_data/16/1703/2284381.html', 'http://cl.fatt.pw/htm_data/16/1703/2283225.html', 'http://cl.fatt.pw/htm_data/16/1703/2283225.html', 'http://cl.fatt.pw/htm_data/16/1703/2284729.html', 'http://cl.fatt.pw/htm_data/16/1703/2284729.html', 'http://cl.fatt.pw/htm_data/16/1703/2284727.html', 'http://cl.fatt.pw/htm_data/16/1703/2284727.html', 'http://cl.fatt.pw/htm_data/16/1703/2284718.html', 'http://cl.fatt.pw/htm_data/16/1703/2284718.html', 'http://cl.fatt.pw/htm_data/16/1703/2281115.html', 'http://cl.fatt.pw/htm_data/16/1703/2281115.html', 'http://cl.fatt.pw/htm_data/16/1703/2284702.html', 'http://cl.fatt.pw/htm_data/16/1703/2284702.html', 'http://cl.fatt.pw/htm_data/16/1703/2284696.html', 'http://cl.fatt.pw/htm_data/16/1703/2284696.html', 'http://cl.fatt.pw/htm_data/16/1703/2284652.html', 'http://cl.fatt.pw/htm_data/16/1703/2284652.html', 'http://cl.fatt.pw/htm_data/16/1703/2284583.html', 'http://cl.fatt.pw/htm_data/16/1703/2284583.html', 'http://cl.fatt.pw/htm_data/16/1703/2284562.html', 'http://cl.fatt.pw/htm_data/16/1703/2284562.html', 'http://cl.fatt.pw/htm_data/16/1703/2284550.html', 'http://cl.fatt.pw/htm_data/16/1703/2284550.html', 'http://cl.fatt.pw/htm_data/16/1703/2284549.html', 'http://cl.fatt.pw/htm_data/16/1703/2284549.html', 'http://cl.fatt.pw/htm_data/16/1703/2284547.html', 'http://cl.fatt.pw/htm_data/16/1703/2284547.html', 'http://cl.fatt.pw/htm_data/16/1703/2284487.html', 'http://cl.fatt.pw/htm_data/16/1703/2284487.html', 'http://cl.fatt.pw/htm_data/16/1703/2284486.html', 'http://cl.fatt.pw/htm_data/16/1703/2284486.html', 'http://cl.fatt.pw/htm_data/16/1703/2284481.html', 'http://cl.fatt.pw/htm_data/16/1703/2284481.html', 'http://cl.fatt.pw/htm_data/16/1703/2284480.html', 'http://cl.fatt.pw/htm_data/16/1703/2284480.html', 'http://cl.fatt.pw/htm_data/16/1703/2284475.html', 'http://cl.fatt.pw/htm_data/16/1703/2284475.html', 'http://cl.fatt.pw/htm_data/16/1703/2284474.html', 'http://cl.fatt.pw/htm_data/16/1703/2284474.html', 'http://cl.fatt.pw/htm_data/16/1703/2284471.html', 'http://cl.fatt.pw/htm_data/16/1703/2284471.html', 'http://cl.fatt.pw/htm_data/16/1703/2284465.html', 'http://cl.fatt.pw/htm_data/16/1703/2284465.html', 'http://cl.fatt.pw/htm_data/16/1703/2284463.html', 'http://cl.fatt.pw/htm_data/16/1703/2284463.html', 'http://cl.fatt.pw/htm_data/16/1703/2284462.html', 'http://cl.fatt.pw/htm_data/16/1703/2284462.html', 'http://cl.fatt.pw/htm_data/16/1703/2284457.html', 'http://cl.fatt.pw/htm_data/16/1703/2284457.html', 'http://cl.fatt.pw/htm_data/16/1703/2284455.html', 'http://cl.fatt.pw/htm_data/16/1703/2284455.html', 'http://cl.fatt.pw/htm_data/16/1703/2284454.html', 'http://cl.fatt.pw/htm_data/16/1703/2284454.html', 'http://cl.fatt.pw/htm_data/16/1703/2284448.html', 'http://cl.fatt.pw/htm_data/16/1703/2284448.html', 'http://cl.fatt.pw/htm_data/16/1703/2284447.html', 'http://cl.fatt.pw/htm_data/16/1703/2284447.html', 'http://cl.fatt.pw/htm_data/16/1703/2284446.html', 'http://cl.fatt.pw/htm_data/16/1703/2284446.html', 'http://cl.fatt.pw/htm_data/16/1703/2284444.html', 'http://cl.fatt.pw/htm_data/16/1703/2284444.html', 'http://cl.fatt.pw/htm_data/16/1703/2284443.html', 'http://cl.fatt.pw/htm_data/16/1703/2284443.html', 'http://cl.fatt.pw/htm_data/16/1703/2284319.html', 'http://cl.fatt.pw/htm_data/16/1703/2284319.html', 'http://cl.fatt.pw/htm_data/16/1703/2284096.html', 'http://cl.fatt.pw/htm_data/16/1703/2284096.html', 'http://cl.fatt.pw/htm_data/16/1703/2283886.html', 'http://cl.fatt.pw/htm_data/16/1703/2283886.html', 'http://cl.fatt.pw/htm_data/16/1703/2283792.html', 'http://cl.fatt.pw/htm_data/16/1703/2283792.html', 'http://cl.fatt.pw/htm_data/16/1703/2284308.html', 'http://cl.fatt.pw/htm_data/16/1703/2284308.html', 'http://cl.fatt.pw/htm_data/16/1703/2284302.html', 'http://cl.fatt.pw/htm_data/16/1703/2284302.html', 'http://cl.fatt.pw/htm_data/16/1703/2284009.html', 'http://cl.fatt.pw/htm_data/16/1703/2284009.html', 'http://cl.fatt.pw/htm_data/16/1703/2283954.html', 'http://cl.fatt.pw/htm_data/16/1703/2283954.html', 'http://cl.fatt.pw/htm_data/16/1703/2283883.html', 'http://cl.fatt.pw/htm_data/16/1703/2283883.html', 'http://cl.fatt.pw/htm_data/16/1703/2283881.html', 'http://cl.fatt.pw/htm_data/16/1703/2283881.html', 'http://cl.fatt.pw/htm_data/16/1703/2283880.html', 'http://cl.fatt.pw/htm_data/16/1703/2283880.html', 'http://cl.fatt.pw/htm_data/16/1703/2283879.html', 'http://cl.fatt.pw/htm_data/16/1703/2283879.html', 'http://cl.fatt.pw/htm_data/16/1703/2283756.html', 'http://cl.fatt.pw/htm_data/16/1703/2283756.html', 'http://cl.fatt.pw/htm_data/16/1703/2283686.html', 'http://cl.fatt.pw/htm_data/16/1703/2283686.html', 'http://cl.fatt.pw/htm_data/16/1703/2283685.html', 'http://cl.fatt.pw/htm_data/16/1703/2283685.html', 'http://cl.fatt.pw/htm_data/16/1703/2283684.html', 'http://cl.fatt.pw/htm_data/16/1703/2283684.html', 'http://cl.fatt.pw/htm_data/16/1703/2283642.html', 'http://cl.fatt.pw/htm_data/16/1703/2283642.html', 'http://cl.fatt.pw/htm_data/16/1703/2283497.html', 'http://cl.fatt.pw/htm_data/16/1703/2283497.html']
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    imglist2 = []
    for x in a:
        try:
            r1 = urllib2.urlopen(x).read()
            imgre1 = re.compile(r'http[^\']*jpg\b')
            imglist1 = re.findall(imgre1, r1)
            imglist2.append(imglist1)
        except:
            continue
        time_myself.sleep(1)
    print imglist2
    f = open('D:\\jpg\\jgp.txt', 'w')
    for j in imglist2:
        print j
        f.writelines(str(j)+'\n')
    f.close()
    print "Done"