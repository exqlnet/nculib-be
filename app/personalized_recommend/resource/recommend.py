from flask import g
from app.utils.decorators import login_required
from sklearn.neighbors import KNeighborsClassifier as kNN

# g.current_user
def knn_recommend(n=None):
    """k近邻推荐算法"""
    k = kNN(n_neighbors=n)  # 选择k近邻k值为n(默认为5)
    ...
    return k.kneighbors(return_distance=False)  # 不返回最近距离，只返回最近点索引


def user_based_recommend():
    """推荐 基于兴趣相似的用户"""
    ...


def collect_based_recommend():
    """推荐 基于相似的收藏书单"""
    ...


def type_recommend():
    """推荐 基于感兴趣书目的类型"""
    ...


def score_recommend():
    """推荐 基于网络评价"""
    ...

def language_recommend():
    """推荐 基于语种"""
    ...
