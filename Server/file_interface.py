import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def post(self,params=[]):
        try:
            print("params : {}".format(params))
            namafile = params[0]
            isifile =base64.b64decode(params[1])
            f = open(namafile,'wb+')
            f.write(isifile)
            f.close()
            return dict(status='OK',keterangan='file {} sudah terkirim'.format(namafile))
        except Exception as e:
            return dict(status='ERROR',keterangan='[ERROR]:'+str(e))
    def delete(self,params=[]):
        try:
            filename = params[0]
            if not filename:
                return dict(status='ERROR', keterangan='file {} tidak ditemukan'.format(filename))
            os.remove(filename)
            return dict(status='OK', keterangan='Sukses menghapus {}'.format(filename))
        except Exception as e:
            return dict(status='[ERROR]', keterangan=str(e))
            
if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
