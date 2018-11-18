import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.serif'] = ['Source Han Serif SC']
mpl.rcParams['axes.unicode_minus'] = False

#相关系数是衡量两个变量的相关程度
#协方差描述两个变量的变化趋势，趋势一致为正，趋势相反为负，相互独立为0
#数据依次为 点击量  喜欢的数量  不喜欢的数量  评论数量
video_data_number_labels = ['click_number','like_number','dislike_number','comments_number']
#美国youtube群体行为分析
us_video_data_number = np.loadtxt("/root/PycharmProjects/data_analysis/data/US_video_data_numbers.csv", delimiter=",", dtype=int)
mean_us_video_data_number = [np.mean(us_video_data_number[:,0]),np.mean(us_video_data_number[:,1]),np.mean(us_video_data_number[:,2]),np.mean(us_video_data_number[:,3])]
print(us_video_data_number)
plt.style.use("ggplot")

us_video_data_number_df = pd.DataFrame()
us_video_data_number_df["click_number"] = us_video_data_number[:,0]
us_video_data_number_df["like_number"] = us_video_data_number[:,1]
us_video_data_number_df["dislike_number"] = us_video_data_number[:,2]
us_video_data_number_df["comments_number"] = us_video_data_number[:,3]

us_corr_comments_like = us_video_data_number_df['comments_number'].corr(us_video_data_number_df['like_number'])
print("youtube中美国群体评论量与喜欢的数量的相关系数"+str(us_corr_comments_like))

us_corr_comments_dislike = us_video_data_number_df['comments_number'].corr(us_video_data_number_df['dislike_number'])
print("youtube中美国群体评论量与不喜欢的数量的相关系数"+str(us_corr_comments_dislike))

us_corr_click_comments = us_video_data_number_df['click_number'].corr(us_video_data_number_df['comments_number'])
print("youtube中美国群体点击量与评论量之间的相关系数"+str(us_corr_click_comments))

us_video_data_number_df.plot(kind="box", title="Behaviour analysis about American in Youtube")
plt.show()



#英国youtube群体行为分析
gb_video_data_number = np.loadtxt("data/GB_video_data_numbers.csv", delimiter=",", dtype=int)
mean_gb_video_data_number = [np.mean(gb_video_data_number[:,0]),np.mean(gb_video_data_number[:,1]),np.mean(gb_video_data_number[:,2]),np.mean(gb_video_data_number[:,3])]
print(gb_video_data_number)
plt.style.use("ggplot")

gb_video_data_number_df = pd.DataFrame()
gb_video_data_number_df["click_number"] = gb_video_data_number[:,0]
gb_video_data_number_df["like_number"] = gb_video_data_number[:,1]
gb_video_data_number_df["dislike_number"] = gb_video_data_number[:,2]
gb_video_data_number_df["comments_number"] = gb_video_data_number[:,3]

corr_comments_like = gb_video_data_number_df['comments_number'].corr(gb_video_data_number_df['like_number'])
print("youtube中英国群体评论量与喜欢的数量的相关系数"+str(corr_comments_like))

corr_comments_dislike = gb_video_data_number_df['comments_number'].corr(gb_video_data_number_df['dislike_number'])
print("youtube中英国群体评论量与不喜欢的数量的相关系数"+str(corr_comments_dislike))

corr_click_comments = gb_video_data_number_df['click_number'].corr(gb_video_data_number_df['comments_number'])
print("youtube中英国群体点击量与评论量之间的相关系数"+str(corr_click_comments))
gb_video_data_number_df.plot(kind="box", title="Behaviour analysis about American in Greet Britain")
plt.show()
