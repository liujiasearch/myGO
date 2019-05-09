import h5py

class HDF5:
    def __init__(self,handle=None):
        self.f_handle=handle

    def setMode(self,file_name,mode):
        self.f_handle=h5py.File(file_name,mode)

    def setValue(self,dir,file,data):
        strings=dir+'/'+file
        self.f_handle[strings]=data
        