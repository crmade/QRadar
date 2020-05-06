import datetime
def read (file):
        data = open(file, "r")
        cont = data.readlines()
        for x in cont:
                #print ("epoch")
                #print (cont)
                convert (x)

def convert (s):
        fmt = "%Y-%m-%d %H:%M:%S"
        t = datetime.datetime.fromtimestamp(float(s)/1000.)
        print t.strftime(fmt) # prints 2012-08-28 02:45:17


read("list.txt")
