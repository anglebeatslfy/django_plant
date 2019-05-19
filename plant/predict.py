import os.path
import tensorflow as tf
import numpy as np


#预测函数
def predict(path_img):

    #数据字典
    strings = ['七叶树', '三角枫', '加杨', '勿忘我', '十大功劳', '大果冬青', '天竺桂', '夹竹桃',
               '女贞', '安徽小檗', '广玉兰', '康乃馨', '日本樱', '月季', '木犀属', '木莲', '木蓖麻', '木蓝', '杜鹃花', '栾树', '桂花', '桃树', '桃花', '梅花',
               '樟树', '樱花', '橘树', '洛神花', '海桐', '滇楠', '牡丹', '牵牛花', '玫瑰',
               '短毛竹', '箭木', '紫罗兰', '紫荆', '紫薇', '罂粟花', '罗汉松', '腊梅', '茉莉花', '荷花', '菊花', '蒲公英', '郁金香', '银杏', '雪松', '风信子',
                '香椿', '鸡爪枫', '鹅掌楸']
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_gfile = os.path.join(BASE_DIR, 'plant/newpb/nn.pb')
    with tf.gfile.GFile(path_gfile, 'rb') as f:#模型加载
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')#导入计算图

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('output/prob:0')
        image_data = tf.gfile.FastGFile(path_img, 'rb').read()
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})  #
        predictions = np.squeeze(predictions)
        top_k = predictions.argsort()[::-1]
        predictions_dict = {strings[idx]: predictions[idx] for idx in top_k[0:10]}

    return predictions_dict

