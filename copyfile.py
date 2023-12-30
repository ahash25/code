sfile=input("enter source file:")
try:
    sf=open(sfile,"rb")
    tfile=input("enter target file:")
    tf=open(tfile,"wb")
    tf.write(sf.read())
    sf.close()
    tf.close()
    print("file copied....")
except FileNotFoundError as e:
    print(e)
