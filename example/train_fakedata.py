import sys,os

lib_path = os.path.join(os.environ['RCNNDIR'],'lib')
if not lib_path in sys.path:
    sys.path.insert(0,lib_path)

from rcnn_train.trainer import train_net
from rcnn_train.toydata import toydata_gen
from vgg_faster_rcnn import vgg

net = vgg()
train_io = toydata_gen()
val_io   = toydata_gen()

net.set_input_shape([1,512,512,1])

train_net(net, 'out','log', train_io, val_io)


